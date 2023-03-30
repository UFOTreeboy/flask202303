from flask import Flask
from .api.routes import api
from .site.routes import site
from .database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'




    app.register_blueprint(api)
    app.register_blueprint(site)

    return app