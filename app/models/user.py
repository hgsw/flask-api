from sqlalchemy import Column, Integer, String, SmallInteger, Float, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models.base import Base
from app.models.base import db
from app.libs.error_code import NotFound, AuthFailed


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column("password", String(256))

    def keys(self):
        # 优雅的序列化指定变量
        return ["id", "email", "nickname"]

    def __getitem__(self, item):
        # 获取指定对象的值
        return getattr(self, item)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg="user not found")
        # 比对密码
        if not user.check_password(password):
            raise AuthFailed()

        return {"uid": user.id}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
