from app import app, db, models, user_datastore, forms, login_manager
from flask.ext.login import login_user, logout_user, login_required, current_user
import json
import random
import datetime
import sys

from flask.ext.security import AnonymousUser

login_manager.anonymous_user = AnonymousUser

@login_manager.unauthorized_handler
def unauthorized():
  return 'Unauthorized!', 401

@login_manager.user_loader
def load_user(user_id):
    return user_datastore.find_user(id=user_id)

@app.route('/accounts/register', methods=['POST'])
def register():
  form = forms.RegistrationForm()
  if form.validate_on_submit():
    user_datastore.create_user(email=form.email.data, password=form.password.data)
    db.session.commit()
    return '', 200
  for field, errors in form.errors.items():
    for error in errors:
      print(error)
  return '', 403


@app.route('/accounts/logout', methods=['POST', 'GET'])
def logout():
  logout_user()
  return ''

@app.route('/accounts/login', methods=['POST'])
def login():
  form = forms.LoginForm()
  if form.validate_on_submit():
    login_user(user_datastore.find_user(email=form.email.data, password=form.password.data))
    return '', 200
  for field, errors in form.errors.items():
    for error in errors:
      print(error)
  return '', 403

@app.route('/accounts/test')
@login_required
def accounts_test():
  return 'test!'

@app.route('/accounts/list')
def list_users():
  return json.dumps(map(lambda x: x.email, models.User.query.all()))

@app.route('/')
@app.route('/hello_world')
def hello_world():
	return "Hello, world!"

@app.route('/Event/list')
def list():
	return json.dumps(map(lambda x: x.to_json(), models.Event.query.all()))

@app.route('/Event/add')
def add():
	t = models.Event(subject = "TestEvent", start_date = datetime.date(2015, 10, 25), end_date = datetime.date(2015, 10, 25), all_day=False, start_time=datetime.datetime.strptime("11:00 PM", "%I:%M %p"), end_time=datetime.datetime.strptime("11:30 PM", "%I:%M %p"), location="HiHi Home", description="This is a test case", class_id = "CS220")
	db.session.add(t)
	db.session.commit()
	return list()

@app.route('/Event/deletefirst')
def delete_first():
	db.session.delete(models.Event.query.get(1))
	db.session.commit()
	return list()

@app.route('/Event/deleteall')
def delete_all():
	for E in models.Event.query.all():
		db.session.delete(E)
	db.session.commit()
	return list()

@app.route('/Event/Query')
def Qry():
	if (models.Event.query.filter_by(class_id = 'CS220').first() == None):
		return "Doesn't exist"
	else:
		return json.dumps(map(lambda x: x.to_json(), models.Event.query.filter_by(class_id = 'CS220')))


@app.route('/Event/add5')
def add5():
	for i in range(5):	
  		t = models.Event(subject = "TestEvent", start_date = datetime.date(2015, 10, i+1), end_date = datetime.date(2015, 10, i+1), all_day=False, start_time=datetime.datetime.strptime("11:00 PM", "%I:%M %p"), end_time=datetime.datetime.strptime("11:30 PM", "%I:%M %p"),  location="HiHi Home", description="This is a test case", class_id = "CS24{}".format(str(i)))
		db.session.add(t)
  	db.session.commit()
  	return list()

@app.route('/Class/list')
def list_class():
	return json.dumps(map(lambda x: x.to_json(), models.Class.query.all()))

@app.route('/Class/Add', methods=['POST'])
def addclass():
	#form = forms.ClassForm()
	# tempClass = models.Class(class_id = form.class_id.data, name = form.name.data)
	# try:
	# 	db.session.add(tempClass)
	# 	db.session.commit()
	# except:
	# 	return "Not a unique course number"
	return "aaaa"
