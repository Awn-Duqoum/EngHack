from app import db

class Test(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.Integer)

  def __repr__(self):
    return '<Test %r>' % self.value
