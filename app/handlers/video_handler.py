from flask import Blueprint, request, jsonify
from app.models import db
from app.models.video_model import Video
import google.cloud.exceptions


video_api = Blueprint("video", __name__)


@video_api.route("/ping", methods=["GET"])
def pong():
    return "PONG."

@video_api.route("/api/video", methods=["GET"])
def get_all_intervals():
    try:
        doc_ref = Video.get_ref()
        res = []
        for vid in doc_ref.stream():
            res.append(vid.to_dict())
        return jsonify(res)
    except Exception as e:
        print(e)
        return e, 500
