<<<<<<< HEAD
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
=======
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Name: {}, ID: {}>".format(self.name, self.id)

class carDetails(db.Model):
    __tablename__='Car'
    carID = db.Column(db.Integer, primary_key=True)
    userID= db.Column(db.Integer, db.ForeignKey('hotels.id'))
    listingTitle = db.Column(db.String(250), nullable=False)
    carMake = db.Column(db.String(250  ), nullable=False)
    picture = db.Column(db.String(250  ), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<carID: {}, userID: {}, listingTitle: {}, carMake: {}, picture: {}, price: {}"
>>>>>>> 30b4d48c5ac36216b95d4abc617e563102418533
