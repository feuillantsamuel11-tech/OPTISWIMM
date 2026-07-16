from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate():

    response = client.post(
        "/api/v1/generate-session",
        json={
            "race_distance": 400,
            "recent_loads": [5000] * 28,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "session" in data
    assert "explanation" in data