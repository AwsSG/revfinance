import os
from flask import Flask, render_template, request, redirect,url_for, flash
from flask import session as ssn
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

if os.path.exists("env.py"):
    import env

# Send email invites to users to join a pot
from sendInvites import sendInvites

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moneypot.db'
app.secret_key = os.environ.get("SECRET_KEY")
# Initialize database
db = SQLAlchemy(app)

# Create db model for users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    # String to return name when something is added to database
    def __repr__(self):
        return '<Name %r>' % self.id


# Create db model for potss table
class Pots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.Integer, nullable=False)
    cycle = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    isPrivate = db.Column(db.Boolean, nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # String to return name when something is added to database
    def __repr__(self):
        return '<Name %r>' % self.id

@app.route("/")
def home():
    """ the main view of the app """
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


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
            # We can redirect to index if we want to
            # return redirect('/dashboard')
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
                flash("Welcome, {}".format(Filtered.fName))
                return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/createPot", methods=["GET", "POST"])
def create_pot():
    """ Create pot page """
    if request.method == "POST":
        # Create records in our database

        private = True
        formValue = request.form.get('private')
        if formValue in ('y', 'yes', 't', 'true', 'True', 'on', '1'):
            private = True
        elif formValue in ('n', 'no', 'f', 'false', 'False', 'off', '0', None):
            private = False
        else:
            raise ValueError("invalid truth value %r" % (formValue,))

        new_pot = Pots(
            title = request.form.get('title'),
            goal = request.form.get('goal'),
            cycle = request.form.get('cycle'),
            amount = request.form.get('amount'),
            isPrivate = private,
            # Once the login is completed we can get the logged user id
            creator = 1
        )

        peer1 = request.form.get('peer1')
        peer2 = request.form.get('peer2')
        peer3 = request.form.get('peer3')
        peer4 = request.form.get('peer4')

        peers = []
        peers.append(peer1)
        peers.append(peer2)
        peers.append(peer3)
        peers.append(peer4)


        # Add each instance into the database
        try:
            db.session.add(new_pot)
            db.session.commit()
            sendInvites(peers)
            # We can redirect to index if we want to
            # return redirect('/dashboard')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            print(error)

    data = Pots.query
    return render_template("createPot.html", pots=data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
