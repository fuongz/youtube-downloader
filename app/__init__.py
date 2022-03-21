import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

ma = Marshmallow()
api = Api()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(os.environ.get('APP_SETTINGS'))
    ma.init_app(app)
    api.init_app(app)

    with app.app_context():
        from . import routes
        return app
