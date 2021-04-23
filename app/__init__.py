# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from datetime import datetime
import os
from flask_restful import Api
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from app.resources.main_resource import UserRegister
from app.resources.main_resource import StudentRegister
from flask_migrate import Migrate, MigrateCommand
# from flask_marshmallow import Marshmallow 
from app.db import db
from app.ma import ma


# Instantiate Flask extensions


migrate = Migrate()

# Initialize Flask Application
def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load common settings
    app.config.from_object('app.settings')
    # Load environment specific settings
    app.config.from_object('app.local_settings')
    # Load extra settings from extra_config_settings param
    app.config.update(extra_config_settings)

    # ma = Marshmallow(app)

    api = Api(app)
    # Setup Flask-SQLAlchemy
    db.init_app(app)

    ma.init_app(app)
    # Setup Flask-Migrated 
    migrate.init_app(app, db)

    # Register blueprints
    # from .views import register_blueprints
    # register_blueprints(app)

    api.add_resource(UserRegister, '/register')
    api.add_resource(StudentRegister, '/student')
    # Define bootstrap_is_hidden_field for flask-bootstrap's bootstrap_wtf.html
    return app
