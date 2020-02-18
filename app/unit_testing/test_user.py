from flask import Flask
from app.user import addmessage
from app.routes import home


def test_base_route():
    app=Flask(__name__)
    home(app)
    client = app.test_client()
    url = '/'

    response=client.get(url)
    assert response.get_data() == b"Welcome Home"
    assert response.status_code == 200

