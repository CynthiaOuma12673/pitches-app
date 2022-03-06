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

@main.route('/comment/<int:pitch_id>',methods = ['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        new_comment = Comment(comment = comment, pitch_id = pitch_id, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form = form, pitch = pitch, comments = comments)