from datetime import datetime
from . import db

class Interval:
    ref = db.collection("interval")

    def __init__(self, url="", start=0, end=0, uuid=""):
        self.url = url
        self.start = start
        self.end = end
        self.uuid = uuid
        self.created = datetime.now()
        self.updated = datetime.now()

    def commit(self):
        self.updated = datetime.now()
        Interval.ref.document().set(self.to_dict())

    @staticmethod
    def get_ref():
        return Interval.ref
    
    def to_dict(self):
        return {
            "url": self.url,
            "start": self.start,
            "end": self.end,
            "uuid": self.uuid,
            "created": self.created,
            "updated": self.updated
        }