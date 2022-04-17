from application import db 

# Library table

class Library(db.Model):
    __tablename__ = 'library'
    id = db.Column(db.Integer, primary_key=True) # library_id is the primary key and a integer value
    name = db.Column(db.String(100), nullable=False) # The name of library must be filled
    description = db.Column(db.String(200), nullable=True)
    books = db.relationship('Book', backref='library')
    
class Book(db.Model):
    __tablename__= 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(200), nullable = False)
    genre = db.Column(db.String(75), nullable = True)
    library_id = db.Column(db.Integer, db.ForeignKey('library_id'), nullable=False)
