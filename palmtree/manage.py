
from flask import (
    Blueprint,  render_template, request
)

from .forms import ListingForm
from . import db
from .models import Listing


# create a blueprint
bp = Blueprint('manage', __name__)

# #create a page that will show the details for the destination



@bp.route('/manage', methods=['GET', 'POST'])
def manage():
    form = ListingForm()
    listing = Listing.query.all()
    print('Method type: ', request.method)
    listing = Listing.query.filter_by(carID=1).first()
    if(form.validate_on_submit()):
        carMake = form.carMake.data

    return render_template('manage.html', form=form, listing=listing)

