from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, ValidationError, BooleanField,TextAreaField
from wtforms.validators import InputRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Enter Your Email Address', validators=[InputRequired(), Email()])
    username = StringField('Enter Your username', validators = [InputRequired()])
    password = PasswordField('Input password', validators = [InputRequired(),EqualTo('password_confirm', message = 'Kindly input matching passwords')])
    password_confirm = PasswordField('Kindly confirm password', validators = [InputRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField ('Enter Your Email Address', validators = [InputRequired(), Email()])
    password = PasswordField('Input Password', validators = [InputRequired()])
    remember = BooleanField('Save password')
    submit = SubmitField('Sign In')
