import math
from shapely.geometry import *
            
def angle(p0: Point, p1: Point, p2: Point) -> float:
    """p1 is the center point; result is in degrees."""
    a = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
    b = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    c = (p2.x-p0.x)**2 + (p2.y-p0.y)**2
    return round(math.acos( (a+b-c) / math.sqrt(4*a*b) ) * 180/math.pi, 5)

def extrapolate(p0: Point, p1: Point, ratio: float =2.0) -> Point:
    """Returns the end of extrapolated line."""
    x = p0.x + ratio * (p1.x - p0.x)
    y = p0.y + ratio * (p1.y - p0.y)
    return Point(x, y)

def which_side(p0: Point, p1: Point, p2: Point) -> str:
    """Returns side of point 'p2' from 'p0->p1' line""" 
    is_left = ((p1.x-p0.x)*(p2.y-p0.y)-(p1.y-p0.y)*(p2.x-p0.x)) > 0
    return 'left' if is_left else 'right'

def which_side_line(line: LineString, point: Point) -> str:
    """Returns side of point from line"""
    segment_distances = []
    for coords in zip(line.coords[:-1], line.coords[1:]):
        distance = LineString(coords).distance(point)
        segment_distances.append((distance, coords))
    _, (a, b) = min(segment_distances)
    return which_side(Point(a), Point(b), point)

if __name__ == '__main__':
    assert angle(Point(0, 0), Point(1, 1), Point(1, 0)) == 45
    assert extrapolate(Point(0, 0), Point(1, 1), ratio=2) == Point(2, 2)
    assert which_side(Point(0, 0), Point(1, 1), Point(1, 0)) == 'right'
    assert which_side(Point(0, 0), Point(1, 1), Point(0, 1)) == 'left'
    assert which_side_line(LineString([(0, 0), (1, 1)]), Point(1, 0)) == 'right'
    assert which_side_line(LineString([(0, 0), (1, 1)]), Point(0, 1)) == 'left'
    print('OK!')