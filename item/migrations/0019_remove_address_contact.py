# Generated by Django 3.0.5 on 2020-04-14 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_address_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='contact',
        ),
    ]
