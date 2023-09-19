from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from .models import Category, Product


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    role = SelectField(
        'Role', choices=[('customer', 'Customer'), ('admin', 'Admin')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PromoteForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[
                       ('customer', 'Customer'), ('employee', 'Employee'), ('admin', 'Admin')])
    submit = SubmitField('Promote')


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()], render_kw={
                       "class": "form-control"})
    description = TextAreaField('Description', validators=[
                                InputRequired()], render_kw={"class": "form-control"})
    price = FloatField('Price', validators=[InputRequired()], render_kw={
                       "class": "form-control"})
    category = QuerySelectField('Category', query_factory=lambda: Category.query.distinct(Category.name).all(),
                                get_label='name', allow_blank=False, render_kw={"class": "form-control"})

    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'])], render_kw={
                      "class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})
