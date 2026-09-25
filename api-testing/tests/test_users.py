import requests


def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] is not None

def test_user_not_found():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999"
    )

    assert response.status_code == 404

def test_create_post():
    data = {
        "title": "Arham API Test",
        "body": "Learning API automation",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == "Arham API Test"
    assert response_data["body"] == "Learning API automation"
    assert response_data["userId"] == 1
    assert "id" in response_data

def test_update_post():
    data = {
        "id": 1,
        "title": "Arham Updated Test",
        "body": "Updated API testing",
        "userId": 1
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1
    assert response_data["title"] == "Arham Updated Test"
    assert response_data["body"] == "Updated API testing"

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200