# Reading and printing contents of words.txt
try:
    my_file = open("words.txt", "r")
    for line in my_file.readlines():
        print_line = line.strip("\n")
        print(f"{print_line}")
    my_file.close()
except FileNotFoundError as e:
    print(f"Error: {e.args}")
    print("The file you are trying to read does not exist")
