
# Nested Patterns: Patterns can be arbitrarily nested. 

class Point: 
    x: int
    y: int

    def __init__(self,x,y): 
        self.x=x
        self.y=y


class NestedPatterns:

    # In this nested pattern sample function, a list input is matched against the case pattern
    # and output is printed. 
    def nested_pattern_sample(self, points):
        match points:
            case []: print("No points in the list")
            case [Point(x=0,y=0)]: print("Origin is the only point in the list")
            case [Point(x=0,y=5)]: print("A single point x,y in the list")
            case [Point(x=0,y=0), Point(x=0,y=5)]: print("Two points on Y axis y1, y2 are in the list")
            case _: 
                print("Something found in the list")


nestedPatternsInstance = NestedPatterns()
#Created points list and passing for pattern matching. 
points = [Point(0,0),Point(0,5)]
nestedPatternsInstance.nested_pattern_sample(points) 
