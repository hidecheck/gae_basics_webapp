from flask_wtf import FlaskForm
from wtforms import StringField, validators


class MyForm(FlaskForm):
    message = StringField(
        'message',
        validators=[
            validators.required(),
            validators.length(max=10),
        ],
    )
