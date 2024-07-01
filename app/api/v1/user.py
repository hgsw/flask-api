from flask import Blueprint
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
# user = Blueprint("user", __name__)
api = Redprint("user")


@api.route("/get_user")
@auth.login_required
def get_user():
    # token 验证是否过期 是否合法
    return "hello get_user"


@api.route("/create")
def create_user(self):
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多"""
    pass
