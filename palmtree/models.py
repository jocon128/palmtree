from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(30), nullable=False)

    def get_id(self):
        return (self.userID)

    def __repr__(self):
        return "<Name: {}, ID: {}>".format(self.userName, self.userID)


class Listing(db.Model):
    __tablename__ = 'Car'
    carID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))

    def __repr__(self):  # string print method
        return "<Name: {}>".format(self.carMake)
