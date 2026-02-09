from flask import Flask
from .config import Config
from .utils.extensions import db
from .routes import auth, admi, viajes, tickets

def create_app():
    app = Flask(__name__)
    app.secret_key = 'manzano-10-urbans'

    app.config.from_object('app.config.Config')
    
    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(viajes.bp)
    app.register_blueprint(tickets.bp)

    app.register_blueprint(admi.bp)
   # app.add_url_rule('/', endpoint='index')

    return app 