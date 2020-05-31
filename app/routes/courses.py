from flask import (
    render_template,
    Blueprint
)


courses_bp = Blueprint(
    'courses_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@courses_bp.route('/courses')
@courses_bp.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template(
        'courses.html',
        courses_data='',
        courses=True,
        term=term
    )
