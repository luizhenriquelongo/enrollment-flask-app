from flask import (
    Blueprint,
    render_template,
    flash,
    url_for,
    redirect,
)

from app.forms import RegisterForm
from app.models import User

register_bp = Blueprint(
    'register_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_data = {
            'user_id': User.objects.count() + 1,
            'email': form.email.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data
        }

        user = User(**user_data)
        user.set_password(form.password.data)
        user.save()
        flash('You are successfully registered!', 'success')
        return redirect(url_for('index_bp.index'))

    return render_template(
        'register.html',
        title="Register",
        form=form,
        register=True
    )
