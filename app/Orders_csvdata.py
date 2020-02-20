from flask import request
from app import app
import csv
import io
from _datetime import datetime
from app import db
from app.models import Orders




# Register product with csv
@app.route('/Home/Shopping/', methods=['POST'])
def productrcsv():
    f = request.files['Orders']
    if not f:
        return "No file"
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = list(csv.DictReader(stream))
    for row in csv_input:
        x=datetime.strptime(row['purchaseDate'], '%d/%m/%Y').date()
        us = Orders(o_id=row['id'], totalPrice=row['totalPrice'], date_of_purchase=x)
        db.session.add(us)
        db.session.commit()
    return "done"

@app.route('/Home/OrdersDetails', methods=['GET'])
def checkOrderDetails():
    id=request.args['id']
    user = Orders.query.filter_by(o_id=id).first()
    message=" Order Id:" +format( user.o_id )+ "</br> Purchase Date:" +format( user.date_of_purchase) + "</br> Total price:"+format(user.totalPrice)
    return message


