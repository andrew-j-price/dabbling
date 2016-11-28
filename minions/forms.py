from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class TrackerFormToInsert(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        return True


class TrackerFormToDelete(FlaskForm):
    uuid = StringField('ID', validators=[DataRequired()])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        return True
