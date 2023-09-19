#  Happy Paws Information System Requirements

  

##  1. Users

###  1.1. End Users (Customers):

-  Can browse the product categories.
-  Have the ability to register and login.
-  Can see their basic account info
-  Can add products to their shopping cart and make a purchase.
-  Can contact through a contact form.


###  1.2. Administrators:

-  Have all the rights of the customer.
-  Can add, update and delete new products to the database.
-  Can access the admin dashboard.
-  Have the ability to promote other users.

  

###  1.3. System:

-  Provides simple user interface.
-  Handles sessions and keeps users logged in.
-  Flashes appropriate messages (success/error) to the users.

  

##  2. Data Requirements

###  2.1. Products:

-  Categories: Dog Food & Treats, Dog Beds & Baskets, Dog toys, sport & training, Dog grooming & care
-  Images
-  Description
-  Price
  
  
###  2.2. Users:

-  Username
-  Password (hashed and salted)
-  Role (Admin/Employee/User)


###  2.3. Cart:

-  List of products selected by a user
-  Quantity of each product
-  Total Price

  

##  3. Functions

###  3.1. Sorting:

-  Products should be sorted by category.
  

###  3.2. Entry:

-  New product addition, update, and deletion by admin.
-  User registration.

###  3.3. Update:

-  Users are able to update their cart (add/remove products).
-  Admins can update product details.
- Admins can promote user to employee/admin role


###  3.4. Validation:

-  Ensure valid inputs for product details.
-  Validate user registration data (e.g., unique username).
  

###  3.5. Integrity:

-  Passwords must be stored securely (hashed).
-  Protect against SQL injection and other potential security risks.


#  Documentation


##  Getting Started

This is the official documentation for the Happy Paws webshop. Here's how you can set up and run the project.
  

##  Prerequisites

-  Python 3.8+
-  Flask framework


##  Setup & Installation

 
Make sure you have the latest version of Python installed.

```bash

git  clone  https://github.com/bojan-bo/flask_web_app-CA_project.git

```


Navigate to the project directory and install the required packages:
```bash

cd  flask_web_app-CA_project

```

```bash

pip  install  -r  requirements.txt

```

##  Running The App

```bash

python3  main.py

```

##  Seed initial data
```bash
python3 seed.py
```

##  Viewing The App

Go to `http://127.0.0.1:5000`

##  Existing code used in following files

base.html:

_<!-- taken from and modified [https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/templates/base.html](https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/templates/base.html) -->_

cart.html: _<!-- taken from and modified: [https://getbootstrap.com/docs/4.0/content/tables/](https://getbootstrap.com/docs/4.0/content/tables/) -->_

home.html _<!-- Code for Slide taken from [https://getbootstrap.com/docs/4.0/components/carousel/#with-indicators--](https://getbootstrap.com/docs/4.0/components/carousel/#with-indicators--)>_

_<!-- Code for cards taken from [https://getbootstrap.com/docs/4.0/components/card/#background-and-color](https://getbootstrap.com/docs/4.0/components/card/#background-and-color) and modified -->_

login.html _<!-- taken from and modified [https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/templates/login.html](https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/templates/login.html) -->_

manage_products.html _<!-- taken from and modified [https://getbootstrap.com/docs/4.0/content/tables/--](https://getbootstrap.com/docs/4.0/content/tables/--)>_

[models.py](http://models.py)

*# taken from and modified [https://github.com/DiptoChakrabarty/flask-online-store/blob/master/split/app.py*](https://github.com/DiptoChakrabarty/flask-online-store/blob/master/split/app.py*)

*# code taken from and modified [https://github.com/diwash007/Flask-O-shop/blob/master/app/db_models.py*](https://github.com/diwash007/Flask-O-shop/blob/master/app/db_models.py*)

[forms.py](http://forms.py) *# taken from and modified [https://github.com/diwash007/Flask-O-shop/blob/master/app/admin/forms.py*](https://github.com/diwash007/Flask-O-shop/blob/master/app/admin/forms.py*)

[decorators.py](http://decorators.py)

*# code taken from and modified [https://www.programcreek.com/python/example/99647/flask_login.current_user.is_authenticated*](https://www.programcreek.com/python/example/99647/flask_login.current_user.is_authenticated*)

**init**.py *# code taken from and modified [https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py*](https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py*)

[auth.py](http://auth.py)

*# some code taken and modified from [https://github.com/diwash007/Flask-O-shop/blob/master/app/__init__.py*](https://github.com/diwash007/Flask-O-shop/blob/master/app/__init__.py*)

[views.py](http://views.py)

*# Some code taken from and modified [https://flask.palletsprojects.com/en/latest/quickstart/#redirects-and-errors*](https://flask.palletsprojects.com/en/latest/quickstart/#redirects-and-errors*)

[main.py](http://main.py) *# taken from and modified [https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/main.py*](https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/main.py*)

## License

All code in this repository is released under a standard open license. This means that you are free to use, modify, and distribute the code as you see fit, provided you adhere to the terms of the license.

Please make sure to check the specific license details for any third-party libraries or components used within this project to ensure compliance.
