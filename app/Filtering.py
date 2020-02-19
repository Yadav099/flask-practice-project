from app import app
from flask import request
from app.models import User
import datetime


@app.route('/Home/userlist/',methods=['GET'])
def filtering():
    type=request.args['type']
    l=[]
    if type=='city':
        region=request.args['region']
        user = User.query.all()
        for row in user:
            if row.state== region:
                l.append(row.name)
    if type=='time':
        time=request.args['time']
        user = User.query.all()
        for row in user:
            difference=time-row.registerationDate
            durations=difference.total_seconds()
            l.append(durations)


    return format(l)


