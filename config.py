import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application Title
APP_NAME="Example App"

# Application Width
APP_WIDTH=500

# Application Minimal Width
APP_MIN_WIDTH=400

# Application Height
APP_HEIGHT=300

# Application Minimal Height
APP_MIN_HEIGHT=250