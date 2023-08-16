"""Module for Complex Patterns and a wildcard"""

from point_class import Point
from color_enum import Color

# class Point:
#     """Point class """
#     int_x: int
#     int_y: int

#     def __init__(self, x_val:int, y_val:int) -> None:
#         self.int_x = x_val
#         self.int_y = y_val

class ComplexPatterns:
    """Complex patterns class"""

    def complex_pattern_sample(self,
                               test_variable: tuple[ int| str, int | str,
                                                    int| str | list[int | str]]) -> None:
        """Complex pattern sample method """
        try:
            match test_variable:
                case ('warning', code, 40): print(' A warning has been received.')
                case (val1 , val2, *rest): #type: ignore
                    print(' Sequence pattern supports wildcards. ') #type: ignore
                case ('error', code, _): #type: ignore
                    print(f"An error {code} occurred.")
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)

    def complex_pattern_with_guard(self, point: Point) -> None:
        """Complex pattern with guard method """

        try:
            match point:
                case Point(int_x,int_y) if int_x == int_y:
                    print(f"The point is located at diagonal Y=X at {int_y}")
                case Point(x_var,y_var): print("Point is not on the diagonal. ")
                case _: pass
                # case (Point(x=x,y=y), Point(x=x,y=y) as p2):
                # print(" Subpattern capturing using as. ") # Subpattern gives an error
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)

    def enumeration_pattern(self, color: Color) -> None:
        """Enumeration pattern method """
        try:
            match color:
                case Color.RED : print('Print Red')
                case Color.GREEN: print('Print Green')
                case Color.BLUE: print('Print Blue')
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)


if __name__ == '__main__':
    cp_instance = ComplexPatterns()
    complex_pattern = (5,5,'_')
    cp_instance.complex_pattern_sample(complex_pattern)
    complex_pattern = ('error','code',800)
    cp_instance.complex_pattern_sample(complex_pattern)

    point_instance = Point(5,7)
    cp_instance.complex_pattern_with_guard(point_instance)
    # cp_instance.complex_pattern_with_guard( Point(5,7),
    # Point(10,10) as p2 ) Getting syntax error
    # when placing a call [SyntaxError: multiple assignments to name 'x' in pattern.]
    cp_instance.enumeration_pattern(Color.BLUE)
