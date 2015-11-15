from app import app, db, models
import json
import random
import datetime


@app.route('/')
@app.route('/hello_world')
def hello_world():
  return "Hello, world!"

@app.route('/Event/list')
def list():
  return json.dumps(map(lambda x: x.to_json(), models.Event.query.all()))

@app.route('/Event/add')
def add():
  t = models.Event(subject = "TestEvent", start_date = datetime.date(2015, 10, 25), all_day=False, start_time=datetime.time(11, 0), end_time=datetime.time(11, 30), location="HiHi Home", description="This is a test case", class_id = "CS246")
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
	return json.dumps(map(lambda x: x.to_json(), models.Event.query.filter_by(class_id = 'CS243').order_by(models.Event.start_date).all()))

@app.route('/Event/add5')
def add5():
	for i in range(5):	
  		t = models.Event(subject = "TestEvent", start_date = datetime.date(2015, 10, i+1), all_day=False, start_time=datetime.time(11, 0), end_time=datetime.time(11, 30), location="HiHi Home", description="This is a test case", class_id = "CS24{}".format(str(i)))
		db.session.add(t)
  	db.session.commit()
  	return list()