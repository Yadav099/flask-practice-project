from flask import Flask
from flask_migrate import Migrate
from config import Config, app_config
from flask_sqlalchemy import SQLAlchemy
#imported required libraries


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('/home/yadav_padiyar/final/microblog/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

#create app which is used as decorator in routing
app = create_app(config_name="testing")

app.config.from_object(Config)

#getting the database and migrate object
db = SQLAlchemy(app)
migrate = Migrate(compare_type=True)
migrate.init_app(app, db)

#import of routing,database and testing related files
from app import Routes, models
from app.unit_testing import test_user
