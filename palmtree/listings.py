from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from .models import Listing, User
from .forms import ListingForm
# from . import db

# create a blueprint
bp = Blueprint('listing', __name__, url_prefix='/listings')

# #create a page that will show the details fo the destination
@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first()
    return render_template('listings/show.html', listing=listing)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = ListingForm()
    print('Method type: ', request.method)
    if form.validate_on_submit():
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

# if the form was successfully submitted
    # access the values in the form data
#    destination = Destination(name=form.name.data,
#                description=form.description.data,
#                image=form.image.data,
#                currency=form.currency.data)
    # add the object to the db session
#    db.session.add(destination)
    # commit to the database
#    db.session.commit()
