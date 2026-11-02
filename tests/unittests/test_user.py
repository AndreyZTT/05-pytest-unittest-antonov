"""Unit tests for the User class."""
import unittest
import allure

from src.user import User


@allure.feature("User")
class TestUser(unittest.TestCase):
    """Unit tests for the User class."""

    def setUp(self):
        self.user = User(
            user_id=1,
            name="Alex",
            age=25,
            email="alex@test.com"
        )

    def tearDown(self):
        self.user = None

    @allure.story("is_adult")
    @allure.title("User older than 18 is adult")
    def test_is_adult_true(self):
        """Тест метода is_adult для пользователя старше 18 лет."""
        self.assertTrue(self.user.is_adult())

    @allure.story("is_adult")
    @allure.title("User younger than 18 is not adult")
    def test_is_adult_false(self):
        """Тест метода is_adult для пользователя младше 18 лет."""
        self.user.age = 17
        self.assertFalse(self.user.is_adult())

    @allure.story("is_adult")
    @allure.title("User age 18 is adult")
    def test_is_adult_boundary(self):
        """Тест метода is_adult для пользователя ровно 18 лет."""
        self.user.age = 18
        self.assertTrue(self.user.is_adult())

    @allure.story("to_dict")
    @allure.title("Convert user to dictionary")
    def test_to_dict(self):
        """Тест метода to_dict класса User."""
        self.assertEqual(self.user.to_dict(), {
            "id": 1,
            "name": "Alex",
            "age": 25,
            "email": "alex@test.com"
        }
        )
