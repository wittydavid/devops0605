# Appending my name to file - words.txt
my_file = open("words.txt", "a", encoding="utf_8")
# my_file = open("words.txt", "a")  # <- also works by default. The default encoding is platform dependent
my_file.write("דוד" + "\n")
my_file.close()
