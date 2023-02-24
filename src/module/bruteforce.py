import time

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
    pair = (space[0], space[1])

    # Brute force by checking distance to each other for each points in space
    for i in range (len(space)):
        for j in range (i + 1, len(space)):
            if space[i].distance_to(space[j]) < min_distance:
                min_distance = space[i].distance_to(space[j])
                pair = (space[i], space[j])

    return pair
    

def run_brute_force_closest_pair(points, answer):
    """
    Run brute force algorithm to solve the closest pair of points problem and display solution on GUI

    Args:
        points (list): list of point objects
        answer (string): solution
    """

    # Defining n
    n = len(points)

    # Brute Force Algorithm
    start_time = time.time()
    p1, p2 = brute_force_closest_pair(points)
    end_time = time.time()

    # Output
    # Closest Pair and Their Distance
    output = "First Point: " + str(p1) + "\n" + "Second Point: " + str(p2) + "\n" + f"Minimum Distance: {p1.distance_to(p2)}\n" + "Euclidean Calculations Done: " + str(int((n-1) * n / 2)) + "\n" + f"Execution Time: {(end_time - start_time) * 1000} ms\n"
    answer.set(output)