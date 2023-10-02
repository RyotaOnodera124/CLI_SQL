from db_config import UserInfo


def create_data():
    user_name = input("New user name > ")
    user_age = input("New user age > ")
    print(f"Add new user: {user_name}")
    UserInfo.create(name=user_name, age=user_age)


if __name__ == "__main__":
    create_data()
