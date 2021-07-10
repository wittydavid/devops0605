import requests

print("hello")

try:
    requests.get("httos://github.com")
# Specific exceptions
except requests.exceptions.InvalidSchema as e:
    print("Schema is not ok")
except requests.exceptions.ConnectionError as e:
    print("Connection Error")
# Basic exceptions
except BaseException as e:
    print(e.args)

print("I'm still here ")


def get_age_from_user():
    age = int(input("Enter your age: "))
    if age < 0:
        # raise ValueError("age can not be negative")
        raise ValueError({"name": "David", "how": "Like that"})
    print("Your age is " + str(age))


try:
    get_age_from_user()
except ValueError as e:
    print(e.args)
