# Project
## Online Marketplace ##
### Authors ###
* [Nathalie Paquin](https://github.com/natpaq "natpaq") - 260803327 - *Team Programming for Accounts and Item Apps*
* [Aidan Wadin](https://github.com/awadin "awadin") - 260716182 - *Team Programming for Accounts and Item Apps*
* [Michelle Lin](https://github.com/mchll-ln "mchll-ln") - 260865595 - *Worked on Chat App* 

### Getting Started ###
#### Prerequisite Installations ####
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

### Deployment ###
Once everything necessary is installed, run the program with:
```
$ python manage.py runserver
```
Superuser username: jimmy  
Superuser password: 1234 

Please NOTE: When checking out, please use the dev tool credit card number: 42 repeating (ex. 4242424242424242) across the input bar.
This is the Stripe "test" card number. 

### Running the tests ###
In order to run the test cases, use the following command:
```
$ python manage.py test
```

### Main Contributions ###

Aidan:
- Designed main UI (buttons and overall design)
- Created item posting 
- Created test cases
- Managed form checking (valid forms or not)
- Managed item inventory checks (valid to add to cart or not)
- Did general debugging
- Generated Stripe integration
- Collaborated on implementation of checkout pipeline 
- Collaborated on managing item editing
- Code refactoring
- Edited video Demo
- Added Messages to certian actions

Nathalie:
- Implemented user sign up, login and logout
- Enabled users to add item listings
- Collaborated on managing item editing
- Created different views for empty cart / no order cases
- Enabled different user options depending on authentication status
- Various bug fixes
- Code refactoring
- Ensured design consistencies for item and accounts app templates
- Collaborated on implementation of checkout pipeline
- Created favicon

Michelle:
- Coded front end and back end for chat application
- Created UI for chat app
- Configured the Websocket and ASGI Consumer
- Implemented validity input checks for chat app

