size = 5

print("Using single for loop:")
for i in range(1, size + 1):
    draw = "*" * i
    print(draw)

print()

print("Using nested for loop:")
for i in range(size):
    draw = ""
    for j in range(size):
        if j <= i:
            draw = draw + "*"
    print(draw)
