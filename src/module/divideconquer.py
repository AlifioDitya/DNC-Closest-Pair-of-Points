from module.Point import Point

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

