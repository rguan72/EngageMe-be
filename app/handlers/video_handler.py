from flask import Blueprint, jsonify, request
from app.models.video_model import Video
import google.cloud.exceptions


video_api = Blueprint("video", __name__)


@video_api.route("/ping", methods=["GET"])
def pong():
    return "PONG."


@video_api.route("/api/video/all", methods=["GET"])
def get_all_video():
    try:
        doc_ref = Video.get_ref()
        res = []
        for vid in doc_ref.stream():
            res.append(vid.to_dict())
        return jsonify(res)
    except Exception as e:
        print(e)
        return e, 500


@video_api.route("/api/video", methods=["GET"])
def get_video():
    try:
        video_url = request.args["url"]
    except KeyError:
        return "Need to include url query parameter", 400
    try:
        doc = next(Video.get_ref().where("url", "==", video_url).stream())
        video = Video.from_dict(doc.to_dict())
    except StopIteration:
        video = {}
    except Exception as e:
        print(e)
        return e, 500
    return jsonify(video)
