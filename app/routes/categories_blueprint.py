from flask import Blueprint

from app.controllers import categories_controller

bp_categories = Blueprint("bp_categories", __name__, url_prefix="/categories")

bp_categories.post("")(categories_controller.create_category)
bp_categories.patch("/<int:category_id>")(categories_controller.update_category)
bp_categories.delete("/<int:category_id>")(categories_controller.delete_category)