from app.libs.redprint import Redprint
from app.libs.enums import ClientTypeEnum
from flask import request
from app.validators.form import ClientForm
from app.validators.form import UserEmailForm, UserIphoneForm
from app.models.user import User
from app.libs.error_code import Success

api = Redprint("client")


@api.route("/register", methods=["POST"])
def register():
    """不要将user局限成人，三方、APP、小程序、用户等，因此注册的形式非常多
    参数、校验、接收参数"""
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __resgister_user_by_email,
        ClientTypeEnum.USER_MOBILE: __resgister_user_by_iphone,
    }
    promise[form.type.data]()

    return Success()


def __resgister_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


def __resgister_user_by_iphone():
    form = UserIphoneForm().validate_for_api()
    User.register_by_iphone(form.nickname.data, form.account.data, form.secret.data)
