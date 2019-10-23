
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
    print('Method type: ', request.method)
    

    return render_template('manage.html', form=form)
