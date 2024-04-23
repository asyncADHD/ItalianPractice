import os


class Config:
    # Sets the base directory for the database file
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Configures the SQLALCHEMY_DATABASE_URI for SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'italian_verbs.db')

    # Optionally, turn off the modification tracker to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
