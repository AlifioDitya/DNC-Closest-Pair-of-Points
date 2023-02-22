from Point import Point

def test():
    oldPoint = Point(1,2,3)
    newPoint = Point(4,5,6)
    distance = newPoint.distance_to(oldPoint)
    print(distance)
    return
