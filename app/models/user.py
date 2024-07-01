from sqlalchemy import Column, Integer, String, SmallInteger, Float, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models.base import Base
from app.models.base import db


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column("password", String(256))

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
