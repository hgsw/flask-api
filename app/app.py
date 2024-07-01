from flask import Flask

# 将user和book两个蓝图文件注册flask的蓝图中
# def register_blueprints(app):
#     from app.api.v1.user import user
#     from app.api.v1.book import book

#     app.register_blueprint(user)
#     app.register_blueprint(book)


# 自定义Redprint对象，先分别注册到蓝图对象中再注册到flask中
def register_blueprints(app):
    from app.api.v1 import create_buleprint_v1

    app.register_blueprint(create_buleprint_v1(), url_prefix="/v1")


def register_plugin(app):
    from app.models.base import db

    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    # 注册蓝图
    register_blueprints(app)
    # 注册数据库
    register_plugin(app)
    return app
