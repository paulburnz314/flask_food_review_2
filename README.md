# flask_food_review
A python flask sqlAlchemy restaurant review site project.

## Background

This is based on Miguel Grinberg's Udemy course - The Flask Mega-Tutorial<br>
Also check out https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world <br>

Other info gleaned from:<br>
Rafeh Qazi, aka, Clever Programmer YouTube, Python Flask Tutorial for Beginners<br>
https://youtu.be/3mwFC4SHY-Y <br>

Anthony Herbert, Pretty Printed YouTube, Flask SQLAlchemy series of videos<br>
https://youtu.be/Tu4vRU4lt6k


### First steps for the python project
1. Make a new project folder
1. Via command prompt navigate to cd c:\users\...\project_folder
1. python -m venv venv  # set up the virtual env
1. venv\Scripts\activate  # acitivate the virtual env
1. python -m pip install --upgrade pip  # uninstalls pip-20.1.1 then install pip-20.2.2
1. pip install flask  # adds flask plus the packages it needs
1. pip install Flask-SQLAlchemy  # Flask-SQLAlchemy==2.4.4
1. pip install Flask-Migrate  # Flask-Migrate==2.5.3

### factor out the different components into a group of interconnected modules
1. run.py
   1. The file invoked by flask run
   1. Be sure to 'Set FLASK_APP=run.py' (Set is for windows)
1. app/__init__.py
   1. Dunder init executes and defines the app package
   1. It brings together all of the various components
1. app/config.py - configs baby
1. app/routes.py
   1. Where the routes are defined
   1. Routes are the different URLs that the application implements
1. app/models.py - where the models are defined, i.e., tables, fields and relationships
1. app/forms.py
   1. Where the forms are defined
   1. The Flask-WTF extension uses Python classes to represent web forms
   1. A form class simply defines the fields of the form as class variables
1. app/static/ - styling sheets and javascript
1. app/templates/
   1. Where the Jinja2 templates are stored
   1. These are html files with jinja2 notations, i.e., {% block head %} {% endblock %}
   1. The notations are called percent braces and double braces
   
### Setting up the database
1. flask db init - 'Set FLASK_APP=run.py' before running flask commands
1. flask db migrate -m "first migration"
   1. Make schema changes without recreating the database from scratch
   1. Alembic adds a migration script to a repository each time changes are made
   1. Does not make any actual changes to the database
1. flask db upgrade
   1. the migration has to be added to source control
   1. upgrade() applies the migration
   1. downgrade() removes it so you can go back to an older version
   1. SQLite detects the database does not exist and will create it the 1st time upgrade is carried out
1. other commands include:
   1. flask db history
   1. flask db current
   
### Playing with the database
1. with venv activated start python
1. from app import db
1. from app.models import Foodservice, User, Review
1. u = User(username='Susan', email='susan@example.com')
1. db.session.add(u)
1. db.session.commit()

### Using flask shell
what to do if you added a user without a password
1. from app import db
1. from app.models import *
1. susan = User.query.get(2)
1. susan.set_password('cathat1')
1. db.session.commit()