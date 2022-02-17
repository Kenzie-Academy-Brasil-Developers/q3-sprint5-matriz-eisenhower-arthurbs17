from app.configs.database import db
from app.exc.invalid_keys import InvalidValues
from app.models.tasks_categories import tasks_categories
from app.models.categories_model import CategoriesModel

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship,validates
from dataclasses import dataclass

@dataclass
class TasksModel(db.Model):
    id: int
    name: str
    description: str
    duration: int
    categories: CategoriesModel

    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)

    categories = relationship("CategoriesModel", secondary=tasks_categories, backref="tasks")

    @validates('importance', 'urgency')
    def check_importance_urgency_values(self, key, value):
        if value in [1, 2]:
            return value
        else:
            raise InvalidValues({key: value})