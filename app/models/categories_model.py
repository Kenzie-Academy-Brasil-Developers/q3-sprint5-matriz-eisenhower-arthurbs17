from app.configs.database import db
from app.exc.invalid_keys import EmpytKey, InvalidKeys, InvalidUpdatedKeys

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import validates
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

    @classmethod
    def check_key_name(cls, data: dict):
        keys = data.keys()
        if not 'name' in keys:
            raise InvalidKeys(data)
        if len(data['name']) == 0:
            raise EmpytKey
    
    @classmethod
    def check_data_update(cls, data: dict):
        keys = data.keys()
        if not 'name' or not 'description' in keys:
            raise InvalidUpdatedKeys(data)
