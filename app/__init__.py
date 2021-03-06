from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    # Define flask app environement config
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    print(f' * Flask ENV is set to: {app.config["ENV"]}')

    # Config app sqlachemy database
    app.config['SQLALCHEMY_DATABASE_URI'] =  f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Define route with Blueprint
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Check if database is created
    from .models import User, Note
    create_database(app)

    # Define login access to pages
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # redirection si login necessaire
    login_manager.init_app(app)

    # Get current user data from db
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    #print(app.config)

    return app

def create_database(app):
    if not path.exists('app/'+ DB_NAME):
        db.create_all(app=app)
        print('Database created!')




