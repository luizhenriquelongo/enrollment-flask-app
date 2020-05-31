from app.database import db

from app.models.user import User
from app.models.course import Course


class Enrollment(db.Document):
    user_id = db.IntField()
    courseID = db.StringField(max_length=10)
