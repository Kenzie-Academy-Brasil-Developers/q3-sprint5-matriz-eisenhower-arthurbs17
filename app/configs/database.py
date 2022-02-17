from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configs import env

db = SQLAlchemy()

def init_app(app: Flask):
    env.init_app(app)

    db.init_app(app)

    app.db = db