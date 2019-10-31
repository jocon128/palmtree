
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
    title = StringField(
        'Describe the make and model of your vehicle.', validators=[InputRequired()])
    description = TextAreaField('Describe your vehicle in detail.',
                                validators=[InputRequired(), Length(min=10, max=200)])
    image = StringField('Upload an image of your vehicle.',
                        validators=[InputRequired()])
    category = StringField('Select a relavent category',
                           validators=[InputRequired()])
    price = StringField(
        'Provide the asking price for your vehicle.', validators=[InputRequired()])
    submit = SubmitField("Create")
