from flask import render_template, redirect, url_for, request,flash
from .import auth
from .models import user
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
from ..email import mail_message

@auth.route('/register',methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message('Welcome to Pitches App','email/welcome_user', user.email, user =user)
        return redirect(url_for('auth.login'))
        title = 'New Account'

    return render_template('auth/register.html', registration_form = form)