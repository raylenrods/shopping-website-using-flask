from flask_login import UserMixin
from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.Text, nullable=False)

Cart = db.Table('Cart',
                db.Column('product_id', db.Integer, db.ForeignKey('products.pid'), primary_key=True),
                db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    mobile = db.Column(db.String(60))


class Products(db.Model, UserMixin):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(20))
    image = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user = db.relationship("Users", secondary=Cart,backref=db.backref('users', lazy=True))
