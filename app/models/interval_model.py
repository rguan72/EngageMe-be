from . import db

class Interval:
    ref = db.collection("interval")

    def __init__(self, url="", start=0, end=0, uuid=""):
        self.url = url
        self.start = start
        self.end = end
        self.uuid = uuid

    def commit(self):
        Interval.ref.document().set(self.to_dict())

    @staticmethod
    def get_ref():
        return Interval.ref
    
    def to_dict(self):
        res = {}
        for field in ("url", "start", "end", "uuid"):
            res[field] = getattr(self, field)
        return res