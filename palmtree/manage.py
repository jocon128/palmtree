
from flask import (
    Blueprint,  render_template, request
)

from .forms import ListingForm
from . import db
from .models import Listing


# create a blueprint
bp = Blueprint('manage', __name__)

# #create a page that will show the details for the destination


@bp.route('/manage/<id>', methods=['GET', 'POST'])
def manage(id):
    form = ListingForm()
    listing = Listing.query.all()
    print('Method type: ', request.method)
    listing = Listing.query.filter_by(id=id).first()
    if request.method == "POST":

        listing.title = form.title.data

        listing.description = form.description.data

        listing.price = form.price.data

        listing.category = form.category.data

        db.session.commit()

    return render_template('manage.html', form=form, listing=listing)
