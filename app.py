import os
#from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////moneypot.db'


# Initialize database
db = SQLAlchemy(app)

# Create a class-based model for the "Users" database
class Users(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    EmailAddress = db.Column(db.String(200), nullable=False, unique=True)
    Password = db.Column(db.String(50), nullable=False)

    # Create String
    def __repr__(self):
        return '<Name %r>' % self.name


@app.route("/")
def home():
    """ the main view of the app """
    return render_template("main.html")

@app.route('/dashboard/')
def about():
    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
