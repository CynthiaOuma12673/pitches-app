import flask_wtf import FlaskForm
from wtforms import StrongField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Kindly let us know you better.', validators = [Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField ('Kindly leave a comment', validators = [Required()])
    submit = SubmitField('Comment')