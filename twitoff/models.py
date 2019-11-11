""""These are my database models  """

from flask_sqlalchemy import SQLAlchemy

# import database for global scope
DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users we analyze  """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """The suers tweets from twitter"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))

