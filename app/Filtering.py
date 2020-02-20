from app import app
from flask import request
from app.models import User, Orders, Review
import datetime

#filtering the customer list
@app.route('/Home/userlist/', methods=['GET'])
def filtering():
    type_of_filter = request.args['type_of_filter']
    l = []
    if type_of_filter:

        # filter based on region

        if type_of_filter == 'city':
            region = request.args['region']
            user = User.query.all()

            for row in user:
                if row.state == region:
                    l.append(row.name)

        # filter based on range of cost

        if type_of_filter == 'totalcost':
            minimum_cost = request.args['minimum_cost']
            maximum_cost = request.args['maximum_cost']
            cost_calc = Orders.query.all()
            for row in cost_calc:
                if int(minimum_cost) < row.totalPrice < int(maximum_cost):
                    l.append(row.o_id)

        # filter based on positive and negative review count
        if type_of_filter == 'feedback':
            cost_calc = Review.query.all()
            positive = 0
            negative = 0
            for row in cost_calc:
                if row.reviewTitle.find("Love" or 'love') != -1:
                    positive += 1
                if row.reviewTitle.find("Bad" or 'bad') != -1:
                    negative += 1
            msg = "Positive feedback=" + format(positive) + "</br> Negative feedback=" + format(negative)
            l = msg
        # filtering male customer based on age range

        if type_of_filter == 'age':
            minimum_age = request.args['minimum_age']
            maximum_age = request.args['maximum_age']
            age_calc = User.query.all()
            for row in age_calc:
                if int(minimum_age) < row.age < int(maximum_age):
                    if row.gender == 'Male':
                        l.append(row.name)
        # filter based on zipcode

        if type_of_filter == 'zipcode':
            zipcode = request.args['zipcode']
            user = User.query.all()

            for row in user:
                if row.zipcode == zipcode:
                    l.append(row.name)

        return format(l)
    else:
        return 'No type selected'