from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LibraryForm(FlaskForm):
    name = StringField('Library name', validators=[DataRequired(), Length(max=100)])
    description = StringField('Library description', validators=[Length(200)])
    submit = SubmitField('Add library')


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired(), Length(100)])
    author = StringField('Author name',validators=[DataRequired(), Length(200)])
    genre = StringField('Book genre', validators=[Length(75)])
    submit = SubmitField("Add book")