# Why create this starter code?

It's annoying to setup all the boilerplate involved with a web app -- creating 
this boilerplate could reduce setup time when creating an app. It will enable
me to "dive right in" to the meat of a project.

## Why this stack?
The React-Flask webpack stack is one that I'm very familiar with (through prior projects with React and Flask in addition to its usage in my internship). By deleting the `app/static` folder, this can also be used as boilerplate for a Flask app (with any frontend). 

### Name the app
Alters:
app folder name
current folder name
config.py

### Run the app
`$ flask run`
Alter `.flaskenv` to change ports, sqlalchemy_database_uri
Alter your own `.env` to change secret_key

### Add a blueprint
Add to blueprints list in `/handlers/__init__.py`

### Make migrations
Create a model in the models folder
Import the model in a blueprint if it isn't already
Add the blueprint as explained above if it isn't already
Run `flask db migrate`

### Add a React component
Automatically built with webpack once it is watched

## Implementation details

### Flask - Migrate
SQLAlchemy

### SQLite


### Webpack


