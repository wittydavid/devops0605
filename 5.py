names = ["haim", "moshe", "david", "miki"]
# print(range(5))
# print(list(range(5)))
# print(list(range(2, 5)))
#
# #             start  end  step
# print(list(range(10, -5, -3)))

print(" --- separate 1 ---")

for i in range(len(names)):
    if i == 2:
        continue  # skip to next iteration
    print(f"hello {names[i]}")
else:  # this means -> perform this action if the loop finished iterating till the last object
    print("finished successfully!")

print(" --- separate 2 ---")

for i in range(len(names)):
    if i == 2:
        break  # stop and get out of the loop all together
    print(f"hello {names[i]}")

print(" --- separate 3 ---")

for name in names:
    print(f"hello {name}")

print(" --- separate 4 ---")

a = 0
while a < 5 and len(names) > 2:
    print("a is still less than 5")
    a = a + 1
else:
    print("finished successfully")

print(" --- separate 5 class exercise : 7 BOOM ---")

# for i in range(1, 101):
#     if i % 7 == 0:
#         continue
#     print(i)

j = 0
while j < 101:
    j = j + 1
    if j % 7 == 0:
        continue
    print(j)
