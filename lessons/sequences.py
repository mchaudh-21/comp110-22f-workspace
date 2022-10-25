"""notes and examples of tuple and range sequence types"""

from tracemalloc import start


Point2d = tuple[float, float]

start_position: Point2d = (5.0, 10.0, 3.0)

print(start_position)