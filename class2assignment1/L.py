height = 7
width = 7

print("NOTE: You can change the drawing by playing with the height and width variables")
print("Have fun!")
for i in range(height):
    draw = ""
    for j in range(width):
        if i == j or i + j == height - 1:
            draw = draw + "*"
        else:
            draw = draw + " "
    print(draw)
