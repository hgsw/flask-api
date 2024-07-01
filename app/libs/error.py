from werkzeug.exceptions import HTTPException
from flask import request, json


class APIException(HTTPException):
    code = 500
    msg = "Sorry, happend error"
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        # 重写HTTPException方法
        main_path = request.method + " " + self.get_url_no_param()
        body = dict(msg=self.msg, error_code=self.error_code, request=main_path)

        return json.dumps(body)

    def get_headers(self, environ=None):
        # 重写HTTPException方法
        return [("Content-Type", "application/json; charset=utf-8")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")

        return main_path[0]
