from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DateField, TimeField, DateTimeField
from wtforms.validators import DataRequired

class RegistrationForm(Form):
    email = StringField('email', validators=[])
    password = StringField('password', validators=[])

class LoginForm(Form):
    email = StringField('email', validators=[])
    password = StringField('password', validators=[])

class AddClassForm(Form):
	class_id = StringField('ClassID', validators=[DataRequired()])
	name = StringField('ClassName', validators=[DataRequired()])


class AddEventForm(Form):
	class_id = StringField('ClassID', validators=[DataRequired()])
	subject = StringField('Subject', validators=[DataRequired()])
	start_date = DateField('StartDate', format='%m/%d/%y', validators=[DataRequired()])
	end_date = DateField('EndDate', format='%m/%d/%y', validators=[DataRequired()])
	all_day = BooleanField('AllDay', default=False])
	start_time = TimeField('StartTime', format='%I:%M %p', validators=[DataRequired()])
	end_time = TimeField('EndTime', format='%I:%M %p', validators=[DataRequired()])
	location = StringField('Location', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	