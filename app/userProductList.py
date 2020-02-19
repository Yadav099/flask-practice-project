from flask import request
from app import app
import csv
import io
from _datetime import datetime
from app import db
from app.models import UserProductView




# Register product with csv
@app.route('/Home/OrdersList', methods=['POST'])
def userproduct():
    f = request.files['UserProductList']
    if not f:
        return "No file"
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = list(csv.DictReader(stream))
    for row in csv_input:
        us = UserProductView(up_id=row['id'], userId=row['userId'], productId=row['productId'],quantity=row['quantity'],o_id=row['orderId'])
        db.session.add(us)
        db.session.commit()
    return "done"