from wtforms import Form
from app.libs.error_code import ParameterException

class BaseForm(Form):
    """使用是自定义的BaseForm进行参数校验"""

    def __init__(self, data):
        # data需要校验的参数
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
