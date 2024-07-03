from flask import Blueprint, jsonify, g
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User
from app.models.base import db
from app.libs.error_code import DeleteSuccess


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


@api.route("", methods=["DELETE"])
@auth.login_required
def delete_user():
    # 超权限（用户可以访问改接口是否拥有删除的操作）
    # 用户1、2， 用户1token验证通过后，携带uid=2，就有可能删除用户2
    # 不应该由用户传递uid删除用户，解决是从token中读取
    # 在验证token的时候，use信息已存在g变量中，g变量是线程隔离的
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()

    return DeleteSuccess()


@api.route("/create")
def create_user(self):
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多"""
    pass
