from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo,
    Email,
    ValidationError
)

from app.models.user import User


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, max=15)
        ]
    )
    password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            Length(min=6, max=15),
            EqualTo('password')
        ]
    )
    first_name = StringField(
        "First Name",
        validators=[DataRequired(), Length(min=2, max=55)]
    )
    last_name = StringField(
        "Last Name",
        validators=[DataRequired(), Length(min=2, max=55)]
    )
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.object(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use!")
