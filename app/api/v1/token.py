from app.libs.redprint import Redprint
from app.validators.form import ClientForm, TokenForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed
from flask import current_app, jsonify
from datetime import datetime

token = Redprint("token")


@token.route("", methods=["POST"])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {ClientTypeEnum.USER_EMAIL: User.verify}
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)
    expiration = current_app.config["TOKEN_EXPIRATION"]
    token = generate_auth_token(identity["uid"], form.type.data, identity["scope"], expiration)

    return token


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """uid: 用户id
    ac_type: 客户端来源
    scope: 权限作用域"""
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)

    return s.dumps({"uid": uid, "type": ac_type.value, "scope": scope})


@token.route("/secret", methods=["POST"])
def get_token_info():
    """获取令牌信息"""
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg="token is expired", error_code=1003)
    except BadSignature:
        raise AuthFailed(msg="token is invalid", error_code=1002)

    r = {
        "scope": data[0]["scope"],
        "create_at": date_str(data[1]["iat"]),
        "expire_in": date_str(data[1]["exp"]),
        "uid": data[0]["uid"],
    }
    return jsonify(r)


def date_str(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
