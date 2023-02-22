from module.Point import Point
import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def brute_force_closest_pair(space):
    """
    Finds the closest pair of points in R^n Euclidean space using brute force algorithm. 
    
    Parameters
    ----------
    space: List of Point objects.

    Returns
    ----------
    pair: a list containing a pair of Point objects with the closest distance.
    """

    # If the list contains two points or less, by definition contains the closest pair
    if (len(space) <= 2):
        return space
    
    # Initialize the list of pair and minimum distance
    min_distance = space[0].distance_to(space[1])
    pair = [space[0], space[1]]

    # Brute force by checking distance to each other for each points in space
    for point1 in space:
        for point2 in space:
            if point1.distance_to(point2) < min_distance and point1 != point2:
                min_distance = point1.distance_to(point2)
                pair = [point1, point2]

    return pair
    

def run_brute_force_closest_pair(answer):
    # Generate random 3D data
    n = 100
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)

    # Pack the data into Point objects
    points = [Point(xi, yi, zi) for xi, yi, zi in zip(x, y, z)]

    # Brute Force Algorithm
    start_time = time.time()
    p1, p2 = brute_force_closest_pair(points)
    end_time = time.time()

    # Output
    # Closest Pair and Their Distance
    output = "First Point: " + str(p1) + "\n\n" + "Second Point: " + str(p2) + "\n\n" + f"Minimum Distance: {p1.distance_to(p2)}\n\n" + "Euclidian Calculation Count: " + str((n-1) * n / 2) + "\n\n" + f"Execution Time: {(end_time - start_time) * 1000} ms\n\n"
    answer.set(output)

    # Create a 3D scatter plot
    figure = plt.figure(figsize=(6, 6))
    ax = figure.add_subplot(111, projection='3d')

    # Filter points
    x = [p[0] for p in points if p != p1 and p != p2]
    y = [p[1] for p in points if p != p1 and p != p2]
    z = [p[2] for p in points if p != p1 and p != p2]

    # Scatter plot
    ax.scatter(x, y, z, alpha=0.25)
    ax.scatter(p1[0], p1[1], p1[2])
    ax.scatter(p2[0], p2[1], p2[2])

    # Set the axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plot a line between the two points
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], "Red")

    # Show the plot
    ax.set_title("3D Scatter Plot")
    plt.show()