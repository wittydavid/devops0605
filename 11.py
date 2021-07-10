# 27.05 class assignment 1 - add * alongside the word exception -> word *exception* word

my_file = open("read_my_contents.txt", "r")
for line in my_file.readlines():
    if "exception" in line:
        print(line, end='')
