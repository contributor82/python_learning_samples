"""Module for Complex Patterns and a wildcard"""

from point_class import Point
from color_enum import Color

class ComplexPatterns:
    """Complex patterns class"""

    def complex_pattern_sample(self,
                               test_variable: tuple[ int| str, int | str,
                                                    int| str | list[int | str]]) -> None:
        """Complex pattern sample method """

        match test_variable:
            case ('warning', code, 40): print(' A warning has been received.')
            case (val1 , val2, *rest) : print(' Sequence pattern supports wildcards. ')
            case ('error', code, _):
                print(f"An error {code} occurred.")

    def complex_pattern_with_guard(self, point: Point) -> None:
        """Complex pattern with guard method """
        match point:
            case Point(x=x_var,y=y_var) if x_var==y_var:
                print(f"The point is located at diagonal Y=X at {x_var}")
            case Point(x=x_var,y=y_var): print("Point is not on the diagonal. ")
            # case (Point(x=x,y=y), Point(x=x,y=y) as p2):
            # print(" Subpattern capturing using as. ") # Subpattern gives an error

    def enumeration_pattern(self, color: Color) -> None:
        """Enumeration pattern method """
        match color:
            case Color.RED : print('Print Red')
            case Color.GREEN: print('Print Green')
            case Color.BLUE: print('Print Blue')



if __name__ == '__main__':
    cp_instance = ComplexPatterns()
    complex_pattern = (5,5,'_')
    cp_instance.complex_pattern_sample(complex_pattern)
    complex_pattern = ('error','code',800)
    cp_instance.complex_pattern_sample(complex_pattern)
    cp_instance.complex_pattern_with_guard(Point(5,7))
    # cp_instance.complex_pattern_with_guard( Point(5,7),
    # Point(10,10) as p2 ) Getting syntax error
    # when placing a call [SyntaxError: multiple assignments to name 'x' in pattern.]
    cp_instance.enumeration_pattern(Color.BLUE)
