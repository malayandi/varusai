from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Visit

class VisitForm(Form):
    """
    Form to record a new visit
    """
    name = StringField('Name', validators=[DataRequired()])
    sid = IntegerField('Student ID', validators=[DataRequired()])

    submit = SubmitField('Log In')
