from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    session,
    Blueprint,
)

from app.website.forms import LoginForm
from app.database.models import User


login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index_bp.index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash_msg = f"{user.first_name}, you are successfully logged in!"
            flash(flash_msg, "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect(url_for('index_bp.index'))

        flash_msg = "Sorry, something went wrong."
        flash(flash_msg, "danger")

    return render_template('login.html', title="Login", form=form, login=True)


@login_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)

    return redirect(url_for('index_bp.index'))
