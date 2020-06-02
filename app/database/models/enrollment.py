from app.database.config import db


class Enrollment(db.Document):
    user_id = db.IntField()
    courseID = db.StringField(max_length=10)
