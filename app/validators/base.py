from collections.abc import Sequence
from typing import Any, Mapping
from wtforms import Form, StringField, IntegerField, ValidationError


class BaseForm(Form):
    def __init__(self, data):
        super(BaseForm, self).__init__(data=data)

    def validate(self):
        pass

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            pass
