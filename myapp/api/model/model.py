from api.routes import api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(api)

class user(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)