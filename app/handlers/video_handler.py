from flask import Blueprint, request, jsonify
from app.models import db
from app.models.video_model import Video
import google.cloud.exceptions


video_api = Blueprint("video", __name__)


@video_api.route("/ping", methods=["GET"])
def pong():
    return "PONG."


@video_api.route("/api/video", methods=["GET"])
def index():
    url = request.args.get("url")
    if not url:
        return "Error 404: No url specified", 404

    doc_ref = db.collection("video").document(url)
    try:
        doc = doc_ref.get()
        video = Video.from_dict(doc.to_dict())
        print(f"Video: {video}")
    except google.cloud.exceptions.NotFound:
        video = {}
        print(f"No document found for: {url}")
    return jsonify(video)
