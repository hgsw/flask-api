from app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config["DEBUG"]:
            return APIException()
        else:
            raise e


if __name__ == "__main__":

    app.run(debug=True)
