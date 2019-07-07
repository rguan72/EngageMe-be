from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def to_json(self):
        res = {}
        for field in ('id', 'name'):
            res[field] = getattr(self, field)
        return res

    def __repr__(self):
        return f'User {self.name}'
