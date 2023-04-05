from api.routes import api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(api)

class product(db.Model):
    __tablename__='product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    product = db.Column(db.String(100), nullable=False)