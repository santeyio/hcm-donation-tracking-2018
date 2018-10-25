from flask import Flask, request, jsonify, make_response, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

#############################
###### Serve Application
#############################

@app.route('/')
def index():
    return render_template("index.html")

#############################
###### API
#############################

@app.route('/api/user', methods=['POST'])
def user(user_id=None):
    save_donor(request)
    emit_donation_update(request)
    return jsonify({'status': 'success'})

@app.route('/api/donations', methods=['GET'])
def donationis():
    return_array = get_all_donations()
    return jsonify(return_array)

#############################
###### Models
#############################

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, default="")
    last_name = db.Column(db.String, default="")
    email = db.Column(db.String, default="")
    payment_method = db.Column(db.String, default="")
    one_time_amount = db.Column(db.Integer, default=0)
    monthly_amount = db.Column(db.Integer, default=0)

#############################
###### Utils
#############################

def emit_donation_update(request):
    jparse = request.get_json()
    donation_update = {
            'one_time_amount': jparse.get('one_time_amount'),
            'monthly_amount': jparse.get('monthly_amount'),
            'displayed': False}
    print('emitting donation_update: ')
    print(donation_update)
    socketio.emit('donations', donation_update)

def save_donor(request):
    jparse = request.get_json()
    new_donor = Donor(
            first_name = jparse.get('first_name'),
            last_name = jparse.get('last_name'),
            email =  jparse.get('payment_method'),
            one_time_amount = jparse.get('one_time_amount'),
            monthly_amount = jparse.get('monthly_amount'))
    db.session.add(new_donor)
    db.session.commit()
    print(new_donor.id)

def get_all_donations():
    donors = Donor.query.all()
    return_array = []
    for donor in donors:
        return_array.append({
            'monthly_amount': donor.monthly_amount, 
            'one_time_amount': donor.one_time_amount,
            'displayed': False})
    return return_array

def create_db():
    """ Helper to create a local test database """
    new_app = Flask(__name__)
    new_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
    new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(new_app)
    db.create_all(app=new_app)
