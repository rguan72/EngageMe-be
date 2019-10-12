from flask import Blueprint, request, jsonify
from app.models.intervals import Interval
from google.cloud import exceptions

interval_api = Blueprint("interval_api", __name__)

@interval_api.route("/api/interval", methods=["POST"])
def create_interval():
    try:
        interval = Interval(**request.json)
    except Exception as e:
        print(e)
        return "Bad request", 400
    interval.commit()
    return jsonify(interval.to_dict())

@interval_api.route("/api/interval", methods=["GET"])
def get_all_intervals():
    try:
        doc_ref = Interval.get_ref()
        res = []
        for interval in doc_ref.get():
            res.append(interval.to_dict())
        return jsonify(res)
    except Exception as e:
        print(e)
        return "Url not found", 404
