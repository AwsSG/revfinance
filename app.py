import os
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, render_template, request, redirect,url_for, flash
from flask import session as ssn
from database import User, Pot, session, get_users, get_pots

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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
    if request.method == "POST":
        # Create records in our database
        new_user = User(
            FirstName=request.form.get('fName'),
            LastName=request.form.get('lName'),
            EmailAddress=request.form.get('email'),
            Password=request.form.get('password')
        )

        # Add each instance into the session
        session.add(new_user)
        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            error = str(e.__dict__['orig'])
            print(error)
    data = get_users()
    session.close()
    return render_template("signup.html", users=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # set variables
        users = get_users()
        user_email = request.form.get("email")
        user_pw = request.form.get("password")
        user_index = next((index for (index, d) in enumerate(users) if d['Email'] == user_email), None)
        # check if user exist in db
        if user_index:
            print("user found!")
        # check if password is correct
            if users[user_index]["Password"] == user_pw:
                print(ssn["user"])
                ssn["user"] = users[user_index]["Name"]
                flash("Welcome, {}".format(ssn["user"]))
                return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
            print("user not exist")

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

        new_pot = Pot(
            PotTitle=request.form.get('title'),
            GoalAmount=request.form.get('goal'),
            PayCycle=request.form.get('cycle'),
            PaymentAmount=request.form.get('amount'),
            isPrivate=private,
            Creator=1,
            # The creator will need to get the user ID from the get from
            Peers=request.form.get('peer1')
        )

        # Add each instance into the session
        session.add(new_pot)
        print(new_pot)
        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            error = str(e.__dict__['orig'])
            print(error)
    data = get_pots()
    session.close()
    return render_template("createPot.html", pots=data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
