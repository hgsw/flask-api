from flask import Blueprint
from app.libs.redprint import Redprint

# user = Blueprint("user", __name__)
api = Redprint("user")


@api.route("/get_user")
def get_user():
    return "hello get_user"


@api.route("/create")
def create_user(self):
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多"""
    pass
