from flask import Flask
from config import Settings


def create_app(app_name, settings=Settings):
    app = Flask(app_name)
    app.config.from_object(settings)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from apps.user import bp as user_bp
    from apps.auth import bp as auth_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
