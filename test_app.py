from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_ready():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"ready": True}
