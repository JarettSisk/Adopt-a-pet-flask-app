# Imports
from flask import Flask, request, render_template, redirect, flash, session, abort
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
# Debugging turned off
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MySecretKey123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)

# Routes
@app.route('/')
def home_redirect():
    return redirect('/pets')

@app.route('/pets')
def list_pets():
    PETS = Pet.query.all()

    return render_template('pets.html', pets=PETS)

@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, age=age, notes=notes)
        if form.photo_url.data != '':
            photo_url = form.photo_url.data
            new_pet.photo_url = photo_url
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/pets")

    else:
        return render_template(
            "add-pet.html", form=form)

@app.route('/pets/<pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    # Convert to int
    petid = int(pet_id)
    current_pet = Pet.query.get_or_404(petid)
    form = EditPetForm(obj=current_pet)

    if form.validate_on_submit():
        if form.photo_url.data != '':
            current_pet.photo_url = form.photo_url.data
        current_pet.notes = form.notes.data
        current_pet.available = form.available.data
        db.session.commit()
        return redirect(f"/pets")

    else:
        return render_template(
            "pet.html", form=form, pet=current_pet)

@app.route('/pets/<pet_id>/delete')
def delete_pet(pet_id):
    petid = int(pet_id)

    # Deleting the pet
    current_pet = Pet.query.get_or_404(petid)
    db.session.delete(current_pet)
    db.session.commit()
    return redirect('/pets')


