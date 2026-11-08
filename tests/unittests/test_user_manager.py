"""Unit tests for the UserManager class."""
import unittest
import allure

from src.user import User
from src.user_manager import UserManager


@allure.feature("User Manager")
class TestUserManager(unittest.TestCase):
    """Юнит-тесты для класса UserManager."""

    def setUp(self):
        self.manager = UserManager()

        self.user = User(
            user_id=1,
            name="Alex",
            age=25,
            email="alex@test.com"
        )

    def tearDown(self):
        self.user = None
        self.manager = None

    @allure.story("Add user")
    @allure.title("Add valid user")
    def test_add_user(self):
        """Тест добавления пользователя в менеджер."""
        self.manager.add_user(self.user)
        self.assertIn(self.user, self.manager.get_all_users())

    @allure.story("Add user")
    @allure.title("Duplicate id raises ValueError")
    def test_add_user_duplicate_id(self):
        """Тест дубликата id пользователя в менеджере."""
        self.manager.add_user(self.user)
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Invalid id type raises TypeError")
    def test_add_user_invalid_id_type(self):
        """Тест добавления пользователя с недопустимым типом id."""
        test_data = [
            "1",
            None,
            1.5,
            {},
            []
        ]

        for invalid_id in test_data:
            with self.subTest(invalid_id=invalid_id):
                invalid_user = User(
                    user_id=invalid_id,
                    name="Alex",
                    age=25,
                    email="alex@test.com"
                )
                with self.assertRaises(TypeError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Empty name raises ValueError")
    def test_add_user_empty_name(self):
        """Тест добавления пользователя с пустым именем."""
        invalid_user = User(
            user_id=1,
            name="",
            age=25,
            email="alex@test.com"
        )
        with self.assertRaises(ValueError):
            self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Short name raises ValueError")
    def test_add_user_short_name(self):
        """Тест добавления пользователя с коротким именем."""
        test_data = [
                    "A",
                    "B",
                    "C",
                    "D",
                ]

        for invalid_name in test_data:
            with self.subTest(invalid_name=invalid_name):
                invalid_user = User(
                    user_id=1,
                    name=invalid_name,
                    age=25,
                    email="alex@test.com"
                )
                with self.assertRaises(ValueError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Invalid name type raises TypeError")
    def test_add_user_invalid_name_type(self):
        """Тест добавления пользователя с недопустимым типом имени."""
        test_data = [
            123,
            None,
            1.5,
            {},
            []
        ]

        for invalid_name in test_data:
            with self.subTest(invalid_name=invalid_name):
                invalid_user = User(
                    user_id=1,
                    name=invalid_name,
                    age=25,
                    email="alex@test.com"
                )
                with self.assertRaises(TypeError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Negative age raises ValueError")
    def test_add_user_negative_age(self):
        """Тест добавления пользователя с отрицательным возрастом."""
        test_data = [
            -10,
            -1,
            -100,
            -35,
        ]

        for invalid_age in test_data:
            with self.subTest(invalid_age=invalid_age):
                invalid_user = User(
                    user_id=1,
                    name="Alex",
                    age=invalid_age,
                    email="alex@test.com"
                )
                with self.assertRaises(ValueError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Age greater than 120 raises ValueError")
    def test_add_user_large_age(self):
        """Тест добавления пользователя с возрастом больше 120."""
        test_data = [
            121,
            130,
            200,
            1000,
        ]

        for invalid_age in test_data:
            with self.subTest(invalid_age=invalid_age):
                invalid_user = User(
                    user_id=1,
                    name="Alex",
                    age=invalid_age,
                    email="alex@test.com"
                )
                with self.assertRaises(ValueError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Invalid age type raises TypeError")
    def test_add_user_invalid_age_type(self):
        """Тест добавления пользователя с недопустимым типом возраста."""
        test_data = [
            "25",
            121.5,
            None,
            [],
            {},
        ]

        for invalid_age in test_data:
            with self.subTest(invalid_age=invalid_age):
                invalid_user = User(
                    user_id=1,
                    name="Alex",
                    age=invalid_age,
                    email="alex@test.com"
                )
                with self.assertRaises(TypeError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Invalid email raises ValueError")
    def test_add_user_invalid_email(self):
        """Тест добавления пользователя с недопустимым email."""
        test_data = [
            "alexexample.com",
            "alex.example.com",
            "alexexamplecom",
            ""
        ]

        for invalid_email in test_data:
            with self.subTest(invalid_email=invalid_email):
                invalid_user = User(
                    user_id=1,
                    name="Alex",
                    age=25,
                    email=invalid_email
                )
                with self.assertRaises(ValueError):
                    self.manager.add_user(invalid_user)

    @allure.story("Add user")
    @allure.title("Invalid email type raises TypeError")
    def test_add_user_invalid_email_type(self):
        """Тест добавления пользователя с недопустимым типом email."""
        test_data = [
            123,
            1.5,
            {},
            []
        ]

        for invalid_email in test_data:
            with self.subTest(invalid_email=invalid_email):
                invalid_user = User(
                    user_id=1,
                    name="Alex",
                    age=25,
                    email=invalid_email
                )
                with self.assertRaises(TypeError):
                    self.manager.add_user(invalid_user)

    @allure.story("Get user")
    @allure.title("Get existing user")
    def test_get_existing_user(self):
        """Тест получения существующего пользователя из менеджера."""
        self.manager.add_user(self.user)
        retrieved_user = self.manager.get_user(self.user.id)
        self.assertEqual(retrieved_user, self.user)

    @allure.story("Get user")
    @allure.title("Get missing user")
    def test_get_missing_user(self):
        """Тест получения отсутствующего пользователя из менеджера."""
        self.manager.add_user(self.user)
        retrieved_user = self.manager.get_user(self.user.id + 1)
        self.assertIsNone(retrieved_user)

    @allure.story("Remove user")
    @allure.title("Remove existing user")
    def test_remove_user(self):
        """Тест удаления существующего пользователя из менеджера."""
        self.manager.add_user(self.user)
        self.manager.remove_user(self.user.id)
        result = self.manager.get_user(self.user.id)
        self.assertIsNone(result)

    @allure.story("Remove user")
    @allure.title("Remove missing user")
    def test_remove_missing_user(self):
        """Тест удаления отсутствующего пользователя из менеджера."""
        with self.assertRaises(ValueError):
            self.manager.remove_user(self.user.id + 1)

    @allure.story("Get all users")
    @allure.title("Get users from empty manager")
    def test_get_all_users_empty(self):
        """Тест получения списка пользователей из пустого менеджера."""
        test_data = {
            "users": [],
        }
        for user in test_data["users"]:
            self.manager.add_user(user)
        result = self.manager.get_all_users()
        self.assertEqual(result, test_data["users"])

    @allure.story("Get all users")
    @allure.title("Get users list")
    def test_get_all_users(self):
        """Тест получения списка пользователей из менеджера."""
        test_data = [
                User(1, "Alex", 25, "alex@example.com"),
                User(2, "John", 30, "john@example.com"),
                User(3, "David", 20, "david@example.com")
        ]
        for user in test_data:
            self.manager.add_user(user)
        result = self.manager.get_all_users()
        self.assertEqual(result, test_data)

    @allure.story("Count users")
    @allure.title("Count users in empty manager")
    def test_count_users_empty(self):
        """Тест подсчета количества пользователей в пустом менеджере."""
        result = self.manager.count_users()
        self.assertEqual(result, 0)

    @allure.story("Count users")
    @allure.title("Count users")
    def test_count_users(self):
        """Тест подсчета количества пользователей в менеджере."""
        test_data = [
                User(1, "Alex", 25, "alex@example.com"),
                User(2, "John", 30, "john@example.com"),
                User(3, "David", 20, "david@example.com")
        ]
        for user in test_data:
            self.manager.add_user(user)
        result = self.manager.count_users()
        self.assertEqual(result, len(test_data))
