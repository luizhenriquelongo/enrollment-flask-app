from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    Blueprint
)

from app.models import Enrollment
from app.models import User

enrollment_bp = Blueprint(
    'enrollment_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


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

    aggregation = [
        {
            '$lookup': {
                'from': 'enrollment', 
                'localField': 'user_id', 
                'foreignField': 'user_id', 
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1', 
                'includeArrayIndex': 'r1_id', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course', 
                'localField': 'r1.courseID', 
                'foreignField': 'courseID', 
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'user_id': user_id
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]
    classes = list(User.objects.aggregate(*aggregation))

    return render_template(
        'enrollment.html',
        title="Enrollment",
        enrollment=True,
        classes=classes
    )