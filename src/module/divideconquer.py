import time

def partition(points, low, high):
    """
    Divides a list of points by their x-axis.

    Parameters
    ----------
    points: a list of Point objects.
    low: Lower index of the partitioned list.
    high: Upper index of the partitioned list.

    Returns
    ----------
    i: Corrected index of pivot.
    """

    # Element to be placed in the correct position
    pivot = points[high]

    # Initialize the lower iterator
    i = low - 1

    # Loop the higher iterator through the list
    for j in range(low, high):

        # If element on the higher iterator index is smaller than pivot, put it on the 'left' of the list
        if (points[j][0] <= pivot[0]):
            # Increment lower iterator
            i += 1
            # Swap the point of smaller value to pivot with the lower iterator
            points[j], points[i] = points[i], points[j]
    
    # Swap the pivot on the right position in the list
    points[i+1], points[high] = points[high], points[i+1]

    # Returns the index of pivot
    return i+1

def quicksort(points, low, high):
    """
    Sorts every points in a list by their x-axis.

    Parameters
    ----------
    points: a list of Point objects.
    low: Lower index of the partitioned list.
    high: Upper index of the partitioned list.

    Returns
    ----------
    points: Points sorted by their x-axis in ascending order.
    """

    if low < high:
        # Get the index of pivot on partition
        idx = partition(points, low, high)

        # Sort the list on the left and right of partition point
        quicksort(points, low, idx-1)
        quicksort(points, idx+1, high)
    
    return points

# Versi Fio
def split_points(points, split, axis):
    """
    Splits points into two sections based off of an axis.

    Parameters
    ----------
    points: a list of Point objects
    split: Coordinate to split on
    axis: Dimension axis

    Returns
    ----------
    left: a list of points with coordinate on the left of split
    right: a list of points with coordinate on the right of split
    """

    left = []
    right = []

    for point in points:
        if point[axis] <= split:
            left.append(point)
        else:
            right.append(point)

    return left, right

def createDivide(points):
    """
    Calculate x coordinate to split a list of points to two list of points with the same amount

    Args:
        points : a list of Point objects

    Returns:
        x : Coordinate to split on
    """

    x = (points[len(points) // 2 - 1][0] + points[len(points) // 2][0]) / 2
    return x

# Versi Michael
def splitPoints(points):
    """
    Splits points into two sections based off of an axis.

    Args:
        points: a list of Point objects

    Returns:
        left_points : a list of Point objects with coordinate on the left of split
        right_points : a list of Point objects with coordinate on the right of split
        x : Coordinate to split on
    """

    x = createDivide(points)
    left_points = []
    right_points = []
    for point in points:
        if(point[0] <= x and len(left_points) < len(points) // 2):
            left_points.append(point)
        else:
            right_points.append(point)
    
    return left_points, right_points, x

def ClassifyPointsInStrip(left_p, right_p, x, temp_min):
    """
    Classify which points are inside of the strip zone

    Args:
        left_p : a list of Point objects with coordinate on the left of split
        right_p : a list of Point objects with coordinate on the right of split
        x : Coordinate to split on
        temp_min : The current minimum distance

    Returns:
        strip_points : a list of Point objects inside of the strip zone
    """

    left_strip_points = []
    i = len(left_p) - 1
    while(i >= 0 and abs(left_p[i][0] - x) <= temp_min):
        left_strip_points.append(left_p[i])
        i -= 1

    right_strip_points = []
    i = 0
    while(i < len(right_p) and abs(right_p[i][0] - x) <= temp_min):
        right_strip_points.append(right_p[i])
        i += 1

    return left_strip_points, right_strip_points

def findSmallerThanMinimumDistance(point1, point2, distance, count):
    """
    Finding smaller distance than the minimum distance inside the strip zone

    Args:
        point1 : a Point object
        point2 : a Point object
        distance : The current minimum distance

    Returns:
        boolean : True if smaller than the current minimum distance
        temp_distance : the new minimum distance
    """
    if(abs(point1[0] - point2[0]) <= distance or (len(point1) > 1 and abs(point1[1] - point2[1]) <= distance)):
        count[0] += 1
        temp_distance = point1.distance_to(point2)
        if(temp_distance < distance):
            return True, temp_distance
    
    return False, 0

def findClosestPairInStrip(left_p, right_p, x, temp_min, temp_pair, count):
    """
    Finding the smallest distance between points in the strip zone

    Args:
        left_p : a list of Point objects with coordinate on the left of split
        right_p : a list of Point objects with coordinate on the right of split
        x : Coordinate to split on
        temp_min : The current minimum distance

    Returns:
        new_min : New minimum distance
    """

    left_strip_points, right_strip_points = ClassifyPointsInStrip(left_p, right_p, x, temp_min)
    new_min = temp_min
    new_pair = temp_pair
    for point1 in left_strip_points:
        for point2 in right_strip_points:
            valid, newDistance = findSmallerThanMinimumDistance(point1, point2, new_min, count)
            if(valid):
                new_min = newDistance
                new_pair = (point1, point2)
    
    return new_min, new_pair

def findClosestPair(points, count):
    """
    Finding closest pair of points with divide and conquer

    Args:
        points : a list of Point objects

    Returns:
        distance : the smallest distance
    """
    if(len(points) <= 1):
        return -1, ()
    elif(len(points) == 2):
        count[0] += 1
        return points[0].distance_to(points[1]), (points[0], points[1])
    else:
        left_points, right_points, x = splitPoints(points)
        min_left, pair_left = findClosestPair(left_points, count)
        min_right, pair_right = findClosestPair(right_points, count)
        temp_min = min_left if min_left < min_right and min_left >= 0 else min_right
        new_pair = pair_left if min_left < min_right and min_left >= 0 else pair_right
        min_strip, pair_strip = findClosestPairInStrip(left_points, right_points, x, temp_min, new_pair, count)
        if(min_strip < temp_min):
            return min_strip, pair_strip
        else:
            return temp_min, new_pair

def run_divide_and_conquer_closest_pair(points, answer):
    # Divide And Conquer Algorithm
    start_time = time.time()
    points = quicksort(points, 0 , len(points) - 1)
    ed_count = [0]
    min_distance, pair = findClosestPair(points, ed_count)
    end_time = time.time()

    # Output
    # Closest Pair and Their Distance
    output = "First Point: " + str(pair[0]) + "\n" + "Second Point: " + str(pair[1]) + "\n" + f"Minimum Distance: {min_distance}\n" + "Euclidian Calculation Count: " + str(ed_count[0]) + "\n" + f"Execution Time: {(end_time - start_time) * 1000} ms\n"
    answer.set(output)