from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.widgets import TextArea


class TestForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.something.choices = [
            (0, "Zero"),
            (1, "One"),
            (2, "Two"),
        ]

    id = StringField("ID")
    name = StringField("Name")
    something = SelectField("Something")
    created = DateTimeLocalField("Created", format='%Y-%m-%dT%H:%M')
    submit = SubmitField("Submit")
    delete = SubmitField("Delete")
