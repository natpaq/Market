from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Item, OrderItem, Order, Address, Payment
from django.db.models import When, Case, Sum
from django.utils import timezone
from django.contrib import messages
from . import forms

import stripe
stripe.api_key = "sk_test_PXpYgH0Kyd3yzZeGEYYoPh6800Oav1iiXB"

def add_item(request):
    context = {}
    if request.method == 'POST':
        form = forms.AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return HttpResponseRedirect(reverse('my_items'))
        context['form'] = form
    return render(request, 'list_item.html', context)


def my_items(request):
    items1 = Item.objects.all()
    items = Item.objects.filter(owner=request.user)
    context = {'items': items1}
    if (items):
       return render(request, 'my_items.html', context)
    else:
       return render(request, 'no_listed_items.html', context)


def my_cart(request):
    orderitems = OrderItem.objects.all()
    # do not throw an error if cart is empty
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {'orderitems': orderitems, 'order': order}
    except Order.DoesNotExist:
        context = {}
    return render(request, 'view_cart.html', context)


def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_inital = Order.objects.filter(user=request.user, ordered=False)
    if order_inital.exists():
        order = order_inital[0]
        if order.items.filter(item__id=item.id).exists():
            if order_item.quantity + 1 <= order_item.item.inv_count:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "This item has been updated in your cart!")
                return redirect(reverse('my_cart'))
            else:
                messages.info(request, "The quantity requested for this item exceeds our inventory!")
                return redirect(reverse('my_cart'))
        else:
            order.items.add(order_item)
            messages.info(request, "This item has been added to your cart!")
            return redirect(reverse('my_cart'))
    else:
        date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=date)
        order.items.add(order_item)
        messages.info(request, "This item has been added to your cart!")
        return redirect(reverse('my_cart'))


def remove_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_inital = Order.objects.filter(user=request.user, ordered=False)
    if order_inital.exists():
        order = order_inital[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            messages.info(request, "This item has been removed from your cart!")
            return redirect(reverse('my_cart'))
        else:
            messages.info(request, "This item was not in your cart!")
            return redirect(reverse('my_cart'))
    else:
        messages.info(request, "You do not have an active order!")
        return redirect(reverse('my_cart'))


def delete_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order = Order.objects.filter(user=request.user, ordered=False)[0]
    order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
    order.items.remove(order_item)
    order_item.delete()
    messages.info(request, "This item was removed from your cart.")
    return redirect(reverse('my_cart'))


def checkout(request):
    orderitems = OrderItem.objects.all()
    # do not throw an error if cart is empty
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        form = forms.CheckoutForm(request.POST, request.FILES)
        context = {'orderitems': orderitems, 'order': order, 'form': form}
        if request.method == 'POST':
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                state = form.cleaned_data.get('state')
                city = form.cleaned_data.get('city')
                zip = form.cleaned_data.get('zip')
                address = Address(
                    user=request.user,
                    street_address=street_address,
                    state=state,
                    city=city,
                    zip=zip
                )
                address.save()
                order.address = address
                order.save()
                return redirect(reverse(payment))
    except Order.DoesNotExist:
        context = {}
        return render(request, 'checkout_empty.html', context)
        
    return render(request, 'checkout.html', context)


def payment(request):
    orderitems = OrderItem.objects.all()
    order = Order.objects.get(user=request.user, ordered=False)
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = int(order.get_total() * 100)  # cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="cad",
                source="tok_amex",
                description="Charge from OSS"
            )

            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = request.user
            payment.amount = order.get_total()
            payment.save()

            # get all user's current unordered items in cart and set them to be 'ordered'
            orderitems = OrderItem.objects.filter(user=request.user, ordered=False)
            orderitems.update(ordered=True)
            newOrderitems = OrderItem.objects.filter(user=request.user, ordered=True)

            for orderitem in newOrderitems:
                orderitem.item.inv_count -= orderitem.quantity
                orderitem.item.save()
                orderitem.save()

            order.ordered = True
            order.payment = payment
            order.save()

            messages.info(request, "Your order was successful")
            return redirect("/")

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            # Since it's a decline, stripe.error.CardError will be caught
            messages.info(request, f"{err.get('message')}")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.info(request, "Rate limit Error")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.info(request, "Invalid Parameters")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            messages.info(request, "Not Authenticated")
            # (maybe you changed API keys recently)

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.info(request, "Network Error")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.info(request, "Something Went Wrong. You were not charged, please try again.")

        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.info(request, "A serious error occured, this will be solved shortly.")

    context = {'orderitems': orderitems, 'order': order}
    return render(request, 'payment.html', context)

def order_history(request):
    orderitems = OrderItem.objects.all()
    orders = Order.objects.all().filter(user=request.user, ordered=True)
    context = {'orderitems': orderitems, 'orders': orders}
    return render(request, 'order_history.html', context)


