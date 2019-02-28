from db import db
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    primary_email = db.Column(db.String, unique=True)
    secondary_email = db.Column(db.String)
    primary_phone = db.Column(db.Integer, unique=True)
    secondary_phone = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    full_address = db.Column(db.String)


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String)
    designation = db.Column(db.String)
    city = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    type = db.Column(db.String)
    role_description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('experiences'))

    @hybrid_property
    def duration(self):
        duration = (self.end_date - self.start_date).days
        years = duration // 365
        months = (duration % 365) // 30
        days = duration % 30
        return "{0} Years {1} months {2} days".format(years, months, days)
