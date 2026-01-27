from flask import Flask

from .routes import auth, admi, viajes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.register_blueprint(auth.bp)
    app.register_blueprint(admi.bp)
    app.register_blueprint(viajes.bp)

    return app 