from flask import render_template, request, redirect, url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User, Pitch, Comment, Upvote, Downvote
from .forms import UpdateProfile, PitchForm, CommentForm
from ..import db,photos
import datetime

@main.route('/')
def index():
    pitches = Pitch.query.all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    product = Pitch.query.filter_by(category = 'Product').all()
    technology = Pitch.query.filter_by(category = 'Technology')
    
    return render_template('index.html', interview = interview, product = product, pitches = pitches,technology = technology, advertisement = advertisement)