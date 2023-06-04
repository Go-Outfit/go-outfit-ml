from flask import Flask
import internal.controller.recommend as controller


def initialize_routes(app: Flask):
    controller.init_routes(app)
