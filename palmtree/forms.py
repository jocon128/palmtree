
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

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
    password = PasswordField('Password', validators=[InputRequired()])
    # validator to check if the user entry is equal to password
    confirm = PasswordField('Confirm Password', validators=[
                            EqualTo('password', message='Password\'s must match')])
    # submit button
    submit = SubmitField("Register")


class ListingForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description',
                                validators=[InputRequired(), Length(min=10, max=200)])
    image = StringField('Image', validators=[InputRequired()])
    category = StringField('Category', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    submit = SubmitField("Create")
