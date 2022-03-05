from flask import render_template, redirect, url_for, request,flash
from .import auth
from .models import user
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
from ..email import mail_message
