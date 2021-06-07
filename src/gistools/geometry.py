from typing import Iterable, List, Callable

import math
from geopy.distance import great_circle
from shapely.geometry import *
            
def angle(p0: Point, p1: Point, p2: Point) -> float:
    """
    p1 is the center point; result is in degrees
    """
    a = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
    b = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    c = (p2.x-p0.x)**2 + (p2.y-p0.y)**2
    return round(math.acos( (a+b-c) / math.sqrt(4*a*b) ) * 180/math.pi, 5)

def extrapolate(p0: Point, p1: Point, ratio: float =2.0) -> Point:
    """
    Returns the end of extrapolated line.
    """
    x = p0.x + ratio * (p1.x - p0.x)
    y = p0.y + ratio * (p1.y - p0.y)
    return Point(x, y)

def which_side(p0: Point, p1: Point, p2: Point) -> str:
    """
    Returns side of point 'p2' from 'p0->p1' line
    """ 
    is_left = ((p1.x-p0.x)*(p2.y-p0.y)-(p1.y-p0.y)*(p2.x-p0.x)) > 0
    return 'left' if is_left else 'right'

def which_side_line(line: LineString, point: Point) -> str:
    """
    Returns side of point from line
    """
    segment_distances = []
    for coords in zip(line.coords[:-1], line.coords[1:]):
        distance = LineString(coords).distance(point)
        segment_distances.append((distance, coords))
    _, (a, b) = min(segment_distances)
    return which_side(Point(a), Point(b), point)

def chain(points: Iterable[Point], dist: Callable=Point.distance) -> List[Point]:
    """
    Sorting points in ordered seqsequence
    """
    def closest(p):
        return min((dist(p, _p), i) for i, _p in enumerate(points))
    points = [Point(p) for p in points]
    sequence = [points.pop()]
    while points:
        start, end = sequence[0], sequence[-1]
        closest_start = closest(start)
        closest_end = closest(end)
        if closest_start < closest_end:
            _, idx = closest_start
            sequence.reverse()
        else:
            _, idx = closest_end    
        sequence.append(points.pop(idx))
    return sequence

def haversine(p0: Point, p1: Point, lonlat: bool = True, unit: str = 'm'):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Radius of earth
    order = -1 if lonlat else 1
    c0 = p0.coords[0][::order]
    c1 = p1.coords[0][::order]
    distance = great_circle(c0, c1)
    return getattr(distance, unit)

if __name__ == '__main__':
    pass