import json
import os
import unittest

from flask import url_for

from app import app, db

BASEDIR = os.path.abspath(os.path.dirname(__file__))


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(BASEDIR, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        # Disable sending emails during unit testing

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.drop_all()

if __name__ == "__main__":
    unittest.main()