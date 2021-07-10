from add_numbers import add_numbers


def get_numbers_and_add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return add_numbers(a, b)


print(get_numbers_and_add())
