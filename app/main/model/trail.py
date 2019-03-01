from .. import db


class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)
    file = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Map({self.name})"
