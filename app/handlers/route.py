from flask import Blueprint, render_template


route_api = Blueprint('route', __name__)

@route_api.route('/ping', methods=['GET'])
def pong():
    return 'PONG.'

@route_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')
