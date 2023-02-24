import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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
    

def run_brute_force_closest_pair(points, answer, canvas, is3D):
    """
    Run brute force algorithm to solve the closest pair of points problem and display solution on GUI

    Args:
        points (list): list of point objects
        answer (string): solution
        canvas (widget): widget to display plot on GUI
        is3D (boolean): check if the points can be plotted or not
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
    
    # If the dimension below or equal to 3
    if(is3D):
        # Create a 3D scatter plot
        figure = plt.figure(figsize=(6, 6))
        ax = figure.add_subplot(111, projection='3d')

        # Filter points
        x = [p[0] for p in points if p != p1 and p != p2]
        if(len(p1) >= 2):
            y = [p[1] for p in points if p != p1 and p != p2]
        if(len(p1) >= 3):
            z = [p[2] for p in points if p != p1 and p != p2]

        # Scatter plot
        if(len(p1) == 1):
            ax.scatter(x, 0, 0, alpha=0.25)
        elif(len(p1) == 2):
            ax.scatter(x, y, 0, alpha=0.25)
        else:
            ax.scatter(x, y, z, alpha=0.25)
        
        if(len(p1) == 1):
            ax.scatter(p1[0], 0, 0)
            ax.scatter(p2[0], 0, 0)
        elif(len(p1) == 2):
            ax.scatter(p1[0], p1[1], 0)
            ax.scatter(p2[0], p2[1], 0)
        else:
            ax.scatter(p1[0], p1[1], p1[2])
            ax.scatter(p2[0], p2[1], p2[2])

        # Set the axis labels
        ax.set_xlabel('X')
        if(len(p1) >= 2):
            ax.set_ylabel('Y')
        if(len(p1) >= 3):
            ax.set_zlabel('Z')

        # Plot a line between the two points
        if(len(p1) == 1):
            ax.plot([p1[0], p2[0]], [0, 0], [0, 0], "Red")
        elif(len(p1) == 2):
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [0, 0], "Red")
        else:
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], "Red")

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