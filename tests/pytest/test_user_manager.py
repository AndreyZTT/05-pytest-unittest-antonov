import pytest
import allure

from src.user import User


@allure.feature("User Manager")
@allure.story("Add user")
def test_add_user(manager, user):
    assert manager.get_user(user.id) is None
    manager.add_user(user)
    assert manager.get_user(user.id) == user


@allure.feature("User Manager")
@allure.story("Add user - duplicate id")
def test_add_user_duplicate_id(manager):
    user1 = User(
        user_id=1,
        name="Alex",
        age=25,
        email="alex@test.com"
    )
    user2 = User(
            user_id=1,
            name="Alex",
            age=25,
            email="alex@test.com"
        )
    manager.add_user(user1)
    with pytest.raises(ValueError):
        manager.add_user(user2)


@allure.feature("User Manager")
@allure.story("Add user - invalid id type")
@pytest.mark.parametrize(
    "invalid_id",
    [
        "1",
        None,
        1.5,
        {},
        []
    ]
)
def test_invalid_id_type(manager, invalid_id):
    user = User(
            user_id=invalid_id,
            name="Alex",
            age=25,
            email="alex@test.com"
        )
    
    with pytest.raises(TypeError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user - invalid name")
@pytest.mark.parametrize(
    "name",
    [
        "",
        "A"
    ]
)
def test_invalid_name(manager, name):
    user = User(
                user_id=1,
                name=name,
                age=25,
                email="alex@test.com"
            )
        
    with pytest.raises(ValueError):
        manager.add_user(user)

@allure.feature("User Manager")
@allure.story("Add user - invalid name type")
@pytest.mark.parametrize(
    "name",
    [
        123,
        1.5,
        {},
        []
    ]
)
def test_invalid_name_type(manager, name):
    user = User(
                user_id=1,
                name=name,
                age=25,
                email="alex@test.com"
            )
        
    with pytest.raises(TypeError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user - invalid age")
@pytest.mark.parametrize(
    "age",
    [
        -1,
        121
    ]
)
def test_invalid_age(manager, age):
    user = User(
            user_id=1,
                name="Alex",
                age=age,
                email="alex@test.com"
            )
        
    with pytest.raises(ValueError):
        manager.add_user(user)

@allure.feature("User Manager")
@allure.story("Add user - invalid age type")
@pytest.mark.parametrize(
    "age",
    [
        "25",
        None,
        1.5,
        {},
        []
    ]
)
def test_invalid_age_type(manager, age):
    user = User(
            user_id=1,
                name="Alex",
                age=age,
                email="alex@test.com"
            )
        
    with pytest.raises(TypeError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user - invalid email type")
@pytest.mark.parametrize(
    "email",
    [
        123,
        1.5,
        {},
        []
    ]
)
def test_invalid_email_type(manager, email):
    user = User(
        user_id=1,
        name="Alex",
        age=25,
        email=email
    )

    with pytest.raises(TypeError):
        manager.add_user(user)

@allure.feature("User Manager")
@allure.story("Add user - invalid email")
@pytest.mark.parametrize(
    "email",
    [
        "alexexample.com",
        "alex.example.com",
        "alexexamplecom",
        ""
    ]
)
def test_invalid_email(manager, email):
    user = User(
        user_id=1,
        name="Alex",
        age=25,
        email=email
    )

    with pytest.raises(ValueError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Get user")
def test_get_existing_user(manager, user):
    manager.add_user(user)
    retrieved_user = manager.get_user(user.id)
    assert retrieved_user == user


@allure.feature("User Manager")
@allure.story("Get user - missing user")
def test_get_missing_user(manager):
    retrieved_user = manager.get_user(777)
    assert retrieved_user is None


@allure.feature("User Manager")
@allure.story("Remove user")
def test_remove_user(manager, user):
    manager.add_user(user)
    manager.remove_user(user.id)
    assert manager.get_user(user.id) is None


@allure.feature("User Manager")
@allure.story("Remove user - missing user")
def test_remove_missing_user(manager):
    with pytest.raises(ValueError):
        manager.remove_user(777)



@allure.feature("User Manager")
@allure.story("Get all users")
@pytest.mark.parametrize(
    "users",
    [
        [],
        [User(1, "Alex", 25, "alex@example.com")],
        [
            User(1, "Alex", 25, "alex@example.com"),
            User(2, "John", 30, "john@example.com"),
            User(3, "David", 20, "david@example.com")
        ],
    ]
)
def test_get_all_users(manager, users):
    for user in users:
        manager.add_user(user)

    result = manager.get_all_users()

    assert result == users
    


@allure.feature("User Manager")
@allure.story("Count users")
@pytest.mark.parametrize(
    "users, expected_count",
    [
        ([], 0),
        (
            [User(1, "Alex", 25, "alex@example.com")],
            1
        ),
        (
            [
                User(1, "Alex", 25, "alex@example.com"),
                User(2, "John", 30, "john@example.com"),
                User(3, "David", 20, "david@example.com")
            ],
            3
        ),
    ]
)
def test_count_users(manager, users, expected_count):
    for user in users:
        manager.add_user(user)

    result = manager.count_users()

    assert result == expected_count