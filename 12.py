def append_name(name):
    file_to_write = open("names.txt", "a")
    file_to_write.write(name + "\n")
    file_to_write.close()


def print_names(file_to_print):
    try:
        my_file = open(file_to_print, "r")
        for line in my_file.readlines():
            name = line.split(" ")[0]
            age = line.split(" ")[1].strip("\n")
            print(f"Hello {name}, you're {age}!")
    except FileNotFoundError as e:
        print("The file you are trying to read does not exist")


name_n_age = input("what is name and age")
append_name(name_n_age)
print_names("names.txt")
