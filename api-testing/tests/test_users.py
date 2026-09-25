import requests
import pytest

def test_get_user(base_url):
    response = requests.get(
        f"{base_url}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] is not None
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)

def test_user_not_found(base_url):
    response = requests.get(
        f"{base_url}/users/999"
    )

    assert response.status_code == 404

def test_create_post(base_url):
    data = {
        "title": "Arham API Test",
        "body": "Learning API automation",
        "userId": 1
    }

    response = requests.post(
        f"{base_url}/posts",
        json=data
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == "Arham API Test"
    assert response_data["body"] == "Learning API automation"
    assert response_data["userId"] == 1
    assert "id" in response_data

def test_update_post(base_url):
    data = {
        "id": 1,
        "title": "Arham Updated Test",
        "body": "Updated API testing",
        "userId": 1
    }

    response = requests.put(
        f"{base_url}/posts/1",
        json=data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1
    assert response_data["title"] == "Arham Updated Test"
    assert response_data["body"] == "Updated API testing"

def test_delete_post(base_url):
    response = requests.delete(
        f"{base_url}/posts/1"
    )

    assert response.status_code == 200

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_multiple_users(base_url, user_id):
    response = requests.get(
        f"{base_url}/users/{user_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id