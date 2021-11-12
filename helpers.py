
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