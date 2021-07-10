# 27.05 class challenge 1:
# add * alongside the word exception e.g word *exception* word

try:
    my_file = open("read_my_contents.txt", "r")
except FileNotFoundError as e:
    print(f"Error: {e.args}")
    print("The file you are trying to read does not exist")
else:
    for line in my_file.readlines():
        if "exception" in line:
            print(line.replace('exception', '*exception*'), end='')
