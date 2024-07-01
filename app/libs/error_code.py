from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    msg = "client is invalid"
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1000
