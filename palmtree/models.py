from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def get_id(self):
        return (self.userID)

    def __repr__(self):
        return "<Name: {}, ID: {}>".format(self.userName, self.userID)


class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(2000))
    title = db.Column(db.String(80))
    image = db.Column(db.String(400))
    price = db.Column(db.String(5))
    category = db.Column(db.String(80))
    created_by = db.Column(db.Integer, db.ForeignKey('users.userID'))
    created_at = db.Column(db.String(80))
    # status_id = db.Column(db.Integer, db.ForeignKey(
    # 'listing_status.listing_id'))

    def __repr__(self):  # string print method
        return "<Name: {}>".format(self.title)


class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    bid_date = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    bidder_id = db.Column(db.Integer, db.ForeignKey('users.userID'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __repr__(self):
        return "<Bid: {}>".format(self.text)
