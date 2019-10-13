from flask import Blueprint

route_api = Blueprint('route', __name__)


@route_api.route("/ping", methods=["GET"])
def pong():
    return "PONG."


@route_api.route("/", methods=["GET"])
def index():
    return "hi"
