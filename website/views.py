from flask import Blueprint, Flask, render_template, request, flash, redirect, session, url_for, current_app
from flask_login import login_required, current_user
from .models import User, Product, Category
from .forms import ProductForm, PromoteForm
from .decorators import check_admin
from . import db
import os
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
import stripe

views = Blueprint('views', __name__)

app = Flask(__name__)


def save_image(image):
    filename = secure_filename(image.filename)
    image.save(os.path.join('static', filename))
    return filename


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)


@views.route('/promote', methods=['GET', 'POST'])
@login_required
def promote():
    if current_user.role != 'admin':
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
    category = Category.query.filter_by(name=category_name).first_or_404()
    products = Product.query.filter_by(category_id=category.id).all()
    return render_template('products.html', user=current_user, products=products, category_name=category_name)


@views.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get('cart', [])
    # Check if the item is already in the cart
    for item in cart:
        if item['id'] == product.id:
            item['quantity'] = item.get('quantity', 0) + 1
            break
    else:
        # Item is not in the cart, add it
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        })
    session['cart'] = cart
    session.modified = True
    flash('Item added to cart', 'success')
    return redirect(url_for('views.products', category_name=product.category.name))


@views.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item.get('quantity', 1) for item in cart)
    return render_template('cart.html', cart={'items': cart, 'total': total})


@views.route('/remove-from-cart/<int:item_id>')
def remove_from_cart(item_id):
    cart = session.get('cart', [])
    # find the item in the cart
    item = next((item for item in cart if item['id'] == item_id), None)
    if item:
        # remove the item from the cart
        cart.remove(item)
        session['cart'] = cart
        session.modified = True
        flash('Item removed from cart', 'success')
    else:
        flash('Item not found in cart', 'error')
    return redirect(url_for('views.cart'))


@views.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    amount = int(sum(item['price'] * item.get('quantity', 1)
                 for item in cart) * 100)
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='eur',
    )
    return render_template('checkout.html', client_secret=intent.client_secret, stripe_public_key=current_app.config['STRIPE_PUBLIC_KEY'])


@views.route('/charge', methods=['POST'])
def charge():
    cart = session.get('cart', [])
    amount = int(sum(item['price'] * item.get('quantity', 1)
                 for item in cart) * 100)
    payment_method_id = request.form.get('paymentMethodId')
    if not payment_method_id:
        flash('Payment failed. Please try again.', 'error')
        return redirect(url_for('views.checkout'))

    try:
        # Create a payment intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True,
        )
        flash('Payment was successful', 'success')
        session['cart'] = []
        session.modified = True
        return redirect(url_for('views.thank_you'))
    except stripe.error.CardError as e:
        # Stripe.error.CardError will be caught
        body = e.error.get('charge')
        code = body.get('code')
        flash(f'Card has been declined. Error code: {code}', 'error')
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        flash('Too many requests made to the API too quickly. Please try again later.', 'error')
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        flash(
            'Invalid parameters were supplied to Stripe\'s API. Please try again.', 'error')
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        flash('Authentication with Stripe\'s API failed. Please try again.', 'error')
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        flash('Network communication with Stripe failed. Please try again.', 'error')
    except stripe.error.StripeError as e:
        # Display generic error to the user
        flash('An error occurred while processing your payment. Please try again.', 'error')
    except Exception as e:
        flash('An unexpected error occurred. Please try again.', 'error')

    return redirect(url_for('views.checkout'))


@views.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')


@views.route('/manage_products', methods=['GET', 'POST'])
@views.route('/manage_products/<int:product_id>', methods=['GET', 'POST'])
@login_required
@check_admin
def manage_products(product_id=None):
    products = Product.query.all()
    form = ProductForm()

    # Handle product deletion
    if request.args.get('action') == 'delete' and product_id:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
        return redirect(url_for('views.manage_products'))
    if product_id:
        product = Product.query.get_or_404(product_id)
        form = ProductForm(obj=product)

    if form.validate_on_submit():
        if product_id:  # Update existing product
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data
            product.category = form.category.data
            if form.image.data:
                image_filename = save_image(form.image.data)
                product.image = image_filename
            db.session.commit()
            flash('Product updated successfully!', 'success')
        else:  # Add new product
            new_product = Product(
                name=form.name.data,
                description=form.description.data,
                price=form.price.data,
                category=form.category.data
            )
            if form.image.data:
                image_filename = save_image(form.image.data)
                new_product.image = image_filename
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')

        return redirect(url_for('views.manage_products'))

    return render_template('manage_products.html', form=form, products=products)


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
