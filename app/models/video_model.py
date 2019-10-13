from . import db


class Video(object):
    ref = db.collection("video")

    def __init__(self, url, name, length, average_intervals):
        self.url = url
        self.name = name
        self.length = length
        self.average_intervals = []
        self.views = 1
        for interval in average_intervals:
            self.average_intervals.append(f"{interval[0]},{interval[1]}")

    def commit(self):
        id_ = Video.ref.document().id
        Video.ref.document(id_).set(self.to_dict())
        return id_

    @staticmethod
    def from_dict(source):
        average_intervals = []
        for interval in source["average_intervals"]:
            average_intervals.append(interval.split(","))
        return {
            "url": source["url"],
            "name": source["name"],
            "length": source["length"],
            "views": source["views"],
            "average_intervals": average_intervals
        }

    @staticmethod
    def get_ref():
        return Video.ref

    def to_dict(self):
        return {
            "url": self.url,
            "name": self.name,
            "length": self.length,
            "views": self.views,
            "average_intervals": self.average_intervals
        }

    def __repr__(self):
        return f"URL: {self.url}\nName: {self.name}\nLength: {self.length}\nAverage Intervals: {self.average_intervals}"