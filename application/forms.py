from flask_wtf import FlaksForm
from wtforms import StringField, SubmitField
from wtform.validator import DataRequired


class LibraryForm(FlaskForm):
    name = StringField('Library name', validators=[DataRequired(), length(max=100)])
    description = StringField('Library description', validators=[length(200)])
    submit = SubmitField('Add library')


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired(), length(100)])
    author = StringFiel('Author name',validators=[DataRequired(), length(200)])
    genre = StringField('Book genre', validators=[length(75)])
    submit = SubmitField("Add book")