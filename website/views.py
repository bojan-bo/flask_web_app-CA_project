from flask_login import login_user
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from flask_login import login_required, current_user
from .models import User, Product, Category
from .forms import ProductForm, PromoteForm
from .decorators import check_admin
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)


@views.route('/promote', methods=['GET', 'POST'])
@login_required
def promote():
    if session.get('role') != 'admin':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('views.home'))

    form = PromoteForm()
    if form.validate_on_submit():
        email = form.email.data
        role = form.role.data
        user = User.query.filter_by(email=email).first()
        if user:
            user.role = role
            db.session.commit()
            flash(f'User {email} has been promoted to {role}.', 'success')
        else:
            flash('User not found.', 'error')

    return render_template('promote.html', form=form)


@views.route('/our-products')
def our_products():
    categories = Category.query.all()
    return render_template('our_products.html', user=current_user, categories=categories)


@views.route('/products/<category_name>')
def products(category_name):
    category = Category.query.filter_by(name=category_name).first()
    products = Product.query.filter_by(
        category_id=category.id).all() if category else []
    return render_template('products.html', user=current_user, products=products, category_name=category_name)


@views.route('/admin/add-product', methods=['GET', 'POST'])
@login_required
@check_admin
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data,
                          description=form.description.data,
                          price=form.price.data,
                          category=form.category.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', category='success')
        return redirect(url_for('views.admin'))
    return render_template('add_product.html', form=form)


@views.route('/account')
@login_required
def account():
    return render_template("account.html", user=current_user)


@views.route('/admin')
@login_required
@check_admin
def admin():
    return render_template('admin.html', user=current_user)


@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)


@views.route('/cart')
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', user=current_user, cart=cart)


@views.route('/search')
def search():
    query = request.args.get('query')
    products = Product.query.filter(Product.name.contains(query)).all()
    return render_template('search.html', user=current_user, products=products)
