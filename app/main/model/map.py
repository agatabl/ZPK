from .. import db


class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    map_file = db.Column(db.Text)
    trails = db.relationship('Trail', backref='map', lazy=True)
    border_N = db.Column(db.Float)
    border_S = db.Column(db.Float)
    border_E = db.Column(db.Float)
    border_W = db.Column(db.Float)

    def __repr__(self):
        return f"Map({self.name})"
