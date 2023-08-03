# Simple Pattern : Match to a literal
from point_class import Point


class SimplePatterns: 

    # Instead of switch statement, match statement has been used in python. 
    # Here the patterns are each of the case statement
    # Literals represents http status codes. 
    # Once the pattern has been identified, respective http error message will be returned. 
    def http_error(self, status: int): 
        match status: 
            case 400: return 'Bad Request'
            case 401 | 403 : return 'Not Allowed' # Here '|' represents OR meaning this case should be executed for 401 or 403 http code. 
            case 404: return 'Not Found'
            case 418: return 'A teapot'
            case _: return 'Something went wrong'

    # Simple Pattern : Patterns with a literal and variable
    # In this example, point(x,y) has been used for pattern matching to print 
    # what values have been passed. 
    def match_point(self, point: tuple[int,int] | str) -> None: 
        match point:
            case (0, 0): print('Origin')
            case (0,y): print(f"Y={y}")
            case (x,0): print(f"X={x}")
            case (x,y): print(f"X={x}, Y={y}")
            case '_': raise ValueError



    # Simple Pattern: Pattern & classes 
    # In this example, Point class added with init to initialize members.  
    # In pattern matching, initialized class instance is given to match the case and print
    # appropriate output. 
    def location(self, point: Point | None): 
        match point:
            case Point(x=0, y=0): print("Origin is the point's location")
            case Point(x=0, y=y): print(f"Y={y} and the point is on y axis")
            case Point(x=x, y=0): print(f"X={x} and the point is on x axis")
            case Point(x=x, y=y): print(f"X={x} and Y={y} and the point is on x & y axis")
            case Point(): print("The point is on somewhere on the graph")
            case _: print("No point")


if __name__ == '__main__': 

    sp_instance = SimplePatterns()

    print("Http Error : ", sp_instance.http_error(418))
   
    sp_instance.match_point(point=(5,5))

    input_point = Point(2,3)
    sp_instance.location(input_point)

