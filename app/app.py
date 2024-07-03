from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import date

# 将user和book两个蓝图文件注册flask的蓝图中
# def register_blueprints(app):
#     from app.api.v1.user import user
#     from app.api.v1.book import book

#     app.register_blueprint(user)
#     app.register_blueprint(book)


# 重写flask的JSONEncoder的default方法
class JSONEncoder(_JSONEncoder):
    """default函数是递归调用的，o里面还有对象也会调用default函数"""

    def default(self, o):
        # r = o.__dict__ # 只能获取实例变量组成的字典
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")

        raise ServerError()


# 重写flask对象的json_encoder的方式，采用自定义的JSONEncoder
class Flask(_Flask):
    json_encoder = JSONEncoder


