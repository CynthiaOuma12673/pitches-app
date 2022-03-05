import flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Kindly let us know you better.', validators = [Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField ('Kindly leave a comment', validators = [Required()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    category = SelectField('Category', choices = [('Events', 'Events'),('Job', 'Job'), ('Advertisement', 'Advertisement')], validators = [Required()])
    post = TextAreaField('Add Your Pitch', validators = [Required()])
    submit = SubmitField('Pitch')