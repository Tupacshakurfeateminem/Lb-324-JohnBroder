import pytest
from app import app  # Importiere die Flask-App

@pytest.fixture
def client():
    # Flask-Testclient einrichten
    app.testing = True
    return app.test_client()

def test_home_page(client):
    # Sende eine GET-Anfrage an die `/`-Route
    response = client.get('/')
    
    # Überprüfe, ob der Statuscode 200 ist
    assert response.status_code == 200
    
    # Überprüfe, ob der Text in der Antwort enthalten ist
    assert b"Welcome to the Simple Flask Application" in response.data
