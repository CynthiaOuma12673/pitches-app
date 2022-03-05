from flask_wtf import FlaskForm
from wtforms import StrongField, PasswordField,SubmitField, ValidationError, BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class RegistrationForm(FlaskForm):
    email = StrongField('Enter Your Email Address', validators=[Required(), Email()])
    username = StrongField('Enter Your username', validators = [Required()])
    password = PasswordField('Input password', validators = [Required(),EqualTo('password_confirm', message = 'Kindly input matching passwords')])
    password_confirm = PasswordField('Kindly confirm password', validators = [Required()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StrongField ('Enter Your Email Address', validators = [Required(), Email()])
    password = PasswordField('Input Password', validators = [Required()])
    remember = BooleanField('Save password')
    submit = SubmitField('Sign In')
    