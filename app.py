import os
from flask import Flask, render_template, request, redirect,url_for, flash
from flask import session as ssn
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import requests
import json

if os.path.exists("env.py"):
    import env

# Send email invites to users to join a pot
from sendInvites import sendInvites

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moneypot.db'
app.secret_key = os.environ.get("SECRET_KEY")
# Initialize database
db = SQLAlchemy(app)

# Association table for users and pots
user_pots = db.Table('user_pots', 
    db.Column('user_id', db.Integer, db.ForeignKey('Users.id')),
    db.Column('pot_id', db.Integer, db.ForeignKey('pots.id'))
    )


# Create db model for users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    joined_pots = db.Column(db.Integer, db.ForeignKey('pots.id'))
    # String to return name when something is added to database
    def __repr__(self):
        return '<Name %r>' % self.id


# Create db model for potss table
class Pots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    cycle = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    isPrivate = db.Column(db.Boolean, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    participants = db.Column(db.JSON())
    # String to return name when something is added to database
    def __repr__(self):
        return '<Name %r>' % self.id

# exchange rates api API 
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=1896b2be48dacf88b405e92f6d2136fe&symbols=USD,GBP,AUD,CAD'
response = requests.get(url)
exchange_data = response.json()

# api call example result:
# {'success': True, 'timestamp': 1674413344, 'base': 'EUR', 'date': '2023-01-22', 'rates': {'USD': 1.087725, 'GBP': 0.877976, 'AUD': 1.560825, 'CAD': 1.456436}}



@app.route("/")
def home():
    """ the main view of the app """
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():

    pots = Pots.query
    public_pots = pots.filter_by(isPrivate=False)
    private_pots = pots.filter_by(isPrivate=True)

    # Get the current user logged in
    logged_user = ""
    if "user" in ssn:
        logged_user = ssn["user"]
    else:
        return render_template('dashboard.html', pots=public_pots, private_pots=private_pots)

    return render_template('dashboard.html', user=logged_user, pots=public_pots, private_pots=private_pots)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ Sign up page """
    duplicateUser = None
    if request.method == "POST":

        fName = request.form.get('fName')
        lName = request.form.get('lName')
        email = request.form.get('email')
        password = request.form.get('password')
        # Check if user exists

        exists = Users.query.filter_by(email=email).first()

        if exists:
            duplicateUser = "There is already an account with this email."
        # Create records in our database
        new_user = Users(
            fName = fName,
            lName = lName,
            email = email,
            password = password
        )

        # Add each instance into the database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("You have signed up successfully!")
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            print(error)

    data = Users.query
    return render_template("signup.html", users=data, error=duplicateUser)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # set variables
        user_email = request.form.get("email")
        user_pw = request.form.get("password")
        Filtered = Users.query.filter_by(email=user_email).first()
        if Filtered: # check if user exist
            if Filtered.password == user_pw: # check if password is correct
                ssn["user"] = Filtered.fName
                ssn["user_id"] = Filtered.id
                flash("Welcome, {}".format(Filtered.fName))
                return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out successfully!")
    ssn.pop("user")
    ssn.pop("user_id")
    return redirect(url_for('home'))


@app.route("/createPot", methods=["GET", "POST"])
def create_pot():
    """ Create pot page """
    if request.method == "POST":

        # Get the current user logged in
        logged_user = 0
        if "user_id" in ssn:
            logged_user = ssn["user_id"]
        
        # Convert vlue from checkbox to accepted format
        private = True
        formValue = request.form.get('private')
        if formValue in ('y', 'yes', 't', 'true', 'True', 'on', '1'):
            private = True
        elif formValue in ('n', 'no', 'f', 'false', 'False', 'off', '0', None):
            private = False
        else:
            raise ValueError("invalid truth value %r" % (formValue,))

        peers = request.form.get('invited')
        invite = peers.replace("[", "").replace("]", "").replace('"', '')
        invite = invite.split(',')
        print(invite)


        # Create records in our database
        new_pot = Pots(
            title = request.form.get('title'),
            goal = request.form.get('goal'),
            currency = request.form.get('currency'),
            cycle = request.form.get('cycle'),
            amount = request.form.get('amount'),
            isPrivate = private,
            creator_id = logged_user,
            participants = peers
        )

        # Add each instance into the database
        try:
            db.session.add(new_pot)
            db.session.commit()
            sendInvites(invite)
            flash("Pot added successfylly.")
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            print(error)

    data = Pots.query
    return render_template("createPot.html", pots=data, exchange_data=exchange_data)


@app.route('/pots/<int:id>')
def pot(id):
    pot = Pots.query.get_or_404(id)
    participants = pot.participants.replace("[", "").replace("]", "").replace('"', '')
    participants = participants.split(',')
    taken_spots = len(participants)
    return render_template('pot.html', pot=pot, participants=taken_spots)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
