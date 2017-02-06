from app import db

class Visit(db.Model):
    """
    Create a Student table
    """

    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    sid = db.Column(db.Integer, index=True)
    visitdate = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Visit by {} on {}>'.format(self.name, self.visitdate)
