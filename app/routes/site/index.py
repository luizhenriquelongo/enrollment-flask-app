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


index_bp = Blueprint(
    'index_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route('/')
@index_bp.route('/index')
def index():
    return render_template('index.html', index=True)
