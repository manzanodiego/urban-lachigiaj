from flask import Blueprint, request, render_template


bp = Blueprint('viaje', __name__, url_prefix='/viaje')

@bp.route('/agregar_viaje')
def agregar_viaje():
    if request.method == 'POST':
        fecha = request.form('fecha')
        hora = request.form('hora')
        return 0
    

@bp.route('/mostrar_viaje')
def mostrar_viaje():
    return render_template('viajes/viajes_cliente.html')