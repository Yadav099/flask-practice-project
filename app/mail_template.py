from app.models import MailTemplate
from app import db
from app import app
from flask import request, jsonify




@app.route('/mail',methods=['POST','GET'])
def html():
    if request.method=='POST':
        us = MailTemplate(html="<div><h1>Hi ,</h1> </br><p>Thank you for the information</p></div> ")
        db.session.add(us)
        db.session.commit()
        return 'pushed'
    else:
        user = MailTemplate.query.filter_by(h_id=2).first()
        return user.html
