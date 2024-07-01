from collections.abc import Sequence
from typing import Any, Mapping
from wtforms import Form, StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, length
from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), Length(6, 32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(form, value):
        try:
            # 无异常即实现了数字向枚举类型转换
            client = ClientTypeEnum(value.data)
        except:
            raise ValidationError("注册方式不正确")
        
        form.type.data = client


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
            raise ValidationError()
