from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    Blueprint
)

from app.database.models import Enrollment
from app.database.helpers import MongoDAO


enrollment_bp = Blueprint('enrollment_bp', __name__)


@enrollment_bp.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    if not session.get('username'):
        return redirect(url_for('login_bp.login'))
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get('user_id')

    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"Oops! You are already registered in this course \
                  {courseTitle}!",
                  "danger")
            return redirect(url_for('courses_bp.courses'))

        Enrollment(user_id=user_id, courseID=courseID).save()
        flash(f"You are enrolled in {courseTitle}!", "success")

    classes = MongoDAO.get_all_enrolled_classes(user_id)

    return render_template(
        'enrollment.html',
        title="Enrollment",
        enrollment=True,
        classes=classes
    )
