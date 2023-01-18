Basic flask app template

This template includes:

flask
template folder
static folder
css folder
js folder
base html template
main html template
base css file
base js file
requirements.txt

you need to create a file (on the same level as readme file) named "env.py" and put these contents in this file for the app to work:

> import os

> os.environ.setdefault("IP", "0.0.0.0")  
> os.environ.setdefault("PORT", "5000")  
> os.environ.setdefault("SECRET_KEY", "THisIsMySecretKey")

All static files are linked to base html template, main html template inherets from base

to run the live server, run the following command in the terminal:
> python3 app.py
