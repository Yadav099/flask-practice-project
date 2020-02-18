from app.models import MailTemplate
from app import db
from app import app
from flask import request, jsonify




@app.route('/mail',methods=['POST','GET'])
def html():
    if request.method=='POST':
        us = MailTemplate(html_first="<div><h1>Hello </h1>",html_middle="</br><p>It was pleasure meeting you ,hope to see you for future buisiness<p>",html_last="</br><p>Thank you</p></br>")
        db.session.add(us)
        db.session.commit()
        return 'pushed'
    else:
        user = MailTemplate.query.filter_by(h_id=3).first()
        return (user.html_first+user.html_middle +user.html_last)
