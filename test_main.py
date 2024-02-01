from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_auth_response(username, password):
    auth_response = client.post(
        "/token",
        data= {
            "username": username,
            "password": password
        }
    )

    return auth_response

def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200

def test_auth_error():
    auth_response = get_auth_response(username="", password="")

    access_token = auth_response.json().get("access_token")
    message = auth_response.json().get("detail")[0].get("msg")

    assert access_token == None
    assert message == "Field required"

def test_auth_success():
    auth_response = get_auth_response(username="Elliot", password="123456")

    access_token = auth_response.json().get("access_token")
    assert access_token

def test_post_article():
    auth_response = get_auth_response(username="Elliot", password="123456")
    
    access_token = auth_response.json().get("access_token")
    assert access_token

    response = client.post(
        "/article/",
        json= {
            "title": "Test article",
            "content": "Test content",
            "published": True,
            "creator_id": 1
        },
        headers= {
            "Authorization": "bearer " + access_token
        }
    )

    assert response.status_code == 200
    assert response.json().get("title") == "Test article"
