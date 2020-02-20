from app import app
from flask_mail import Message,Mail
from app.models import User
from flask import request
from app.models import MailTemplate





app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 2525
mail = Mail(app)


@app.route('/mail/sent', methods=['GET'])
def sendMessage():
    msg = Message('Hello', sender="yourid@gmail.com", recipients=['id1@gmail.com'])
    msg.body = "This is email body"
    msg.subject='Testing'
    mail.send(msg)
    return "sent"



@app.route('/Home/userlist',methods=['GET'])
def send_touser():
    data=User.query.all()
    if request.args['templateId']=='':
        templateId=3
    else:
        templateId=request.args['templateId']
    for i in data:
        msg = Message('Hello', sender="yourid@gmail.com", recipients=[i.email])

        user = MailTemplate.query.filter_by(h_id=templateId).first()
        message=user.html_first+i.name+user.html_middle+user.html_last+i.name
        msg.html =message
        msg.subject = 'Message to '
        mail.send(msg)
    return "sent"