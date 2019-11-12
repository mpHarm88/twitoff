from flask import Flask, render_template, request
from .models import DB, User, Tweet
from decouple import config

# now we make a app factory
def create_app():
    app = Flask(__name__)
    
    # add our config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # now have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        tweets = Tweet.query.all()
        return render_template('base.html', title='Home', users=users, tweets=tweets)
    return app

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])
    return app 

