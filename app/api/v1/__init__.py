from flask import Blueprint
from app.libs.redprint import Redprint
from app.api.v1 import user, book, client, token


def create_buleprint_v1():
    # from app.api.v1.book import api as book
    # from app.api.v1.user import api as user
    bp_v1 = Blueprint("v1", __name__)

    # 将自定义的红图注册到蓝图上，同时增加每个视图文件自己的url前缀
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.token.register(bp_v1)

    return bp_v1
