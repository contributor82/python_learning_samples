"""Module for simple Pattern : Match to a literal"""
__all__ = ['SimplePatterns']

import sys
# sys.path.append('../py_patterns/point_class')
# import point_class
assert sys.version_info >= (3,10)
#import importlib
#point_class = importlib.import_module('point_class', 'py_patterns')
#Point = point_class.Point

from py_patterns.point_class import Point


class SimplePatterns:
    """Simple patterns class """

    def http_error(self, status: int)-> str:
        """Http error method """
        # Instead of switch statement, match statement has been used in python.
        # Here the patterns are each of the case statement
        # Literals represents http status codes.
        # Once the pattern has been identified, respective http error message will be returned.
        error_msg: str = ''
        try:
            match status:
                case 400: error_msg= 'Bad Request'
                case 401 | 403 : error_msg = 'Not Allowed' # Here '|' represents
                                                    # OR meaning this case should be
                                                    # executed for 401 or 403 http code.
                case 404: error_msg = 'Not Found'
                case 418: error_msg = 'A teapot'
                case _: error_msg = 'Something went wrong'
        except TypeError as type_error:
            print(type_error)
            error_msg = str(type_error)

        except ValueError as value_error:
            print(value_error)
            error_msg = str(value_error)
        return error_msg

    def match_point(self, point_verify: tuple[int,int] | str) -> None:
        """Match point method """
        # Simple Pattern : Patterns with a literal and variable
        # In this example, point(x,y) has been used for pattern matching to print
        # what values have been passed.
        try:
            match point_verify:
                case (0, 0): print('Origin')
                case (0,y_val): print(f"Y={y_val}")
                case (x_val,0): print(f"X={x_val}")
                case (x_val,y_val): print(f"X={x_val}, Y={y_val}")
                case '_': raise ValueError #type: ignore
                case _: pass
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)


    def location(self, point: Point | None) -> None:
        """Location method using point """
        # Simple Pattern: Pattern & classes
        # In this example, Point class added with init to initialize members.
        # In pattern matching, initialized class instance is given to match the case and print
        # appropriate output.
        try:
            match point:
                case Point(x=0, y=0): print("Origin is the point's location")
                case Point(x=0, y=y_val): #type: ignore
                    print(f"Y={y_val} and the point is on y axis") #type: ignore
                case Point(x=x_val, y=0): #type: ignore
                    print(f"X={x_val} and the point is on x axis") #type: ignore
                case Point(x=x_val, y=y_val): #type: ignore
                    print(f"X={x_val} and Y={y_val} and the point is on x & y axis")
                case Point(): print("The point is on somewhere on the graph")
                case _: print("No point")
        except TypeError as type_error:
            print(type_error)
        except ValueError as value_error:
            print(value_error)

if __name__ == '__main__':
    sp_instance = SimplePatterns()
    print("Http Error : ", sp_instance.http_error(418))
    sp_instance.match_point((5,5))
    input_point = Point(2,3)
    sp_instance.location(input_point)
