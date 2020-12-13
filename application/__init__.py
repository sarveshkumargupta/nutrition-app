from flask import Flask
from application.config import Config
from application.routes import app_bp
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap = Bootstrap(app)
    fontawesom = FontAwesome(app)

    app.register_blueprint(app_bp)

    return app
