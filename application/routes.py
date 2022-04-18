from application import app, db
from application.forms import LibraryForm, BookForm
from application.models import Library, Book
from flask import render_template, request, redirect, url_for


@app.route('/index')
def index():
    all_librarys = Library.query.all()
    return render_template('index.html', all_librarys=all_librarys)

@app.route('/libraries', methods = ['GET', 'POST'])
def libraries():
    form = LibraryForm()

    if request.method == "POST":
        library = Library(name= form.name.data, description= form.description.data)
        db.session.add(library)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('libraries.html', form = form)

@app.route('/books', methods= ['GET', 'POST'])
def books():
    form = BookForm()

    if request.method == "POST":
        book= Book(title= form.title.data, author= form.author.data, genre= form.genre.data, library_name= form.library_name.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('shelf'))
    
    return render_template('books.html', form = form)



