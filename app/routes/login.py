from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    Blueprint
)

from app.forms.login import LoginForm
from app.models import User

login_bp = Blueprint(
    'login_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash_msg = f"{user.first_name}, you are successfully logged in!"
            flash(flash_msg, "success")
            return redirect(url_for('index_bp.index'))

        flash_msg = "Sorry, something went wrong."
        flash(flash_msg, "danger")

    return render_template('login.html', title="Login", form=form, login=True)
