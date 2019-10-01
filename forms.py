
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo

# creates the login information


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[
                           InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

    # this is the registration form


class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[
                        Email("Please enter a valid email")])

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")


class carForm(FlaskForm):
    carID = StringField('CarID', validators=[InputRequired()])
    userID = StringField('UserID', validators=[InputRequired()])
    listingTitle = StringField('Listing Title', validators=[InputRequired()])
    carMake = StringField('Car Make', validators=[InputRequired()])
    picture = StringField('Car Image', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    submit = SubmitField("Create")
