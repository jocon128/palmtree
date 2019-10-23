from flask import Blueprint, render_template
from flask import request, session
from .models import Listing


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    listing = Listing.query.all()
    return render_template('index.html', listings=listing)
