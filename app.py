import os
from flask import Flask, render_template, request
from database import User, session, get_users

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def home():
    """ the main view of the app """
    return render_template("main.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ Sign up page """
    if request.method == "POST":
        # Create records in our database
        new_user = User(
            FirstName = request.form.get('fName'),
            LastName = request.form.get('lName'),
            EmailAddress = request.form.get('email'),
            Password = request.form.get('password')
        )
        # Add each instance of our Note into the session
        session.add(new_user)
        try:
            session.commit()
        except:
            session.rollback()
            print("There was an error submitting this request. Please, try again.")
    
    data = get_users()
    return render_template("signup.html", users=data)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
