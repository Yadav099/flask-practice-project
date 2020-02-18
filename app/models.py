from app import db
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120))
    age= db.Column(db.Integer)
    city= db.Column(db.String(120))
    accepted=db.Column(db.Boolean)

class Employee(db.Model):
    e_id= db.Column(db.Integer, primary_key=True)
    e_name = db.Column(db.String(64))
    e_email = db.Column(db.String(120))
    e_password= db.Column(db.String(120))

class MailTemplate(db.Model):
    h_id= db.Column(db.Integer, primary_key=True)
    html = db.Column(db.String(128))