import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Normal mode
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False


#testing mode
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_URL'] or 'sqlite:///' + os.path.join(basedir, 'app.db')

    DEBUG = True

#switch between testing and developer mode
app_config = {
    'config': Config,
    'testing': TestingConfig,
}