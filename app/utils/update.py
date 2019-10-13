from app.models.interval_model import Interval
from app.models import db
from datetime import datetime

CUTOFF = .2
MIN_LENGTH = 10


def average_interval_update(video_id):
    video_ref = db.collection("video").document(video_id).get()
    video = video_ref.to_dict()
    video_id = video_ref.id
    url = video["url"]
    views = video["views"]
    length = int(video["length"])
    cumulative = [0 for _ in range(length)]
    print("len(cumulative)", len(cumulative))
    for interval in db.collection("interval").where("url", "==", url).stream():
        start_time = int(interval.to_dict()["start"])
        end_time = int(interval.to_dict()["end"])
        print("end_time", end_time)
        for i in range(start_time, end_time + 1):
            cumulative[i] += 1
    intervals = []
    start = 0
    end = 0
    while end < len(cumulative):
        if (cumulative[end] / views) > CUTOFF:
            end += 1
        else:
            if (end - start) > MIN_LENGTH:
                intervals.append(f"{start},{end}")
            end += 1
            start = end

    if start < end:
        intervals.append(f"{start},{end-1}")
    db.collection("video").document(video_id).update({ "average_intervals": intervals })
    return cumulative
