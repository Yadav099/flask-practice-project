from app.models import User
from app import db
from flask import request, jsonify
from app import app



# registration
@app.route('/Home/Register/user', methods=['POST'])
def addmessage():
    content = request.get_json()
    us = User(name=content['name'], email=content['email'], age=content['age'],city=content['city'], accepted=False)
    db.session.add(us)
    db.session.commit()
    return 'Data acquired'




    # update existing age
@app.route('/Home/<name>/changeage/', methods=['PUT'])
def age(name):
   if  request.args['age']:
        return "NO Changes"
   else:
        user = User.query.filter_by(name=name).first()
        user.age = request.args['age']
        db.session.commit()
        return 'updated age'


    # update existing email address
@app.route('/Home/<name>/updatemail/', methods=['PUT'])
def update_useremail(name):
    if request.args['email'] :
        return "No changes"
    else:
        admin = User.query.filter_by(name=name).first()
        admin.email = request.args['email']
        db.session.commit()
        return 'updated email' + request.args['email']


    # update existing address
@app.route('/Home/<name>/changestate/', methods=['PUT'])
def update_city(name):
    if request.args['state'] :
        return "No changes"
    else:
        admin = User.query.filter_by(name=name).first()
        admin.state = request.args['state']
        db.session.commit()
        return 'updated state' + request.args['state']

