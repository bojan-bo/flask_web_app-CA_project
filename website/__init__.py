import os
from flask_migrate import Migrate
from flask_login import LoginManager
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['STRIPE_SECRET_KEY'] = os.environ.get('STRIPE_SECRET_KEY')
    app.config['STRIPE_PUBLIC_KEY'] = os.environ.get(
        'STRIPE_PUBLIC_KEY')
    db.init_app(app)
    migrate = Migrate(app, db)

    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint
    from .models import User, Category, Product, Order, OrderItem

    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/')

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Initalize db
    # flask db init

# To generate a migration script:
    # flask db migrate -m "updated db to handle admin user"

# And to apply the migrations to the database:
    # flask db upgrade
