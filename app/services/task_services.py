from flask import current_app
from sqlalchemy import Table

from app.models.categories_model import CategoriesModel
from app.models.tasks_model import TasksModel
from app.models.tasks_categories import tasks_categories

def match_priority(importance: int, urgency: int):
    priority_quadrants = [["Do It First", "Delegate It"], ["Schedule It", "Delete It"]]
    classification = priority_quadrants[importance - 1][urgency - 1]
    return classification


def check_categories(data: list, task: TasksModel):
    session = current_app.db.session
    
    for category in data:
        category = category.lower()
        db_category: CategoriesModel = CategoriesModel.query.filter_by(
            name=category).one_or_none()
        
        if not db_category:
            db_category = CategoriesModel(name=category)
            session.add(db_category)
            session.commit()

        task.categories.append(db_category)