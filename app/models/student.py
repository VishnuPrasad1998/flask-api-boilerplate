from app.db import db

class StudentModel(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    course = db.Column(db.String(80))

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

