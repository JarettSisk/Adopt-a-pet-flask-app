from flask_sqlalchemy import SQLAlchemy


# Set up db connection
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



# Database models
class Pet(db.Model):
    """Pet Model"""

    # Table setup
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=True, default='https://images.unsplash.com/photo-1623387641168-d9803ddd3f35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    # End table setup

    # Instance methods
    def __repr__(self):
        return f"name = {self.name}, age = {self.age}, available = {self.available}"

