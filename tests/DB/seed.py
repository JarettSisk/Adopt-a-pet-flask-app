import sys
sys.path.append('../../')

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

name = db.Column(db.String(20), nullable=False)
species = db.Column(db.String, nullable=False)
photo_url = db.Column(db.String, nullable=True)
age = db.Column(db.Integer, nullable=True)
notes = db.Column(db.String, nullable=True)
available = db.Column(db.Boolean, nullable=False, default=True)

# Populate the pets table with some rows of data 
pet1 = Pet(name='miss kitty', species='Cat', photo_url='https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', age=5, notes='Likes to play', available=True)

pet2 = Pet(name='doggy dog', species='Dog', photo_url='https://images.unsplash.com/photo-1596492784531-6e6eb5ea9993?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', age=10, notes='Needs a bath', available=False)

db.session.add_all([pet1, pet2])
db.session.commit()