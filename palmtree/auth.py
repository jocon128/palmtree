from flask import (
    Blueprint, flash, render_template, url_for, redirect
)
from .models import User
from .forms import LoginForm, RegisterForm
from . import db
from flask_login import login_user

# for password storage
from werkzeug.security import generate_password_hash, check_password_hash

# create a blueprint
bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if(form.validate_on_submit()):
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(userName=username).first()

        # if there is no user with that name
        if user is None:
            error = 'Incorrect user name'
        # check the password - notice password hash function
        # takes the hash and password
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            print(user)
            # all good, set the login_user
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)
        # it comes here when it is a get method
    return render_template('user_form.html', form=form, heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Register form submitted')

        # get username, password and email from the form
        username = form.username.data
        password = form.password.data
        email = form.email.data
        # don't store the password - create password hash
        password_hash = generate_password_hash(password)
        # create a new user model object
        new_user = User(userName=username,
                        password_hash=password_hash, email=email)
        db.session.add(new_user)
        db.session.commit()
        # commit to the database and redirect to HTML page
        return redirect(url_for('auth.register'))

    return render_template('user_form.html', form=form, heading='Register')
