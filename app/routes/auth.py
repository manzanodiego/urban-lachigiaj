from flask import Blueprint, request, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login_auth():
    return render_template('auth/login.html')


@bp.route('/registro')
def registro_usuario():
    return render_template('auth/registro.html')
        