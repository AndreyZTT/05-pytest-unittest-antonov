import pytest
import allure

from src.user import User


@allure.feature("User")
@allure.story("is_adult")
@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True)
    ]
)
def test_is_adult(age, expected):
    user = User(
        user_id=1,
        name="Alex",
        age=age,
        email="alex@test.com"
    )
    assert user.is_adult() == expected


@allure.feature("User")
@allure.story("to_dict")
@allure.title("Convert user to dictionary")
def test_to_dict(user):
    result = user.to_dict()

    assert result == {
        "id": 1,
        "name": "Alex",
        "age": 25,
        "email": "alex@test.com"
    }
    