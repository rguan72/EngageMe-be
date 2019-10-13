from flask import Blueprint, request, jsonify
from app.models.interval_model import Interval
from app.models.video_model import Video
from app.utils.update import average_interval_update

interval_api = Blueprint("interval_api", __name__)


@interval_api.route("/api/interval", methods=["POST"])
def create_interval():
    uuid = request.json["uuid"]
    url = request.json["url"]
    for intvl in request.json["intervals"]:
        interval = Interval(url=url, uuid=uuid, start=intvl[0], end=intvl[1])
        interval.commit()

    try:
        video_id = next(Video.get_ref().where("url", "==", request.json["url"]).stream()).id
    except StopIteration:
        print(request.json)
        vid = Video(url=request.json["url"], name=request.json["name"], length=request.json["length"], average_intervals=request.json["intervals"])
        video_id = vid.commit()
    except Exception as e:
        print(e)
        return e, 400

    average_interval_update(video_id)
    return "", 200


@interval_api.route("/api/interval", methods=["GET"])
def get_all_intervals():
    try:
        doc_ref = Interval.get_ref()
        res = []
        for interval in doc_ref.stream():
            res.append(interval.to_dict())
        return jsonify(res)
    except Exception as e:
        print(e)
        return e, 500
