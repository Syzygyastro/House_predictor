from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    IntegerField,
    StringField,
    EmailField,
    PasswordField,
    BooleanField,
    SelectField
)
from wtforms.validators import DataRequired, ValidationError, NumberRange
from house_price_app.models import User
from house_price_app import db


class PredictionForm(FlaskForm):
    """Fields to a form to input the values required for an iris species prediction"""

    # https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.DecimalField
    year_wanted = IntegerField("Desired Year", validators=[DataRequired(), NumberRange(min= 2022, max= 2060, message=None)])
    house_type_selection = SelectField("Desired house type", choices=[('Price (All)', 'Average Houses'), ('Price (New)', 'Newer Houses'), \
    ('Price (Modern)', 'Modern houses'), ('Price (Older)', 'Older Houses')], validators=[DataRequired()])


class RegisterForm(FlaskForm):
    """Fields to a form to input the values required for adding a new user account"""

    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField(label="Email address", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember = BooleanField(label="Remember me")
