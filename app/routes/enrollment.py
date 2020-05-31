from flask import (
    render_template,
    request,
    json,
    Response,
    redirect,
    url_for,
    flash,
    Blueprint
)

enrollment_bp = Blueprint(
    'enrollment_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@enrollment_bp.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template(
        'enrollment.html',
        enrollment=True,
        data={
            "id": id,
            "title": title,
            "term": term
        }
    )
