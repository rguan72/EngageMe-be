from itertools import accumulate
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
    arr = [0 for _ in range(length + 1)]
    for interval in db.collection("interval").where("url", "==", url).stream():
        start_time = int(interval.to_dict()["start"])
        end_time = int(interval.to_dict()["end"])
        arr[start_time] += 1
        if end_time + 1 < len(arr):
            arr[end_time + 1] -= 1
    arr = list(accumulate(arr))
    intervals = []
    start = 0
    end = 0
    while end < len(arr):
        if (arr[end] / views) > CUTOFF:
            end += 1
        else:
            if (end - 1 - start) > MIN_LENGTH:
                intervals.append(f"{start},{end - 1}")
            end += 1
            start = end

    if start < end:
        intervals.append(f"{start},{end - 1}")
    db.collection("video").document(video_id).update({ "average_intervals": intervals })
    return arr
