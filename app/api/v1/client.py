from app.libs.redprint import Redprint
from app.libs.enums import ClientTypeEnum
from flask import request
from app.validators.form import ClientForm
from app.validators.form import UserEmailForm
from app.models.user import User
from app.libs.error_code import ClientTypeError

api = Redprint("client")


@api.route("/register", methods=["POST"])
def register():
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多
    参数、校验、接收参数"""
    data = request.json
    form = ClientForm(data=data)
    form.validate_for_api()
    promise = {ClientTypeEnum.USER_EMAIL: __resgister_user_by_email}
    promise[form.type.data]()

    return "register success"


def __resgister_user_by_email():
    data = request.json
    form = UserEmailForm(data=data)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
