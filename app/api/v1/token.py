from app.libs.redprint import Redprint
from app.validators.form import ClientForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


token = Redprint("token")


@token.route("", methods=["POST"])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {ClientTypeEnum.USER_EMAIL: User.verify}
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)
    expiration = current_app.config["TOKEN_EXPIRATION"]
    token = generate_auth_token(identity["uid"], form.type.data, identity["is_admin"], expiration)

    return token


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """uid: 用户id
    ac_type: 客户端来源
    scope: 权限作用域"""
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)

    return s.dumps({"uid": uid, "type": ac_type.value, "is_admin": scope})
