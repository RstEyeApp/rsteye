def test_home(client):
    resp = client.get("/")

    assert resp.status_code == 200



