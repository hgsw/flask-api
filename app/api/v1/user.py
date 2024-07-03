from flask import Blueprint, jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User


# user = Blueprint("user", __name__)
api = Redprint("user")


@api.route("/<int:uid>", methods=["GET"])
@auth.login_required
def get_user(uid):
    # token 验证是否过期 是否合法
    user = User.query.get_or_404(uid)
    # 当然可以，但是不够优雅
    # r = {"nickname": user.nickname, "email": user.email}
    # return jsonify(r)

    return jsonify(user)


@api.route("/create")
def create_user(self):
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多"""
    pass
