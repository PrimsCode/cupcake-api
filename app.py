from flask import Flask, jsonify, redirect, render_template, request
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SQLALCHEMY_ECHO']=True
app.config['SECRET_KEY']="DELIOUS"

connect_db(app)
db.create_all()

def serialize_cupcake(cupcake):
    """Serialize a cupcake SQLAlchemy obj to dictionary"""
    return {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image,
        'recipe': cupcake.recipe
    }

@app.route('/')
def index_page():
    """Show cupcake landing page"""

    return render_template('index.html')

# @app.route('/')
# def add_cupcake_form():
#     """Add a cupcake from form"""

#     new_cupcake = Cupcake(
#         flavor=request.form['flavor'],
#         size=request.form['size'],
#         rating=request.form['rating'],
#         image=request.form['image'],
#         recipe=request.form['recipe'],)
#     db.session.add(new_cupcake)
#     db.session.commit()

#     flash('Cupcake Added!')

#     return redirect('/')

@app.route('/cupcakes', methods=['GET'])
def get_all_cupcakes():
    """Return JSON for cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    """Return JSON for a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a new cupcake & return JSON"""

    new_cupcake = Cupcake(
        flavor=request.json['flavor'],
        size=request.json['size'],
        rating=request.json['rating'],
        image=request.json['image'],
        recipe=request.json['recipe'],)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)
    response_json = jsonify(cupcake=serialized)

    return (response_json, 201)

@app.route('/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Update a cupcake & return JSON"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    cupcake.recipe = request.json.get('recipe', cupcake.recipe)

    db.session.commit()

    serialized = serialize_cupcake(cupcake)
    response_json = jsonify(cupcake=serialized)

    return (response_json, 201)


@app.route('/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete cupcake from db"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")




