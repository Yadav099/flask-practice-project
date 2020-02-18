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
    if request.args['age'] != '':
        admin = User.query.filter_by(name=name).first()
        admin.age = request.args['age']
        db.session.commit()
        return 'updated age' + request.args['age']




    # update existing email address
@app.route('/Home/<name>/updatemail/', methods=['PUT'])
def update_useremail(name):
    if request.args['email'] != '':
        admin = User.query.filter_by(name=name).first()
        admin.email = request.args['email']
        db.session.commit()
        return 'updated email' + request.args['email']


    # update existing address
@app.route('/Home/<name>/changecity/', methods=['PUT'])
def update_city(name):
    if request.args['city'] != '':
        admin = User.query.filter_by(name=name).first()
        admin.city = request.args['city']
        db.session.commit()
        return 'updated city' + request.args['city']

