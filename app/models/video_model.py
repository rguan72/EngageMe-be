from . import db

class Video(object):
    ref = db.collection("video")
    def __init__(self, url, name, length, average_intervals):
        self.url = url
        self.name = name
        self.length = length
        self.average_intervals = average_intervals

    def commit(self):
        Video.ref.document().set(self.to_dict())

    @staticmethod
    def from_dict(source):
        average_intervals = []
        for interval in source["average_intervals"]:
            average_intervals.append(interval.split(","))
        return {
            "url": source["url"],
            "name": source["name"],
            "length": source["length"],
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
            "average_intervals": self.average_intervals
        }

    def __repr__(self):
        return f"URL: {self.url}\nName: {self.name}\nLength: {self.length}\nAverage Intervals: {self.average_intervals}"