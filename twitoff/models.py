""""These are my database models  """

from flask_sqlalchemy import SQLAlchemy

# import database for global scope
DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users we analyze  """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger) 
    def __repr__(self):
        return '<User {}>.format(self.name)'


class Tweet(DB.Model):
    """The users tweets from twitter"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
