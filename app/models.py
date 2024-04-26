from app import db


class Verb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String(80), unique=True, nullable=False)
    conjugations = db.Column(db.PickleType)

    def __repr__(self):
        return f'<Verb {self.infinitive}>'

