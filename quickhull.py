class Point:
    """
    Define the class of a 2D point.
    """
    def __init__(self, x, y):
        self.x = x  # The coordinate on x-axis.
        self.y = y  # The coordinate on y-axis.
        #self.label = label  # The name of the point.

def locate_side(point_1, point_2, point):
    val = (point.y - point_1.y) * (point_2.x - point_1.x) - (point_2.y - point_1.y) * (point.x - point_1.x)

    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def distance_to_line(point_1, point_2, point):
    return abs((point.y - point_1.y) * (point_2.x - point_1.x) - (point_2.y - point_1.y) * (point.x - point_1.x))

def quickhull(points, n, point_1, point_2, side):
    ind = -1
    max_distance = 0

    for i in range(0, n):
        temp = distance_to_line(point_1, point_2, points[i])

        if (locate_side(point_1, point_2, points[i]) == side and temp > max_distance):
            ind = i
            max_distance = temp

    if ind == -1:
        hull.add((point_1.x, point_1.y))
        hull.add((point_2.x, point_2.y))
        return

    quickhull(points, n, points[ind], point_1, -locate_side(points[ind], point_1, point_2))
    quickhull(points, n, points[ind], point_2, -locate_side(points[ind], point_2, point_1))

def locate_starting_points(points, n):
    min_x = 0
    max_x = 0

    for i in range(1, n):
        if (points[i].x < points[min_x].x):
            min_x = i
        if (points[i].x > points[max_x].x):
            max_x = i

    return min_x, max_x

def display_hull(hull, n):
    if (n < 3):
        print('Convex hull not possible.')

    min_x, max_x = locate_starting_points(points, n)

    quickhull(points, n, points[min_x], points[max_x], 1)

    quickhull(points, n, points[min_x], points[max_x], -1)

    print('The points in Convex Hull are: ')
    for point in hull:
        print(point[0], point[1])

def create_point_objects(points):
    point_objects = []
    for point in points:
        point_objects.append(Point(point[0], point[1]))

    return point_objects

hull = set()
points = [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]
points = create_point_objects(points)
n = len(points)
display_hull(hull, n)
