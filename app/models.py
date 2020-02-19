from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    email = db.Column(db.String(120))
    age = db.Column(db.Integer)
    city = db.Column(db.String(120))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)
    registerationDate = db.Column(db.DateTime)
    phonenumber = db.Column(db.String(64))
    accepted = db.Column(db.Boolean)
    UserProductView=db.relationship('UserProductView',backref='user',lazy=True)


class Employee(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    e_name = db.Column(db.String(64))
    e_email = db.Column(db.String(120))
    e_password = db.Column(db.String(120))


class MailTemplate(db.Model):
    h_id = db.Column(db.Integer, primary_key=True)
    html_first = db.Column(db.String(128))
    html_middle = db.Column(db.String(128))
    html_last = db.Column(db.String(128))


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.String(128))
    productName = db.Column(db.String(128))
    brand = db.Column(db.String(64))
    productDescription = db.Column(db.Text)
    UserProductView=db.relationship('UserProductView',backref='products',lazy=True)




class Orders(db.Model):
    o_id = db.Column(db.Integer, primary_key=True)
    date_of_purchase = db.Column(db.Date)
    totalPrice = db.Column(db.Integer)
    UserProductView=db.relationship('UserProductView',backref='orders',lazy=True)

class UserProductView(db.Model):
    up_id=db.Column(db.Integer, primary_key=True)
    userId=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    productId=db.Column(db.Integer, db.ForeignKey('products.id'),nullable=False)
    quantity=db.Column(db.Integer)
    o_id=db.Column(db.Integer, db.ForeignKey('orders.o_id'),nullable=False)
    review = db.relationship('Review', backref='user_product_view', lazy=True)


class Review(db.Model):
    r_id = db.Column(db.Integer, primary_key=True)
    userProductId = db.Column(db.Integer, db.ForeignKey('user_product_view.up_id'),nullable=False)
    productRating = db.Column(db.Integer)
    reviewTitle = db.Column(db.String(64))
    reviewDetails = db.Column(db.Text)
