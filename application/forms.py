from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class OwnerForm(FlaskForm):
    first_name = StringField('Owner first name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField('Owner last name', validators=[Length(30)])
    submit = SubmitField('Add owner')


class CarForm(FlaskForm):
    number_plate = StringField('number plate', validators=[DataRequired(), Length(7)])
    submit = SubmitField("Add car")