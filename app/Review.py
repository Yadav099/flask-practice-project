from flask import request
from app import app
import csv
import io
from _datetime import datetime
from app import db
from app.models import Review




# Register product with csv
@app.route('/Home/Product/Review', methods=['POST'])
def reviewcsv():
    f = request.files['Review']
    if not f:
        return "No file"
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = list(csv.DictReader(stream))
    for row in csv_input:
        us = Review(r_id=row['id'], userProductId=row['userProductId'], productRating=row['productRating'],reviewTitle=row['reviewTitle'],reviewDetails=row['reviewDetails'])
        db.session.add(us)
        db.session.commit()
    return "done"