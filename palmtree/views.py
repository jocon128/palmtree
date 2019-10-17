from flask import Blueprint,render_template
from flask import request,session
from .models import carDetails

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
