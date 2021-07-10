isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if isTrue == False and a == 2:
    print("Hello world!")

if strOne != "Two" or (strThree == "Three" and isTrue == False) and a == 2:
    print("hey")

if not b == 2.5:
    print("b is not 2.5")

if a < 2 and b > 2.5:
    print("hey")

if 1 <= b <= 100:
    print("b is between 1 and 100")

if a == 2.6:
    print("hey")
elif a == 2.7:
    print("hey")
elif a == 2.8:
    print("hey")
else:
    print("no hey")

print(a == 2)

# option 1
names = ["david", "adam", "john"]
my_name = "adam"
if my_name in names:
    print(f"{my_name} is in the list")
else:
    print(f"{my_name} NOT in list")

# option 2
print(f"is the name in? {my_name in names}")

print("--- first separation ---")

c = [1, 2, 3]
d = [1, 2, 3]
e = c
f = 5
g = 5
print(c == d)
print(c is d)
print(e is c)
# notice that this is is not the same as the previous one.
# this is because in this case these are "primitive"
# variables so python looks at the same memory area.
print(f is g)
print(type(f) is str)

print("--- second separation ---")

h = [1, 2, 3]
i = []
if h:
    print("h has elements")
if i:
    print("i has elements")

if len(h):
    print(f"h has {len(h)} elements")

print("--- third separation ---")

first_array = []
if first_array and first_array[2] == 1:
    print("banana!")
else:
    print("no banana :(")