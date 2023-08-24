""" Module for Nested patterns: patterns can be arbitrarily nested."""
import sys
assert sys.version_info >= (3,10)
import importlib
point_class =  importlib.import_module('point_class','py_patterns')
Point = point_class.Point

class NestedPatterns:
    """Nested patterns class """
    int_point: Point
    str_point: Point
    def __init__(self) -> None:
        self.int_point = Point(0,0)
        self.str_point = Point(1,2)

    def nested_pattern_sample_one(self, pattern: dict[int | str, Point | str ] ) -> None:
        """Nested pattern sample one method """
        # In this nested pattern sample function,
        # a dictionary input matched against the case pattern
        # and output is printed.
        # currently not matching pattern as expected
        # case {}: print('Nothing provided in pattern to match. ')
        try:
            match pattern:

                case {1: self.int_point }: print('Integer object pattern')
                case {'OnePoint': self.str_point}: print('String object pattern')
                case {'SecondPoint': 'second point'} : print ('String string pattern')
                case _:
                    print('Something found in the list')
        except TypeError as nested_pattern_one_type_error:
            print(nested_pattern_one_type_error)
        except ValueError as nested_pattern_one_value_error:
            print(nested_pattern_one_value_error)


    def nested_pattern_sample_two(self, points : list[Point | None]) -> None:
        """Nested pattern sample two method """
        # In this nested pattern sample function, a list input is matched against the case pattern
        # and output is printed.
        # currently not matching pattern as expected
        try:
            match points:
                case []: print("No points in the list")
                case [Point(x=0,y=0)]: print("Origin is the only point in the list")
                case [Point(x_val=0,y_val=5)]: print("A single point x,y in the list")
                case [Point(x=0,y=0),Point(x=0,y=5)]:
                    print("Two points on Y axis y1, y2 are in the list")
                case [Point(0,0),Point(0,5)]:
                    print("Two points on Y axis.")
                case _:
                    print("Something found in the list")
        except TypeError as nested_pattern_two_type_error:
            print(nested_pattern_two_type_error)
        except ValueError as nested_pattern_two_value_error:
            print(nested_pattern_two_value_error)

if __name__ == '__main__':
    nested_patterns_instance = NestedPatterns()
    #Created points list and passing for pattern matching.
    dict_one = {}
    nested_patterns_instance.nested_pattern_sample_one(dict_one)

    dict_two: dict[int | str, Point | str ] = {1:Point(0,0) }
    nested_patterns_instance.nested_pattern_sample_one(dict_two)

    dict_three: dict[int | str, Point | str ] =  {'OnePoint': Point(1,2) }
    nested_patterns_instance.nested_pattern_sample_one(dict_three)

    dict_four: dict[int | str, Point | str ] = {'SecondPoint': 'second point'}
    nested_patterns_instance.nested_pattern_sample_one(dict_four)


    pt_one_instance = Point(x_val=0,y_val=0)
    pt_two_instance = Point(x_val=0,y_val=5)
    points_list_trial_one: list[Point | None] = []
    nested_patterns_instance.nested_pattern_sample_two(points_list_trial_one)

    points_list_trial_two: list[Point | None] = [Point, Point]
    nested_patterns_instance.nested_pattern_sample_two(points_list_trial_two)

    points_list_trial_three: list[Point | None] = [Point(x_val=0,y_val=0), Point(x_val=0, y_val=5)]
    nested_patterns_instance.nested_pattern_sample_two(points_list_trial_three)

    points_list_trial_four: list[Point | None] = [Point(x_val=0,y_val=5)]
    nested_patterns_instance.nested_pattern_sample_two(points_list_trial_four)
