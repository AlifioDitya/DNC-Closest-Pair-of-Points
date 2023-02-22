from Point import Point

def main():
    oldPoint = Point(1,2,3)
    newPoint = Point(4,5,6)
    distance = newPoint.distance_to(oldPoint)
    print(distance)
    return

if __name__ == '__main__':
    main()
