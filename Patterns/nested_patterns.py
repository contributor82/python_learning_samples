""" Module for Nested patterns: patterns can be arbitrarily nested."""
import sys
assert sys.version_info >= (3,10)
from point_class import Point

class NestedPatterns:
    """Nested patterns class """

    def nested_pattern_sample(self, points : list[Point | None]) -> None:
        """Nested pattern sample method """
        # In this nested pattern sample function, a list input is matched against the case pattern
        # and output is printed.
        try:
            match points:
                case []: print("No points in the list")
                case [Point(x=0,y=0)]: print("Origin is the only point in the list")
                case [Point(x=0,y=5)]: print("A single point x,y in the list")
                case [Point(x=0,y=0), Point(x=0,y=5)]:
                    print("Two points on Y axis y1, y2 are in the list")
                case _:
                    print("Something found in the list")
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)

if __name__ == '__main__':
    nested_patterns_instance = NestedPatterns()
    #Created points list and passing for pattern matching.
    points_list: list[Point | None] = [Point(0,0),Point(0,5)]
    nested_patterns_instance.nested_pattern_sample(points_list)
