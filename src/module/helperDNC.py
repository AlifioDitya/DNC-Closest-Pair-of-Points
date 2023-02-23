from Point import Point
import random

def createDivide(points):
    # I.S Array of point sudah terurut
    x = (points[len(points) // 2 - 1][0] + points[len(points) // 2 ][0]) / 2
    return x

def splitPoints(points):
    x = createDivide(points)
    left_points = []
    right_points = []
    for point in points:
        if(point[0] <= x):
            left_points.append(point)
        else:
            right_points.append(point)
    
    return left_points, right_points

"""n = 8
x = [random.randint(1, 100) for _ in range(n)]
y = [random.randint(1, 100) for _ in range(n)]
z = [random.randint(1, 100) for _ in range(n)]

points = [Point(xi, yi, zi) for xi, yi, zi in zip(x, y, z)]

print(createDivide(points))
print(splitPoints(points))"""