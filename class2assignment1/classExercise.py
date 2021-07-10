def get_list_length(my_list):
    """
    This function does cool things
    :param my_list: User defined list
    :return: Number of items in the list, -1 if not list
    """
    if type(my_list) == list:
        return len(my_list)
    else:
        return -1


def get_list_length_mine(my_list):
    """
    This function does cool things
    :param my_list: User defined list
    :return: Number of items in the list, -1 if not list
    """
    count = 0
    if type(my_list) == list:
        for item in my_list:
            count = count + 1
    else:
        return -1
    return count


def verify_dict_format(my_dict):
    """
    Function checks if a given dictionary has the following format -
    {"name": <String>, "age": <Number>, "Hobbies": <List>}
    :param my_dict: User defined dictionary
    :return: -1 if correct
    """
    if type(my_dict) != dict:
        return -1
    else:
        if ((type(my_dict["name"]) == str) and
                (type(my_dict["age"]) == int or type(my_dict["age"]) == float) and
                (type(my_dict["Hobbies"]) == list)):
            print("Format is correct")
            return 1
        else:
            print("Format is not correct")
            return 0


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list_2 = [1, 2, 3, 4, 5, 6, 7]
some_list_3 = [1, 2, 3, 4, 5]

print("--- Length tester ---")
print("--- test 1 ---")
print(get_list_length(some_list))
print(get_list_length_mine(some_list))
print("--- test 2 ---")
print(get_list_length(some_list_2))
print(get_list_length_mine(some_list_2))
print("--- test 3 ---")
print(get_list_length(some_list_3))
print(get_list_length_mine(some_list_3))

print("--- Dictionary format checker ---")
some_dict = {"name": "String", "age": 1, "Hobbies": [1, 2]}
print(bool(verify_dict_format(some_dict)))
some_dict_2 = {"name": "String", "age": "hello", "Hobbies": [1, 2]}
print(bool(verify_dict_format(some_dict_2)))
