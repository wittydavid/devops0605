print("Welcome to Lesson 1 - 06/05/2021")
print("Hello World!")
a = 4
print(a)
b = "David Askarian"
print(b)
# c is a list - list is mutable - we can change it dynamically
c = ["aaa", 4, True]
d = False
print(c)
print(c[2])
c[2] = "Moshe"
# e is a tuple - is immutable kind of a list but we cannot change it dynamically
e = ("aa", 2, "bbb")
print(c)
print(e)
person1 = ["David", "Askarian", 26, True]
person2 = {"fname": "David", "lname": "Askarian",
           "age": 26, "is_male": True}
print(person2["fname"])
print(person2.keys())
print(person2.values())
