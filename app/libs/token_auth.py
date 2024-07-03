from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed
from flask import current_app, g
from collections import namedtuple

auth = HTTPBasicAuth()
User = namedtuple("User", ["uid", "ac_type", "scope"])


@auth.verify_password
def verify_password(token, password):
    # 采用HTTPBasicAuth的方式处理账号和密码的方式，必须放在http的头部中
    # kay=Authorization value=basic base64(账号:密码)
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(token)
        # 异常发生就是token认证失败
    except SignatureExpired:
        raise AuthFailed(msg="Token is expired", error_code=1003)
    except BadSignature:
        raise AuthFailed(msg="Token is invalid", error_code=1002)

    uid = data["uid"]
    ac_type = data["type"]

    return User(uid, ac_type, "")
