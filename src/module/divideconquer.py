import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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

    # Calculate the middle x coordinate to split the points
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

    # Divide points into left and right zone with each contains half size of the initial size
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
        left_strip_points : a list of Point objects inside of the left strip zone
        right_strip_points : a list of Point objects inside of the right strip zone
    """

    # Classifying points into left and right strip zone
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
        count : euclidean calculation count

    Returns:
        boolean : True if smaller than the current minimum distance
        temp_distance : the new minimum distance
    """

    # Checking if point1 and point2 have smaller distance than the current minimum distance
    check = 0
    threshold = distance ** 2
    for i in range (len(point1)):
        check += (abs(point1[i] - point2[i]) ** 2)
        if(check > threshold):
            return False, 0
    
    # Calculate euclidean distance
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
        temp_pair : The current closest pair of point

    Returns:
        new_min : New minimum distance
        new_pair : New closest pair of point
    """

    # Classify points into left and right strip zone
    left_strip_points, right_strip_points = ClassifyPointsInStrip(left_p, right_p, x, temp_min)
    
    # Initialize the current minimum distance and the closest pair
    new_min = temp_min
    new_pair = temp_pair

    # Finding pair of points that are more closer than the initial pair
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
        count : euclidean calculation count

    Returns:
        distance : the smallest distance
        pair : pair of points with the smallest distance
    """

    # Handle case for n != 2^k
    if(len(points) <= 1):
        return -1, ()
    # Base Recurrens
    elif(len(points) == 2):
        count[0] += 1
        return points[0].distance_to(points[1]), (points[0], points[1])
    else:
        # Splitting Points
        left_points, right_points, x = splitPoints(points)

        # Finding closest pair of points on the left side
        min_left, pair_left = findClosestPair(left_points, count)

        # Finding closest pair of points on the right side
        min_right, pair_right = findClosestPair(right_points, count)

        # Find the minimum distance and closest pair of points between left side and right side
        temp_min = min_left if min_left < min_right and min_left >= 0 else min_right
        new_pair = pair_left if min_left < min_right and min_left >= 0 else pair_right
        
        # Find the minimum distance and closest pair of points between the strip zone
        min_strip, pair_strip = findClosestPairInStrip(left_points, right_points, x, temp_min, new_pair, count)
        
        # Return the minimum distance and the closest pair of points
        if(min_strip < temp_min):
            return min_strip, pair_strip
        else:
            return temp_min, new_pair

def run_divide_and_conquer_closest_pair(points, answer, canvas, is3D):
    """
    Run divide and conquer algorithm to the closest pair of points problem and display the solution on GUI

    Args:
        points (list): list of point objects
        answer (string): solution
        canvas (widget): widget to display plot on GUI
        is3D (boolean): check if the points can be plotted or not
    """

    # Divide And Conquer Algorithm
    start_time = time.time()
    points = quicksort(points, 0 , len(points) - 1)
    ed_count = [0]
    min_distance, pair = findClosestPair(points, ed_count)
    end_time = time.time()

    # Output
    # Closest Pair and Their Distance
    output = "First Point: " + str(pair[0]) + "\n" + "Second Point: " + str(pair[1]) + "\n" + f"Minimum Distance: {min_distance}\n" + "Euclidean Calculations Done: " + str(ed_count[0]) + "\n" + f"Execution Time: {(end_time - start_time) * 1000} ms\n"
    answer.set(output)

    # If the dimension below or equal to 3
    if(is3D):
        # Create a 3D scatter plot
        figure = plt.figure(figsize=(6, 6))
        ax = figure.add_subplot(111, projection='3d')

        # Filter points
        x = [p[0] for p in points if p != pair[0] and p != pair[1]]
        if(len(pair[0]) >= 2):
            y = [p[1] for p in points if p != pair[0] and p != pair[1]]
        if(len(pair[0]) >= 3):
            z = [p[2] for p in points if p != pair[0] and p != pair[1]]

        # Scatter plot
        if(len(pair[0]) == 1):
            ax.scatter(x, 0, 0, alpha=0.25)
        elif(len(pair[0]) == 2):
            ax.scatter(x, y, 0, alpha=0.25)
        else:
            ax.scatter(x, y, z, alpha=0.25)
        
        if(len(pair[0]) == 1):
            ax.scatter(pair[0][0], 0, 0)
            ax.scatter(pair[1][0], 0, 0)
        elif(len(pair[0]) == 2):
            ax.scatter(pair[0][0], pair[0][1], 0)
            ax.scatter(pair[1][0], pair[1][1], 0)
        else:
            ax.scatter(pair[0][0], pair[0][1], pair[0][2])
            ax.scatter(pair[1][0], pair[1][1], pair[1][2])

        # Set the axis labels
        ax.set_xlabel('X')
        if(len(pair[0]) >= 2):
            ax.set_ylabel('Y')
        if(len(pair[0]) >= 3):
            ax.set_zlabel('Z')

        # Plot a line between the two points
        if(len(pair[0]) == 1):
            ax.plot([pair[0][0], pair[1][0]], [0, 0], [0, 0], "Red")
        elif(len(pair[0]) == 2):
            ax.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], [0, 0], "Red")
        else:
            ax.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], [pair[0][2], pair[1][2]], "Red")

        # Set Plot Title
        ax.set_title("3D Scatter Plot")

        # Destroy last plot
        if output:
            for child in canvas.winfo_children():
                child.destroy()
        output = None
        
        # Show the plot
        output = FigureCanvasTkAgg(figure, master = canvas)
        output.draw()
        toolbar = NavigationToolbar2Tk(output,
                                    canvas)
        toolbar.update()
        output.get_tk_widget().pack()

    else: # Destroy last plot if exists
        if output:
            for child in canvas.winfo_children():
                child.destroy()
        output = None