from app.configs.database import db
from app.models.tasks_categories import tasks_categories

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from dataclasses import dataclass

@dataclass
class CategoriesModel(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    tasks = relationship("TasksModel", secondary=tasks_categories, backref="categories")