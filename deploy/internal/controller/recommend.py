from flask import Flask, request, jsonify
import pkg.response.base as response
import flask_expects_json as validator
import http
from internal.model.model import RecommenderRequestBody
from werkzeug.exceptions import BadRequest
import pkg.config.config as config
import internal.service.recommend as recommendation_service


def ping():
    return response.success_response("pong")


dataset = config.load_csv_data()


@validator.expects_json(RecommenderRequestBody)
def recommend():
    req = request.json
    # data = request.get_data
    res = recommendation_service.OutfitRecommender(
        req["gender"], req["weather"], req["situation"], req["fashion_style"], dataset=dataset)
    res = res.recommend()
    return response.success_response(res)


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
