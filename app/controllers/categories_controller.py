from flask import request,jsonify,current_app
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.exc.invalid_keys import EmpytKey, InvalidKeys, InvalidUpdatedKeys
from app.models.categories_model import CategoriesModel
from app.services.processing_values import processing_values

def create_category():
    session = current_app.db.session
    data = request.get_json()
    
    try:
        data = processing_values(data)
        CategoriesModel.check_key_name(data)
        new_category = CategoriesModel(**data)

        session.add(new_category)
        session.commit()
        return jsonify(new_category), HTTPStatus.CREATED

    except AttributeError:
        return jsonify({"erro": "Os valores devem ser passados em string!"}), HTTPStatus.BAD_REQUEST
    except InvalidKeys as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    except EmpytKey as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return jsonify({"msg": "category already exists!"}), HTTPStatus.CONFLICT

def update_category(category_id: int):
    session = current_app.db.session
    try:
         
        query_category: CategoriesModel = CategoriesModel.query.get_or_404(
            category_id, description = "category not found!")
            
        data = request.get_json()
        data = processing_values(data)
            
        CategoriesModel.check_data_update(data)

        for key, value in data.items():
            setattr(query_category, key, value)
        
        session.add(query_category)
        session.commit()
        
        return jsonify(query_category), HTTPStatus.OK

    except InvalidUpdatedKeys as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
   
def delete_category(category_id: int):
    session = current_app.db.session
    query_category: CategoriesModel = CategoriesModel.query.get_or_404(
            category_id, description = "category not found!")
        
    session.delete(query_category)
    session.commit()
        
    return "", HTTPStatus.NO_CONTENT

def get_all_categories():

    categories = CategoriesModel.query.all()
    categories_list = list()

    for category in categories:
        categories_list.append(
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "tasks": category.tasks
            }
        )
    return jsonify(categories_list), HTTPStatus.OK