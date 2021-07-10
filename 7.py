# Don't define global objects and using them inside functions
# This creates strong link between the function and it's main program

# use _print prefix to functions that you want to purposefully to print something
def square(number):
    result = number * number
    return result


def mul_and_sum1(a, b):
    mul = a * b
    sum1 = a + b
    return mul, sum1


def mul_and_sum1_dict(a, b):
    mul = a * b
    sum1 = a + b
    return {"mul": mul, "sum1": sum1}


# program starts here
a = square(20)
print(a)

print("--- 1 separation ---")

result = mul_and_sum1(5, 7)
print(result)

print("--- 2 separation ---")

result2 = mul_and_sum1_dict(5, 7)
print(type(result2))
print(result2)
print(str(result2["mul"]))

print("--- 3 separation ---")
# my_name = input("enter name: ")
# print("hello " + my_name)

print("--- 4 separation class excise 2 ---")


def get_list_length(my_list):
    if type(my_list) == list:
        return len(my_list)
    else:
        return -1


def get_list_length_mine(my_list):
    count = 0
    if type(my_list) == list:
        for item in my_list:
            count = count + 1
    else:
        return -1
    return count


# {‘name’: String, ‘age’: Number, ‘Hobbies’: List}
def verify_dict_format(my_dict):
    if type(my_dict) != dict:
        return -1
    else:
        for item in my_dict:
            print(item)


some_list = [1, 2, 3, 3, 3, 3, 3, 3, 3]
print(get_list_length(some_list))
print(get_list_length_mine(some_list))
