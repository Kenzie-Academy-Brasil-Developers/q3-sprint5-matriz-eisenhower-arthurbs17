from flask import Blueprint
from app.routes.categories_blueprint import bp_categories

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_categories)