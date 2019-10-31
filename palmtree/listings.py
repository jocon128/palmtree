from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from . import db
from .models import Listing, User, Bid
from .forms import ListingForm
from flask_login import login_required, current_user
from datetime import datetime


# create a blueprint
bp = Blueprint('listing', __name__, url_prefix='/listings')

# #create a page that will show the details of the car
@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first()
    # Passes through to html template
    return render_template('listings/show.html', listing=listing)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ListingForm(request.form)
    print('Method type: ', request.method)
    if request.method == 'POST':
        print("test")
        # datetime object containing current date and time
        now = datetime.now().isoformat()
        listing = Listing(title=form.title.data,
                          description=form.description.data,
                          image=form.image.data,
                          price=form.price.data, category=form.category.data, created_at=now)

        db.session.add(listing)
        db.session.commit()
        print('Successfully created new listing', 'success')
        flash('Successfully created new listing', 'success')
        return redirect(url_for('listing.create'))
    return render_template('listings/create.html', form=form)


@bp.route('/<listing>/bid', methods=['GET', 'POST'])
def bid(listing):
    bid = Bid(listing_id=listing, bidder_id=current_user.userID)

    db.session.add(bid)
    db.session.commit()

    # flashing a message which needs to be handled by the html
    print('Your bid has been submitted', 'success')
    # using redirect sends a GET request to destination.show
    return redirect(url_for('listing.show', id=listing))
