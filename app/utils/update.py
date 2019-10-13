from app.models.interval_model import Interval
from app.models import db
from datetime import datetime

CUTOFF = .5
MIN_LENGTH = 1


def average_interval_update(video_id):
    video = db.collection("video").document(video_id).get()
    url = video.to_dict()["url"]
    length = int(video.to_dict()["length"])
    cumulative = [0 for _ in range(length)]
    num_users = 0
    for interval in db.collection("interval").where("url", "==", url).stream():
        start_time = int(interval.to_dict()["start"])
        end_time = int(interval.to_dict()["end"])
        for i in range(start_time, end_time + 1):
            cumulative[i] += 1
        num_users += 1
    intervals = []
    start = 0
    end = 0
    while end < len(cumulative):
        if (cumulative[end] / num_users) > CUTOFF:
            end += 1
        else:
            if (end - start) > MIN_LENGTH:
                intervals.append(f"{start},{end}")
            end += 1
            start = end

    if start < end:
        intervals.append(f"{start},{end-1}")
    db.collection("video").document(video.id).update({ "average_intervals": intervals })
    return cumulative
