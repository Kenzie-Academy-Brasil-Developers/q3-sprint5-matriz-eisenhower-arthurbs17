from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):

    from app.models import CategoriesModel, EisenhowerModel, tasks_categories, TasksModel

    Migrate(app, app.db)