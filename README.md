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

> os.environ.setdefault("IP", "0.0.0.0") <br>
> os.environ.setdefault("PORT", "5000") <br>
> os.environ.setdefault("SECRET_KEY", "THisIsMySecretKey") <br>


All static files are linked to base html template, main html template inherets from base

to run the live server, run the following command in the terminal:
> python3 app.py

### Tailwind Installation Guide
Tailwind is added with the NPM (Node Package Manager), To be able to use it on your machine you need to have Node.js installed:

Download Node.js [here](https://nodejs.org/en/)

After Node.js is installed, install the Tailwind by running the following command in the terminal from the roof of the project:

> npm install

To compile Tailwind to work during development use command:

> npx tailwindcss -i ./static/src/input.css -o ./static/output.css --watch