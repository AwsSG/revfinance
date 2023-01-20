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

> npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch

For faster development, npm script has been added. Run command:

>  npm run watch


### Connect to the database Guide
To connect to the databse you need to follow these steps:

- Create a new file called creds.py

- Enter the following code

        from sqlalchemy import create_engine
    
        # Database Credentials
        DB_HOST = ""
        DB_NAME = ""
        DB_USER = ""
        DB_PASS = ""
    
        def database_credentials():
        return create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
