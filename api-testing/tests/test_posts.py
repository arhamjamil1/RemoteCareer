import requests


def test_get_post(base_url):
    response = requests.get(
        f"{base_url}/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data


def test_post_not_found(base_url):
    response = requests.get(
        f"{base_url}/posts/9999"
    )

    assert response.status_code == 404