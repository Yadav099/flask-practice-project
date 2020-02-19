
from app.models import User
from flask import request
from app import app
import csv
import io
from app import db
from app.models import Products


# Register product with csv
@app.route('/Home/Register/Productcsv/', methods=['POST'])
def ordercsv():
    f = request.files['Product']
    if not f:
        return "No file"
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input =list( csv.DictReader(stream))

    for row in csv_input:
        us = Products(id=row['id'],SKU=row['SKU'],productName=row['productName'],brand=row['brand'], productDescription=row['productDescription'])
        db.session.add(us)
        db.session.commit()
    return "Data aquired"


   # check your product data
@app.route('/Home/Products', methods=['GET'])
def checkproductprofile():
    id=request.args['id']
    user = Products.query.filter_by(id=id).first()
    if user==None:
        return "No data"
    else:
        message=" Name:" + user.productName + "</br> SKU:" + user.SKU + "</br> brand:"+user.brand+"</br> Product Description"+user.productDescription;
        return message





# registration of customers using csv
@app.route('/Home/Register/Customercsv/', methods=['POST'])
def customercsv():
    f = request.files['Customer']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input =list( csv.DictReader(stream))
    for row in csv_input:
        us = User(id=row['id'],name=row['first_name'],lastname=row['last_name'],gender=row['gender'], email=row['email'], age=row['age'], city=row['address'],state=row['state'],zipcode=row['zipcode'],phonenumber=row['phoneNumber'],registerationDate=row['registerationDate'],accepted=False)
        db.session.add(us)
        db.session.commit()
    return 'Data aquired'


   # check your profile data
@app.route('/Home/Profile/Customercsv/<name>', methods=['GET'])
def checkuserprofile(name):

    user = User.query.filter_by(name=name).first()
    if user!=None:
        message=" Name:" + user.name + "</br> mail id:" + user.email + "</br>  Age:" + format(user.age)+"</br> Address:"+user.city;
        return message
    else:
        return "No data"
