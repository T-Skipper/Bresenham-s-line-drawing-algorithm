print("Original Pixel(x, y) ")
x = int(input("x coordinate "))
y = int(input("y coordinate "))

print("\n\nDestinantion Pixel(j, k) ")
j = int(input("j coordinate "))
k = int(input("k coordinate "))

count = 0
axes = [[x, y]]

#   Obtain change in x and change in y respectively
dx = j - x
dy = k - y

#   Derive the Decision Parameter
p = 2*dy - dx

# Print the origin
print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

#   Store the co-ordinates in a list - Axes
while x != j and y != k:
    if p < 0:
        count += 1
        x += 1
        p = p + 2*dy
        axes.append([x, y])
        # print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

    else:
        count += 1
        x += 1
        y += 1
        p = p + 2*(dy - dx)
        axes.append([x, y])
        # print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

print(axes)