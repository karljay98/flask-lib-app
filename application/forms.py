from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LibraryForm(FlaskForm):
    name = StringField('Library name', validators=[DataRequired(), Length(max=100)])
    description = StringField('Library description', validators=[Length(max=200)])
    submit = SubmitField('Add library')


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired(), Length(max=100)])
    author = StringField('Author name',validators=[DataRequired(), Length(max=200)])
    genre = StringField('Book genre', validators=[Length(max=75)])
    library_name = StringField('library name',validators=[DataRequired(), Length(max=100)])

    submit = SubmitField("Add book")