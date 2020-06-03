from flask import (
    render_template,
    Blueprint
)

from app.database.models.user import User


user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user')
def user():
    users = User.objects.all()
    return render_template("user.html", users=users)
