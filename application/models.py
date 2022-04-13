from application import db 

# Library table

class Library(db.model):
    id = db.column(db.Integer, primary_key=True) # library_id is the primary key and a integer value
    name = db.column(db.string(100), nullable=False) # The name of library must be filled
    description = db.column(db.string(200))
    books = db.relationship(“Books”. Backreef=”library”)
    
class Book(db.model):
    book_id = db.column(db.integer, primary_kay=True)
    title = db.column(db.string(100), nullable=False)
    author = db.column(db.string(200))
    genre = db.column(db.string(75))
    library_id = db.column(db.integer, db.foreignkey(“library_id”))
