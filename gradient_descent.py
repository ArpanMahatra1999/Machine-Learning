# general variables
points = []
number_of_points = int(input("Enter how many points are there: "))

while number_of_points != 0:
    # new point
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    points.append((x, y))
    number_of_points -= 1

# gradient descent
iterations = 0
m, b = 0, 0
learning_rate = 0.02
last_cost = float('inf')
while iterations <= 1000:
    print(f"m: {m}, b: {b}, cost: {last_cost}, iteration: {iterations}")
    n = len(points)
    cost = 1/(2*n)*sum([point[1]-(m*point[0]+b) for point in points])
    if cost > last_cost:
        break
    dm = -(2/n)*sum([point[0]*(point[1]-(m*point[0]+b)) for point in points])
    db = -(2/n)*sum([point[1]-(m*point[0]+b) for point in points])
    m = m - learning_rate*dm
    b = b - learning_rate*db
    last_cost = cost
    iterations += 1
    
# equations
if b < 0:
    if m < 0:
        print(f"The equation of line of best fit by LLS is y={b}{m}x")
    elif m == 0:
        print(f"The equation of line of best fit by LLS is y={b}")
    else:
        print(f"The equation of line of best fit by LLS is y={b}+{m}x")
elif b == 0:
    if m < 0:
        print(f"The equation of line of best fit by LLS is y={m}x")
    elif m == 0:
        print(f"The equation of line of best fit by LLS is y=0")
    else:
        print(f"The equation of line of best fit by LLS is y={m}x")
else:
    if m < 0:
        print(f"The equation of line of best fit by LLS is y={b}{m}x")
    elif m == 0:
        print(f"The equation of line of best fit by LLS is y={b}")
    else:
        print(f"The equation of line of best fit by LLS is y={b}+{m}x")
