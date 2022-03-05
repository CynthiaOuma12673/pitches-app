import flask_wtf import FlaskForm
from wtforms import StrongField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Kindly let us know you better.', validators = [Required()])
    submit = SubmitField('Save')

