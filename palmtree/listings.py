from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from . import db
from .models import Listing, User
from .forms import ListingForm
from flask_login import login_required

# create a blueprint
bp = Blueprint('listing', __name__, url_prefix='/listings')

# #create a page that will show the details of the car
@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(carID=id).first()
    print("Start")
    print(listing)  # Gets listing matching id from db
    print("End")
    # Passes through to html template
    return render_template('listings/show.html', listing=listing)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ListingForm(request.form)
    print('Method type: ', request.method)
    if request.method == 'POST':
        print("test")
        listing = Listing(title=form.title.data,
                          description=form.description.data,
                          image=form.image.data,
                          price=form.price.data, category=form.category.data)

        db.session.add(listing)
        db.session.commit()
        print('Successfully created new listing', 'success')
        return redirect(url_for('listing.create'))
    return render_template('listings/create.html', form=form)


# @bp.route('/<destination>/comment', methods=['GET', 'POST'])
# def comment(destination):
#     form = CommentForm()
#     # get the destination object associated to the page and the comment
#     destination_obj = Destination.query.filter_by(id=destination).first()
#     if form.validate_on_submit():
#         # read the comment from the form
#         comment = Comment(text=form.text.data,
#                           destination=destination_obj)
#         # here the back-referencing works - comment.destination is set
#         # and the link is created
#         db.session.add(comment)
#         db.session.commit()

#         # flashing a message which needs to be handled by the html
#         print('Your comment has been added', 'success')
#     # using redirect sends a GET request to destination.show
#     return redirect(url_for('destination.show', id=destination))
