from flask import Blueprint
from app.libs.redprint import Redprint

# book = Blueprint("book", __name__)
api = Redprint("book")


# @api.route("/get")
@api.route("", methods=["GET"])
def get_book():
    return "hello get_book"
