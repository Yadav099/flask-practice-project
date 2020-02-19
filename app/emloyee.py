from app.models import User,Employee
from app import db
from app import app
from flask import request, jsonify

#delete specific user
@app.route('/Home/userlist/',methods=['DELETE'])
def delete_user():
    obj = request.args['deleteuser']
    User.query.filter_by(name=obj).delete()
    db.session.commit()
    return obj+" deleted."





# registration
@app.route('/Home/Register/company', methods=['POST'])
def add_employee():
    content = request.get_json()
    us = Employee(e_name=content['e_name'], e_email=content['e_email'], e_password=content['e_password'])
    db.session.add(us)
    db.session.commit()
    return 'Data acquired'

# update existing email address
@app.route('/Home/<e_name>/changmail', methods=['PUT'])
def update_email(e_name):
    if request.args['e_email'] != '':
        admin = Employee.query.filter_by(e_name=e_name).first()
        admin.e_email = request.args['e_email']
        db.session.commit()
        return 'updated e_email ' +request.args['e_email']

    # check your profile data
@app.route('/Home/Profile/Employee/<e_name>/', methods=['GET'])
def check_profile(e_name):

    user = Employee.query.filter_by(e_name=e_name).first()
    e_email = user.e_email
    e_password = user.e_password
    return " Name:" + e_name + ", mail id:" + e_email + ",  Age:" + e_password
#delete update