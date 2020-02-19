from flask import Flask
from flask_migrate import Migrate
from config import Config, app_config
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('/home/yadav_padiyar/final/microblog/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

app = create_app(config_name="testing")

# app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate=Migrate(app, db)
migrate = Migrate(compare_type=True)
migrate.init_app(app, db)

from app import routes, models
from app.unit_testing import test_user
