from flask import Blueprint

library_bp = Blueprint("library", __name__)


@library_bp.route("/books", methods=["GET"])
def get_books():
    return "Here be books!"
