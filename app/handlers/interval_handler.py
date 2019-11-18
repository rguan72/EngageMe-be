from flask import Blueprint, request, jsonify
from app.models.interval_model import Interval
from app.models.video_model import Video
from app.utils.update import average_interval_update

interval_api = Blueprint("interval_api", __name__)


@interval_api.route("/api/interval", methods=["POST"])
def create_interval():
    uuid = request.json["uuid"]
    url = request.json["url"]
    name = request.json["name"]
    length = request.json["length"]
    new_video = False

    try:
        video_ref = next(Video.get_ref().where("url", "==", request.json["url"]).stream())
        length = video_ref.to_dict()["length"]
    except StopIteration:
        new_video = True

    intervals = []
    for start, end in request.json["intervals"]:
        if 0 <= start < length and 0 <= end < length and start <= end:
            intervals.append(Interval(url=url, uuid=uuid, start=start, end=end))
        else:
            return "Start or end time greater than length", 400

    for interval in intervals:
        interval.commit()

    if new_video:
        print(request.json)
        vid = Video(url=url, name=name, length=length)
        video_id = vid.commit()
    else:
        video_id = video_ref.id
        old_views = video_ref.to_dict()["views"]
        Video.get_ref().document(video_id).update({ "views": old_views + 1 }) 

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
