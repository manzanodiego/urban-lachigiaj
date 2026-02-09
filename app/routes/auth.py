from flask import Blueprint, request, render_template, jsonify, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from app.models import User
from app.utils.extensions import db

bp = Blueprint('auth', __name__, url_prefix='/auth')




@bp.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        numero_telefono = request.form.get('numero_telefono')
        contraseña_usuario = request.form.get('contraseña_usuario')
        
        password_hash = generate_password_hash(contraseña_usuario)

        usuario = User(
            nombre = nombre_usuario, 
            numero_telefono = numero_telefono, 
            contrasena = password_hash
        )
        ##session['username'] = User.nombre
        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('viaje.mostrar_viaje'))

    return render_template('auth/registro.html')





@bp.route('/login_auth', methods=['GET', 'POST'])
def login_auth():
    if request.method == 'POST':
        numero_tel = request.form.get('numero_telefono')
        contraseña_usuario = request.form.get('contraseña')

        user_login = User.query.filter_by(numero_telefono = numero_tel).first()
        # 2. Validar existencia y contraseña
        if user_login and check_password_hash(user_login.contrasena, contraseña_usuario):
            # 3. Guardar en sesión (Usa el objeto user_login, no la clase User)
            session['username'] = user_login.nombre
            session['user_id'] = user_login.iduser
            return redirect(url_for('viaje.mostrar_viaje'))
        
        # 4. Manejo de error si falla
        return "Usuario o contraseña incorrectos", 401
        
    return render_template('auth/login.html')


@bp.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('username', None)
    return redirect(url_for('auth.login_auth'))



def login_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login_auth'))
        return f(*args, **kwargs)
    return decorated_function
        







@bp.route('/users', methods = ['GET'])
def users():
    usuarios = User.query.all()
    return jsonify([
        {
            "id": usuario.iduser, 
            "nombre": usuario.nombre,
            "telefono": usuario.numero_telefono,
            "contraseña": usuario.contrasena,
            "tipo": usuario.tipo.value if hasattr(usuario.tipo, 'value') else str(usuario.tipo)
        }
        for usuario in usuarios
    ])

