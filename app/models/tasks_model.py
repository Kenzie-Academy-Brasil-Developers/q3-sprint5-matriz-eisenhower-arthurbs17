from app.configs.database import db

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from dataclasses import dataclass

@dataclass
class TasksModel(db.Model):
    id: int
    name: str
    description: str
    duration: int

    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)