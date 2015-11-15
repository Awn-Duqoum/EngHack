from app import db


class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  subject = db.Column(db.String(64))
  start_date = db.Column(db.Date, index=True)
  all_day = db.Column(db.Boolean)
  start_time = db.Column(db.Time, index=True)
  end_time = db.Column(db.Time)
  location = db.Column(db.String(100))
  description = db.Column(db.String(500))
  class_id = db.Column(db.Integer, index=True)

  def __repr__(self):
  	return "{} {} {} {} {} {} {} {}".format(self.subject, self.start_date.strftime("%m/%d/%y"), str(self.all_day), self.start_time.strftime("%I:%M %p"), self.end_time.strftime("%I:%M %p"), self.location, self.description, self.class_id) 

  def to_json(self):
    return {

    'subject': self.subject,
    'start_date': self.start_date.strftime("%m/%d/%y"),
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

  