from flask import Flask, request, jsonify
import pkg.response.base as response
import flask_expects_json as validator
import http
from internal.model.model import RecommenderRequestBody
from werkzeug.exceptions import BadRequest


def ping():
    return response.success_response("pong")


@validator.expects_json(RecommenderRequestBody)
def recommend():
    data = request.json
    print(data)
    return response.success_response("recommend")


def handle_bad_request(e: BadRequest):
    error = {
        "code": e.code,
        "name": e.name,
        "description": e.description.message
    }
    return response.error_response(error, http.HTTPStatus.BAD_REQUEST), 400


def init_routes(app: Flask):
    app.route("/ping", methods=['GET', 'POST',
              'PUT', 'PATCH', 'DELETE', 'OPTIONS'])(ping)
    app.register_error_handler(400, handle_bad_request)
    app.route("/recommend", methods=["POST"])(recommend)
