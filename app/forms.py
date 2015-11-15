from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class RegistrationForm(Form):
    email = StringField('email', validators=[])
    password = StringField('password', validators=[])

class LoginForm(Form):
    email = StringField('email', validators=[])
    password = StringField('password', validators=[])
