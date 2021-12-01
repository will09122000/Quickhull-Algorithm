import csv
import matplotlib.pyplot as plt
from random import randint

from point import Point

def read_points_file(file_name):
    """Reads a points csv file and loads as a set of Point objects."""

    points = []

    with open(file_name) as points_file:
        points_reader = csv.reader(points_file)

        # Iterate through each line in the file.
        for point in points_reader:
            x, y = float(point[0]), float(point[1])

            # Create the Point object and add it to the list.
            points.append(Point(x, y))

    if (len(points) < 3):
        exit('Convex solution not possible, there must be at least 3 points.')

    return points

def generate_points(num_points, scope):
    """Generate a list of points of length 'num_points' within a certain scope, e.g. 100x100."""

    points = []

    for _ in range(0, num_points):

        # Create random X and Y coordinates within the scope.
        x, y = randint(0, scope), randint(0, scope)

        # Create the Point object and add it to the list.
        points.append(Point(x, y))

    return points

def display_solution(points, solution):
    """
    Prints the set of solution points and displays the solution as red points with all remaining
    points shown as blue. Can't easily create lines between the solution points without additional
    processing as they are not ordered.
    """

    # Prints the solution
    print('The points in Convex solution are: ')
    for point in solution:
        print('(' + str(point[0]) + ', ' + str(point[1]) + ')')

    fig = plt.figure('Quickhull Algorithm Solution')
    ax = fig.add_subplot(111)

    # Points within convex hull (blue).
    plt.plot([point.x for point in points], [point.y for point in points], 'bo')

    # Points that make up convex hull (red).
    plt.plot([point[0] for point in solution], [point[1] for point in solution], 'ro')

    # Add the name of points to the figure.
    for point in points:
        ax.annotate(str(point.x) + ', ' + str(point.y), xy=(point.x, point.y))

    plt.axis('off')
    plt.show()
