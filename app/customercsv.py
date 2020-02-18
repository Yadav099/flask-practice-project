from flask import request, jsonify
from app import app
import csv
import io
from app import db
from app.models import User

# registration
@app.route('/Home/Register', methods=['POST'])
def customercsv():
    f = request.files['Customer']
    if not f:
        return "No file"
    l=[]
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input =list( csv.DictReader(stream))
    for row in csv_input:
        us = User(name=row['first_name'],lastname=row['last_name'],gender=row['gender'], email=row['email'], age=row['age'], city=row['address'],state=row['state'],zipcode=row['zipcode'],phonenumber=row['phoneNumber'],registerationDate=row['registerationDate'],accepted=False)
        db.session.add(us)
        db.session.commit()
    return 'Data acquired'


