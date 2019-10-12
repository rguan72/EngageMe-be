from flask import Blueprint, render_template
from app.models import db


route_api = Blueprint('route', __name__)

@route_api.route("/ping", methods=["GET"])
def pong():
    return "PONG."

@route_api.route("/", methods=["GET"])
def index():
    doc_ref = db.collection(u"users").document(u"alovelace").set({"yo": "hi"})
    db.collection("users").document().set({"bro": "yo"})
    return "hi"
