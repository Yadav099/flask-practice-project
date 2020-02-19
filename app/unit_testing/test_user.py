import json
import os
import unittest
from io import BytesIO, StringIO
from unittest.mock import Mock

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


    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    #test for adding new user
    def test_addmessage(self):
        response = self.app.post('/Home/Register/user',
                                 data=json.dumps(dict(name='bar',email='abc@xyz.com',age=20,city='Newyork',accepted=False)),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Data acquired', response.data)

#update age
    # def test_update_useragel(self):
    #
    #     response=self.app.put("/Home/abc/changeage?age=20")
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     # self.assertEqual(b'NO Changes', response.data)

    #
    # def test_update_city(self):
    #     data = {
    #         'city': 'asdff'
    #     }
    #     response = self.app.put("/Home/abc/changecity/", query_string=data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(b'updated age', response.data)

    #testing delete user/customer
    def test_delete_user(self):
        response = self.app.delete('/Home/userlist?deleteuser=abc',)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(b' deleted', response.data)


    #testing to add employee in database
    def test_add_employee(self):
        response = self.app.post('/Home/Register/company',
                                 data=json.dumps(dict(e_name='abc',e_email='abc@xyz.com',e_password='abc')),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Data acquired', response.data)

    #testing to fetech data from database
    def test_view_employee(self):
        response = self.app.get('/Home/Profile/Employee/abc')
        data=Mock()
        self.assertEqual(response.status_code, 200)
        # id=data.e_name
        # id2=data.e_email
        # id3=data.e_password
        # message=" Name:" + id + ", mail id:" + id2 + ",  Age:" +id3
        self.assertEqual(b"no data", response.data)

    #testing to posting a html template
    def test_templatehtml(self):
        response = self.app.post('/mail')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"pushed", response.data)
        response=self.app.get('/mail')
        self.assertEqual(response.status_code, 200)

    # testing to upload and input cdv data of customer into database
    def test_customercsv(self):
        data = {
            'Customer': (BytesIO(b'FILE CONTENT'), 'test.csv')
        }

        response = self.app.post('/Home/Register/Customercsv/', content_type='multipart/form-data', buffered=True,  data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"Data aquired", response.data)


        response = self.app.get('/Home/Profile/Customercsv/name')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"No data", response.data)


    # testing to upload and input cdv data of order into database
    def test_ordercsv(self):
        data = {
            'Product': (BytesIO(b'FILE CONTENT'), 'test.csv')
        }

        response = self.app.post('/Home/Register/Productcsv/', content_type='multipart/form-data', buffered=True,
                                 data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"Data aquired", response.data)



        response = self.app.get('/Home/Products?id=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"No data", response.data)

    #testing the uploading review csv file into database
    def test_reviewcsv(self):
        data = {
            'Review': (BytesIO(b'FILE CONTENT'), 'test.csv')
        }

        response = self.app.post('/Home/Product/Review', content_type='multipart/form-data', buffered=True,
                                 data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"Data aquired", response.data)

    #testing to send static mail

if __name__ == "__main__":
    unittest.main()
