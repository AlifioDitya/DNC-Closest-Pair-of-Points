# from module.Point import Point
from Point import Point
import random

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

# Test
# n = 10
# x = [random.randint(1, 100) for _ in range(n)]
# y = [random.randint(1, 100) for _ in range(n)]
# z = [random.randint(1, 100) for _ in range(n)]

# points = [Point(xi, yi, zi) for xi, yi, zi in zip(x, y, z)]

# print(quicksort(points, 0, len(points)-1))