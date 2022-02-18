from operator import ne
from flask import request,jsonify,current_app, session
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.exc.invalid_keys import InvalidTasksKeys, InvalidValues
from app.models.tasks_model import TasksModel
from app.models.eisenhowers_model import EisenhowerModel
from app.services.task_services import match_priority, check_categories

def create_taks():
    session = current_app.db.session
    data = request.get_json()

    try:
        categories = data.pop("categories")

        new_task = TasksModel(**data)

        eisenhower_category = match_priority(new_task.importance, new_task.urgency)
        eisenhower_type: EisenhowerModel = EisenhowerModel.query.filter_by(type=eisenhower_category).one()
        new_task.eisenhower_id = eisenhower_type.id
        
        check_categories(data=categories, task=new_task)
        categories_list = [category.name for category in new_task.categories]

        session.add(new_task)
        session.commit()
        
        final_response = {
            "id": new_task.id,
            "name": new_task.name,
            "description": new_task.description,
            "duration": new_task.duration,
            "classification": eisenhower_type.type,
            "categories": categories_list
        }

        return jsonify(final_response), HTTPStatus.CREATED
    
    except InvalidValues as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    
    except IntegrityError:
        return jsonify({"msg": "task already exists!"}), HTTPStatus.CONFLICT

    except TypeError:
        error = InvalidTasksKeys(data)
        return jsonify(error.message), HTTPStatus.BAD_REQUEST

def update_task(task_id: int):
    session = current_app.db.session

    try:
        query_task: TasksModel = TasksModel.query.get_or_404(
            task_id, description = "task not found!")
        
        data = request.get_json()
        categories = data.pop("categories")

        for key, value in data.items():
            setattr(query_task, key, value)
        
        eisenhower_category = match_priority(query_task.importance, query_task.urgency)
        eisenhower_type: EisenhowerModel = EisenhowerModel.query.filter_by(type=eisenhower_category).one()
        
        setattr(query_task, "eisenhower_id", eisenhower_type.id)

        session.add(query_task)
        session.commit()

        check_categories(data=categories, task=query_task)
        categories_list = [category.name for category in query_task.categories]

        final_response = {
            "id": query_task.id,
            "name": query_task.name,
            "description": query_task.description,
            "duration": query_task.duration,
            "classification": eisenhower_type.type,
            "categories": categories_list
        }

        return jsonify(final_response), HTTPStatus.OK
    
    except InvalidValues as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST

def delete_task(task_id:int):
    session = current_app.db.session

    query_task: TasksModel = TasksModel.query.get_or_404(
            task_id, description = "task not found!")
        
    session.delete(query_task)
    session.commit()

    return "", HTTPStatus.NO_CONTENT