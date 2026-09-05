import pytest


pytestmark = pytest.mark.auth


def test_login_returns_bearer_token(api_client):
    response = api_client.login("qa.engineer", "correct-password")

    assert response.status_code == 200
    assert response.json() == {
        "access_token": "portfolio-token",
        "token_type": "bearer",
    }


@pytest.mark.parametrize(
    "username,password",
    [
        ("qa.engineer", "wrong-password"),
        ("unknown.user", "correct-password"),
    ],
)
def test_login_rejects_invalid_credentials(api_client, username, password):
    response = api_client.login(username, password)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_create_order_requires_authorization(api_client, test_data):
    response = api_client.create_order(test_data["valid_order"])

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or missing token"
