# Project
## Online Marketplace ##
An online marketplace that allows users to list products up for sale. Users are able to add, update and delete their product listings. Anyone can view the products listed for sale but only authenticated users can add items to their cart, view the total price of their cart, input shipping information and finish their check out. Users can view which items they previously purchased by checking their order history. Authenticated merchants and buyers are also able to chat with sellers in real time using a room ID.  
<img src=/project/media/images/Webpage.png width=75% height=75%>

## Getting Started ##
### Prerequisite Installations ###
The commands to install everything necessary for deployment are listed below:  
It's necessary to have Django 3.0 installed. This can be done by running the following command:
```
$ python3 -m pip install Django
```
Redis and Channels installations are also required:
```
$ sudo apt-get install redis-server
$ python3 -m pip install channels_redis
$ sudo apt-get install libssl-dev
$ python3 -m pip install -U channels
```
Lastly, Stripe installations are required:
```
$ python3 -m pip install stripe
$ python3 -m pip install --upgrade stripe
```
Please NOTE: When checking out, please use the dev tool credit card number: 42 repeating. (ex. 4242424242424242) Across the input bar.
This is the Stripe "test" card number. 
## Deployment ##
Once everything necessary is installed, run the program with:
```
$ python manage.py runserver
```

## Running the tests ##
In order to run the test cases, use the following command:
```
$ python manage.py test
```

## Authors ##
* [Nathalie Paquin](https://github.com/natpaq "natpaq") - 260803327 - *Team Programming for Accounts and Item Apps*
* [Aidan Wadin](https://github.com/awadin "awadin") - 260716182 - *Team Programming for Accounts and Item Apps*
* [Michelle Lin](https://github.com/mchll-ln "mchll-ln") - 260865595 - *Worked on Chat App* 

