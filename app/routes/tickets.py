
from flask import Blueprint, request, render_template
from .auth import login_requerido

bp = Blueprint('tickets', __name__, url_prefix="/tickets")


@bp.route('/detalle_ticket')
@login_requerido
def detalle_ticket():
    return render_template('tickets/detalle_boleto.html')
