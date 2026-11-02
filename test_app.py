
import app

def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Automatic Jenkins Build Successful!" in response.data

def test_health():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert b"healthy" in response.data
