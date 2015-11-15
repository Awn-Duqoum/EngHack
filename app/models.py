from flask.ext.security import UserMixin, RoleMixin
from app import db

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  subject = db.Column(db.String(64))
  start_date = db.Column(db.Date, index=True)
  end_date = db.Column(db.Date)
  all_day = db.Column(db.Boolean)
  start_time = db.Column(db.DateTime, index=True)
  end_time = db.Column(db.DateTime)
  location = db.Column(db.String(100))
  description = db.Column(db.String(500))
  class_id = db.Column(db.String, index=True)

  def __repr__(self):
  	return "{} {} {} {} {} {} {} {}".format(self.subject, self.start_date.strftime("%m/%d/%y"), self.end_date.strftime("%m/%d/%y"), str(self.all_day), self.start_time.strftime("%I:%M %p"), self.end_time.strftime("%I:%M %p"), self.location, self.description, self.class_id) 

  def to_json(self):
    return {
      'subject': self.subject,
      'start_date': self.start_date.strftime("%m/%d/%y"),
      'end_date': self.end_date.strftime("%m/%d/%y"),
      'all_day': str(self.all_day),
      'start_time': self.start_time.strftime("%I:%M %p"),
      'end_time': self.end_time.strftime("%I:%M %p"),
      'location': self.location,
      'description': self.description,
      'class_id': self.class_id
    }

class Class(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	class_id = db.Column(db.String(10), index=True, unique=True)
	name = db.Column(db.String(100))

	def to_json(self):
		return{
		  'class_id': self.class_id,
		  'name': self.name
	}

# Define models
roles_users = db.Table('roles_users',
  db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
  db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))

# Define the User data model. Make sure to add the flask_user.UserMixin !!
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean())
  confirmed_at = db.Column(db.DateTime())
  roles = db.relationship('Role', secondary=roles_users,
                          backref=db.backref('users', lazy='dynamic'))
