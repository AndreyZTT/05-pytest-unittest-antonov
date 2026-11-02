from .user import User


class UserManager:

    def __init__(self):
        self._users = []

    def add_user(self, user):

        if not isinstance(user.id, int):
            raise TypeError("User id must be integer")

        if self.get_user(user.id):
            raise ValueError("User id already exists")

        if not isinstance(user.name, str):
            raise TypeError("Name must be string")

        if len(user.name.strip()) < 2:
            raise ValueError(
                "Name must contain at least 2 characters"
            )

        if not isinstance(user.age, int):
            raise TypeError("Age must be integer")

        if user.age < 0 or user.age > 120:
            raise ValueError(
                "Age must be between 0 and 120"
            )

        if not isinstance(user.email, str):
            raise TypeError("Email must be string")

        if "@" not in user.email:
            raise ValueError("Invalid email")

        self._users.append(user)

    def get_user(self, user_id):

        for user in self._users:
            if user.id == user_id:
                return user

        return None

    def remove_user(self, user_id):

        user = self.get_user(user_id)

        if user is None:
            raise ValueError(
                "User not found"
            )

        self._users.remove(user)

    def get_all_users(self):
        return self._users

    def count_users(self):
        return len(self._users)