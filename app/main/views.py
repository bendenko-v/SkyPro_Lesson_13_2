from flask import Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def page_index():
    return "<h2>Main page</h2>"
