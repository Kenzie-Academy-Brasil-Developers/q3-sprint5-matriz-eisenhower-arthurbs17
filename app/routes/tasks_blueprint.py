from flask import Blueprint

from app.controllers import tasks_controller

bp_tasks = Blueprint("bp_tasks", __name__, url_prefix="/tasks")

bp_tasks.post("")(tasks_controller.create_taks)
bp_tasks.patch("/<int:task_id>")(tasks_controller.update_task)
bp_tasks.delete("/<int:task_id>")(tasks_controller.delete_task)