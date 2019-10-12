from . import db

class Interval:
    def __init__(self, url="", start=0, end=0, uuid=""):
        self.url = url
        self.start = start
        self.end = end
        self.uuid = uuid
        self.ref = db.collection("interval")

    def commit(self):
        self.ref.document().set(self.to_dict())

    @staticmethod
    def get_ref():
        return db.collection("interval")
    
    def to_dict(self):
        res = {}
        for field in ("url", "start", "end", "uuid"):
            res[field] = getattr(self, field)
        return res