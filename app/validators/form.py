from collections.abc import Sequence
from typing import Any, Mapping
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, length
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    # message="不允许为空" 自定义错误
    account = StringField(validators=[DataRequired(message="不允许为空"), Length(6, 32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            # 无异常即实现了数字向枚举类型转换
            client = ClientTypeEnum(value.data)
        except:
            raise ValidationError("注册方式不正确")

        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message="invalidate email")])
    secret = StringField(
        validators=[
            DataRequired(),
            # password can only include letters , numbers and "_"
            Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$"),
        ]
    )
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("该邮箱已注册")


class UserIphoneForm(ClientForm):
    account = StringField(validators=[Regexp("^1[35789]\d{9}$", message="手机号格式不正确")])
    secret = StringField(
        validators=[
            DataRequired(),
            Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$"),
        ]
    )
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        # User模型数据库应该有iphone字段，这里就用email代替了
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("该手机号已注册")


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])
