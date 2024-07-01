"""标准的REST风格中url不应该包含动词
url是用来定位资源，仅需要对资源进行描述即可

内部开发的api，
对外开放的api，围绕某一个资源进行增删改查（只提供数据，而不提供具体业务逻辑）
"""


class APIException:
    code = 500
    msg = "Sorry, error"
    error_code = 999

    def __init__(self, msg=None):
        print("APIException init ...")

    def error_400(self):
        pass


class ClientTypeError(APIException):
    code = 400
    msg = "client is invalid"
    error_code = 1006


# client_error = ClientTypeError()
# print(client_error.msg)  # Sorry, error


client_error = ClientTypeError()
print(client_error.msg)
# APIException init ...
# client is invalid
