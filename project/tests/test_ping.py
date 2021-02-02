def test_ping(test_app):
    response = test_app.get("/ping")

    expected = {"environment": "dev", "ping": "pong!", "testing": True}
    assert response.status_code == 200
    assert response.json() == expected
