class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    cars = db.relationship('Car', backref='ownerbr')

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(7), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)