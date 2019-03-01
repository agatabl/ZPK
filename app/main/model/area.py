from .. import db


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    maps = db.relationship('Map', backref='area', lazy=True)
    starting_point_lat = db.Column(db.Float, nullable=False)
    starting_point_lon = db.Column(db.Float, nullable=False)
    radius = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Area({self.name})"
