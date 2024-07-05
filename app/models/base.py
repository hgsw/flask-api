from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger
from contextlib import contextmanager
from datetime import datetime
from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    """依赖方法的重载，在三方接口上增加'status'默认状态查询条件
    此时还需要将自定义的类替换原有的类"""

    def filter_by(self, **kwargs):
        # 父类方法重写，增加默认查询条件
        if not "status" in kwargs.keys():
            kwargs["status"] = 1

        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, description=None):
        # 父类方法重写，抛出自定义异常
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self, description=None):
        # 父类方法重写，抛出自定义异常
        rv = self.first()
        if rv is None:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):

    __abstract__ = True

    create_time = Column("create_time", Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        """动态对传入attrs_dict同名的属性进行复值
        hasattr(object, key)判断对象是否包含key这个属性"""
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        return None

    def __getitem__(self, item):
        # 获取指定对象传递item的值
        return getattr(self, item)

    def delete(self):
        """逻辑删除"""
        self.status = 0

    """修改模型返回的字段，需要在模型类的构造函数中加上@orm.reconstructor
    keys是返回的字段，hide是需要隐藏的字段，append是追加字段"""

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self
