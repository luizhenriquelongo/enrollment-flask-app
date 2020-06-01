from flask import (
    render_template,
    Blueprint
)

from app.models.course import Course

courses_bp = Blueprint(
    'courses_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@courses_bp.route('/courses')
@courses_bp.route('/courses/<term>')
def courses(term="Spring 2019"):
    classes = Course.objects.order_by('courseID')
    return render_template(
        'courses.html',
        courses_data=classes,
        courses=True,
        term=term
    )
