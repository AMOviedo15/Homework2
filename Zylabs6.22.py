#Aaron Oviedo #1990958

x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())

solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if x1 * x + y1 * y == z1 and x2 * x + y2 * y == z2:
            print(x, y)
            solution = True

if solution != True:
    print("No solution")



