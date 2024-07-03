from flask import Blueprint, jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User


class UserTest:
    """调用类的__dict__函数，类变量不会被转化为dict
    必须是实例变量__dict__才会将变量转化dict"""

    name = "hou"
    age = 18

    def __init__(self):
        self.nickname = "user1"

    def keys(self):
        # 通过dict(self)返回对象构建字典的key
        return ("name", "age", "nickname")

    def __getitem__(self, item):
        # 根据item获取对象的值
        return getattr(self, item)


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

    #! 测试对象序列化代码
    return jsonify(UserTest())
    # return jsonify(user)


@api.route("/create")
def create_user(self):
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多"""
    pass
