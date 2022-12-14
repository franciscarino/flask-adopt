"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for pets."""

    name = StringField("Pet Name",
                        validators=[InputRequired()] )
    species = SelectField("Species",
                            choices = [('cat', 'Cat'),
                             ('dog', 'Dog'),
                              ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL",
                               validators=[Optional(), URL()])
    age = SelectField("Age",
                            choices = [('baby', 'Baby'),
                                    ('young', 'Young'),
                                    ('adult', 'Adult'),
                                    ('senior', 'Senior')])
    notes = TextAreaField('Notes',
                                validators = [Optional()])

class EditPetForm(FlaskForm):
    """Form to edit a pet"""
    photo_url = StringField("Photo URL",
                               validators=[Optional(), URL()])
    notes = TextAreaField('Notes',
                                validators = [Optional()])
    available = BooleanField('Available?')
