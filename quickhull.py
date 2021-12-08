from helpers import *

def quickhull(points, num_points):
    """
    The main function for calculating the convex hull using the divide and conquer approach of the
    quickhull algorithm.
    """

    # The solutuion of the quickhull algorithm is stored as a set of points.
    solution = set()

    # Finds the index of the leftmost and rightmost points in the original set.
    left_point_index, right_point_index = locate_starting_points(points, num_points)

    # Add points recursively on one side of the two starting point.
    add_point(points     = points,
              num_points = num_points,
              point_1    = points[left_point_index],
              point_2    = points[right_point_index],
              solution   = solution,
              side       = 1)

    # Add points recursively on the other side of the two starting point.
    add_point(points     = points,
              num_points = num_points,
              point_1    = points[left_point_index],
              point_2    = points[right_point_index],
              solution   = solution,
              side       = -1)

    return solution

def locate_starting_points(points, num_points):
    """
    Finds the index of the leftmost and rightmost points in the original set from which the
    quickhull algorithm starts with to recursively find the rest of the points in the convex hull
    solution.
    """

    left_point_index = 0
    right_point_index = 0

    # Iterate through all points in the original set updating the leftmost and rightmost points if
    # a more extreme point is found.
    for i in range(0, num_points):
        if (points[i].x < points[left_point_index].x):
            left_point_index = i
        if (points[i].x > points[right_point_index].x):
            right_point_index = i

    return left_point_index, right_point_index

def locate_side(point_1, point_2, point):
    """Locates which side a point is from the original leftmost and rightmost starting points."""

    side = (point.y - point_1.y) * (point_2.x - point_1.x) - (point_2.y - point_1.y) * (point.x - point_1.x)

    if side > 0:
        return 1
    else:
        return -1

def distance_to_line(point_1, point_2, point):
    """Finds the distance a points is from the original leftmost and rightmost starting points."""

    return abs((point.y - point_1.y) * (point_2.x - point_1.x) - (point_2.y - point_1.y) * (point.x - point_1.x))

def add_point(points, num_points, point_1, point_2, solution, side):
    """
    Recursive function to keep adding points to the convex hull set until no more points are left.
    """

    index = -1
    max_distance = 0

    for i, point in enumerate(points):

        # Find the distance to the line between the two points.
        point_distance = distance_to_line(point_1, point_2, point)

        # Update the index of the next point to be added to the solution.
        if locate_side(point_1, point_2, point) == side and point_distance > max_distance:
            index = i
            max_distance = point_distance

    # Termination condition.
    # Add the two points once there are no more points to add.
    if index == -1:
        solution.add((point_1.x, point_1.y))
        solution.add((point_2.x, point_2.y))
        return

    # Recursively add points to the convex hull solution.
    add_point(points     = points,
              num_points = num_points,
              point_1    = points[index],
              point_2    = point_1,
              solution   = solution,
              side       = locate_side(points[index], point_2, point_1))

    add_point(points     = points,
              num_points = num_points,
              point_1    = points[index],
              point_2    = point_2,
              solution   = solution,
              side       = locate_side(points[index], point_1, point_2))

if __name__ == '__main__':

    # Points read from a file and stored in a list of Point objects.
    #points = read_points_file('points.csv')

    # Points generated randomonly within a specific range.
    points = generate_points(num_points=15, scope=100)

    # Determines the number of points in the set. Calculated here as this number is used
    # many times during the quickhull algorithm. 
    num_points = len(points)

    # Quickhull function returns the solution as a set of points.
    solution = quickhull(points, num_points)

    # Print results and display in a graph.
    display_solution(points, solution)
