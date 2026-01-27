

from flask import Blueprint, request, render_template

bp = Blueprint('admi', __name__, url_prefix='/admi')

@bp.route('/')
def index():
    return render_template('index.html')