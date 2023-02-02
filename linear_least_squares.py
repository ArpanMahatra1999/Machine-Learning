# general variables
points = []
number_of_points = int(input("Enter how many points are there: "))

while number_of_points != 0:
    # new point
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    points.append((x, y))
    number_of_points -= 1

# summations
sum_x, sum_y, sum_xy, sum_x2 = 0, 0, 0, 0
for point in points:
    sum_x += point[0]
    sum_y += point[1]
    sum_xy += (point[0] * point[1])
    sum_x2 += pow(point[0], 2)

print(sum_x, sum_y, sum_xy, sum_x2)
# slope b2 and bias b1
b2 = (sum_x * sum_y - 4 * sum_xy) / (pow(sum_x, 2) - 4 * sum_x2)
b1 = (sum_xy - sum_x2 * b2) / sum_x

# equations
if b1 < 0:
    if b2 < 0:
        print(f"The equation of line of best fit by LLS is y={b1}{b2}x")
    elif b2 == 0:
        print(f"The equation of line of best fit by LLS is y={b1}")
    else:
        print(f"The equation of line of best fit by LLS is y={b1}+{b2}x")
elif b1 == 0:
    if b2 < 0:
        print(f"The equation of line of best fit by LLS is y={b2}x")
    elif b2 == 0:
        print(f"The equation of line of best fit by LLS is y=0")
    else:
        print(f"The equation of line of best fit by LLS is y={b2}x")
else:
    if b2 < 0:
        print(f"The equation of line of best fit by LLS is y={b1}{b2}x")
    elif b2 == 0:
        print(f"The equation of line of best fit by LLS is y={b1}")
    else:
        print(f"The equation of line of best fit by LLS is y={b1}+{b2}x")

# sum of square of residuals
ssr = sum([pow(point[1] - (b1 + b2 * point[0]), 2) for point in points])
print(f"The SSR value is {ssr:.2f} .")
