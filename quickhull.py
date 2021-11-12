import csv

from point import Point
from helpers import locate_side, distance_to_line

def read_points_file(file_name):
    """
    """
    points = []
    with open(file_name) as points_file:
        points_reader = csv.reader(points_file)
        for point in points_reader:
            x, y = float(point[0]), float(point[1])
            label = point[2]
            points.append(Point(x, y, label))

    if (len(points) < 3):
        exit('Convex solution not possible, there must be at least 3 points.')

    return points

def quickhull(solution, num_points):
    """
    """

    # The solutuion by the quickhull algorithm is stored as a set of points.
    solution = set()

    left_point_index, right_point_index = locate_starting_points(points, num_points)

    add_point(points, num_points, points[left_point_index], points[right_point_index], solution, 1)
    add_point(points, num_points, points[left_point_index], points[right_point_index], solution, -1)

    return solution

def locate_starting_points(points, num_points):
    """
    """
    left_point_index = 0
    right_point_index = 0

    for i in range(0, num_points):
        if (points[i].x < points[left_point_index].x):
            left_point_index = i
        if (points[i].x > points[right_point_index].x):
            right_point_index = i

    return left_point_index, right_point_index

def add_point(points, num_points, point_1, point_2, solution, side):
    """
    """
    ind = -1
    max_distance = 0

    for i in range(0, num_points):
        point_distance = distance_to_line(point_1, point_2, points[i])

        if (locate_side(point_1, point_2, points[i]) == side and point_distance > max_distance):
            ind = i
            max_distance = point_distance

    if ind == -1:
        solution.add((point_1.x, point_1.y))
        solution.add((point_2.x, point_2.y))
        return

    add_point(points, num_points, points[ind], point_1, solution, -locate_side(points[ind], point_1, point_2))
    add_point(points, num_points, points[ind], point_2, solution, -locate_side(points[ind], point_2, point_1))

if __name__ == '__main__':

    # Points read from a file and stored in a list of Point objects.
    points = read_points_file('points.csv')

    # Determines the number of points in the set. Calculated here as this number is used
    # many times during the quickhull algorithm. 
    num_points = len(points)

    # Quickhull function returns the solution as a set of points.
    solution = quickhull(points, num_points)

    print('The points in Convex solution are: ')
    for point in solution:
        print(point[0], point[1])
