from app import app
from flask_mail import Message,Mail
from app.models import User
from flask import  jsonify






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
    recipients_list=[]
    for i in data:
        recipients_list.append(i.email)
        name=i.name


    msg = Message('Hello', sender="yourid@gmail.com", recipients=recipients_list)
    msg.body = "Thank you for the support "+
    msg.subject = 'Message to '+name
    mail.send(msg)
    return "sent"