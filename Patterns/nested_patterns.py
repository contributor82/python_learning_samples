
# Nested Patterns: Patterns can be arbitrarily nested. 

from PointClass import Point

class NestedPatterns:

    # In this nested pattern sample function, a list input is matched against the case pattern
    # and output is printed. 
    def nested_pattern_sample(self, points : any):
        match points:
            case []: print("No points in the list")
            case [Point(x=0,y=0)]: print("Origin is the only point in the list")
            case [Point(x=0,y=5)]: print("A single point x,y in the list")
            case [Point(x=0,y=0), Point(x=0,y=5)]: print("Two points on Y axis y1, y2 are in the list")
            case _: 
                print("Something found in the list")


if __name__ == '__main__': 
    nested_patterns_instance = NestedPatterns()
    #Created points list and passing for pattern matching. 
    points = [Point(0,0),Point(0,5)]
    nested_patterns_instance.nested_pattern_sample(points) 
