from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
from website import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    password = db.Column(db.String(60), nullable=False)

class Customer(User):
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    orders = db.relationship('Order', backref='customer', lazy=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    reviews = db.relationship('Review', backref='customer', lazy=True)

class Employee(User):
    employee_id = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    assigned_tasks = db.Column(db.String(100), nullable=True)

class Owner(User):
    business_name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='owner', lazy=True)
    products = db.relationship('Product', backref='owner', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    products = db.relationship('Product', backref='cart', lazy=True)
    quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    payment_type = db.Column(db.String(20), nullable=False)
    payment_status = db.Column(db.String(20), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    street_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    customers = db.relationship('Customer', backref='address', lazy=True)

