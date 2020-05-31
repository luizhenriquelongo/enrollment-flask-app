from app.database import db

from .user import User
from .course import Course


class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField(max_length=10)
