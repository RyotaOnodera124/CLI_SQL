from db_config import UserInfo


def create_data():
    user_name = input("New user name > ")
    user_age = input("New user age > ")
    print(f"Add new user: {user_name}")
    UserInfo.create(name=user_name, age=user_age)


def read_all():
    userdates = UserInfo.select()
    for userdate in userdates:
        print(f"Name: {userdate.name} Age: {userdate.age}")


def main():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")
    print()
    while True:
        command = input("Your command > ")
        if command == "S" or command == "s":
            read_all()
            print()
        elif command == "A" or command == "a":
            create_data()
            print()
        elif command == "Q" or command == "q":
            print("Bye!")
            break
        else:
            print(f"{command}: command not found")
            print()


if __name__ == "__main__":
    main()
