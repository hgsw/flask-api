from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = -1


class ServerError(APIException):
    code = 500
    msg = "Sorry, we made a mistake"
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = "Client is invalid"
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = "Invalid parameter"
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = "The resource not found"
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = "Authorization failed"
    error_code = 1005
