from app.models import User
from app import db
from flask import request, jsonify
from app import app


# registration
@app.route('/Home/Register/user', methods=['POST'])
def addmessage():
    content = request.get_json()
    us = User(name=content['name'], email=content['email'], age=content['age'], city=content['city'], accepted=False)
    db.session.add(us)
    db.session.commit()
    return 'Data acquired'

    # update existing age


@app.route('/Home/<name>/Edit/age', methods=['PUT'])
def updateage(name):
    if request.args['age'] is not None:
        user = User.query.filter_by(name=name).first()
        if user is not None:
            user.age = request.args['age']
            db.session.commit()
            return 'updated age'
        else:
            return "No Changes"
    else:
        return "No Changes"

    # update existing email address


@app.route('/Home/<name>/Edit/mail', methods=['PUT'])
def update_useremail(name):
    if request.args['email'] is not None:
        user = User.query.filter_by(name=name).first()
        if user:
            user.email = request.args['email']
            db.session.commit()
            return 'updated email'
        else:
            return 'No data changed'
    else:
        return 'No data changed'

    # update existing address


@app.route('/Home/<name>/Edit/state', methods=['PUT'])
def update_state(name):
    if request.args['region'] is not None:
        user = User.query.filter_by(name=name).first()
        if user:
            user.state = request.args['region']
            db.session.commit()
            return 'updated state'
        else:
            return 'No changes'
    else:
        return "No changes"


@app.route('/Home/<name>/Edit/zipcode', methods=['PUT'])
def update_zipcode(name):
    if request.args['zipcode'] is not None:
        user = User.query.filter_by(name=name).first()
        if user:
            user.zipcode = request.args['zipcode']
            db.session.commit()
            return 'updated zipcode'
        else:
            return 'No changes'
    else:
        return "No changes"


@app.route('/Home/<name>/Edit/Phonenumber', methods=['PUT'])
def update_phonenumber(name):
    if request.args['Phonenumber']:
        user = User.query.filter_by(name=name).first()
        if user:
            user.Phonenumber = request.args['Phonenumber']
            db.session.commit()
            return 'updated Phonenumber'
        else:
            return 'No changes'
    else:
        return "No changes"

    # check your profile data


@app.route('/Home/Profile/User/<name>', methods=['GET'])
def check_userprofile(name):
    user = User.query.filter_by(name=name).first()
    if user != None:
        return " Name:" + name + "</br> mail id:" + user.email + "</br>  Age:" + format(
            user.age) + "</br> State:" + user.state + "</br> Phonenumber:" + user.Phonenumber + "</br> Zip c:" + user.state
    else:
        return "no data"
