from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_hello_default():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "hello, world"}

def test_hello_with_name():
    r = client.get("/hello?name=junior")
    assert r.status_code == 200
    assert r.json() == {"message": "hello, junior"}

def test_echo_ok():
    r = client.post("/echo", json={"text": "abc"})
    assert r.status_code == 200
    assert r.json() == {"text": "abc", "length": 3}

def test_echo_validation_error():
    r = client.post("/echo", json={})
    assert r.status_code == 422

def test_sum():
    r = client.get("/sum?a=1&b=2")
    assert r.status_code == 200
    # expect the result to be 3
    assert r.json() == {"result": 3}