from app import app, db, models
import json
import random

@app.route('/')
@app.route('/hello_world')
def hello_world():
  return "Hello, world!"

@app.route('/test/list')
def list():
  return json.dumps(map(lambda x: x.value, models.Test.query.all()))


@app.route('/test/add')
def add():
  t = models.Test(value = random.randint(0, 100))
  db.session.add(t)
  db.session.commit()
  return list()
