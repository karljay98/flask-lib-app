from application import app, db
from application.forms import LibraryForm, BookForm
from application.models import Library, Book
from flask import render_template, request, redirect, url_for

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = LibraryForm()
    return render_template('index.html', form = form)
