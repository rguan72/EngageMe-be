from flask import Blueprint, jsonify
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


@video_api.route("/api/video/<video_url>", methods=["GET"])
def get_video(video_url):
    try:
        doc = next(Video.get_ref().where("url", "==", video_url).stream())
        video = Video.from_dict(doc.to_dict())
    except StopIteration:
        video = {}
    except Exception as e:
        print(e)
        return e, 500
    return jsonify(video)
