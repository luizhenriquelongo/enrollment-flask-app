from flask import (
    render_template,
    request,
    json,
    Response,
    redirect,
    url_for,
    flash
)

from app import app
from app.models.user import User
from app.forms.login import LoginForm
from app.forms.register import RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', index=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You are successfully logged in!", "success")
        return redirect(url_for('index'))
    return render_template('login.html', title="Login", form=form, login=True)


@app.route('/courses')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template(
        'courses.html',
        courses_data='',
        courses=True,
        term=term
    )


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template(
        'register.html',
        title="Register",
        form=form,
        register=True
    )


@app.route('/enrollment', methods=['GET', 'POST'])
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


@app.route('/user')
def user():
    users = User.objects.all()
    return render_template("user.html", users=users)


@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
    if not idx:
        jdata = courses_data
    else:
        jdata = courses_data[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")
