from fastapi.testclient import TestClient
from main import app, models, database  # absolute import

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Testing"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["completed"] is False
