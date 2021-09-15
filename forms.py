
from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, BooleanField
from wtforms.validators import AnyOf, Optional, NumberRange

# WTForms
class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField('Pet name')
    species = StringField('Species', validators=[AnyOf(['cat', 'dog', 'porcupine'], message='Species must be a cat, dog, or porcupine')])
    photo_url = StringField('URL for pet photo', validators=[Optional()])
    age = IntegerField('Age of Pet', validators=[NumberRange(min=1, max=30, message='Age must be betweem 1 and 30')])
    notes = TextAreaField('Notes')
    available = BooleanField("Avaiable to adopt", default="checked")

class EditPetForm(FlaskForm):
    """Form to edit a pet"""
    photo_url = StringField('URL for pet photo', validators=[Optional()])
    notes = TextAreaField('Notes')
    available = BooleanField("Avaiable to adopt", default="checked")