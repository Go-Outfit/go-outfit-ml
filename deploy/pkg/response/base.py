from flask import jsonify
import http


class BaseResponse:
    def __init__(self, code, message, errors, data):
        self.code = code
        self.message = message
        self.errors = errors
        self.data = data

    def json(self):
        return jsonify({"code": self.code, "message": self.message, "errors": self.errors, "data": self.data})


response_message = {
    "success": http.HTTPStatus.OK,
    "bad_request": http.HTTPStatus.BAD_REQUEST,
    "internal_server_error": http.HTTPStatus.INTERNAL_SERVER_ERROR
}


def success_response(data):
    return BaseResponse(200, response_message["success"].phrase, None, data).json()
