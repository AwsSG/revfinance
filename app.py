import os
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


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
