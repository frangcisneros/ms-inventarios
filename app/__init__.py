from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config
from app.route import RouteMainApp

db = SQLAlchemy()


def create_app() -> Flask:
    app_context = os.getenv("FLASK_CONTEXT")
    app = Flask(__name__)

    f = config.factory(app_context)
    app.config.from_object(f)

    route = RouteMainApp()
    route.init_app(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
