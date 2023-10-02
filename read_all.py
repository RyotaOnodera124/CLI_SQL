from db_config import UserInfo


def read_all():
    userdates = UserInfo.select()
    for userdate in userdates:
        print(f"Name: {userdate.name} Age: {userdate.age}")


if __name__ == "__main__":
    read_all()
