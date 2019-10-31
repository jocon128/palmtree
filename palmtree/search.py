from flask import (
    Blueprint, render_template
)
from .models import Listing


# create a blueprint
bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/<category>', methods=['GET', 'POST'])
def category(category):

    listings = Listing.query.filter_by(category=category)
    # Passes through to html template
    return render_template('/category.html', listings=listings, category=category)
