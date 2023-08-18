"""Module for point """
class Point:
    """Point class """
    int_x: int
    int_y: int

    def __init__(self, x_val:int, y_val:int) -> None:
        """Initializing point class members """
        self.int_x = x_val
        self.int_y = y_val

    def get_point_x_val(self)->int:
        """Get point x val"""
        return self.int_x

    def get_point_y_val(self)->int:
        """Get point y val"""
        return self.int_y

    def display(self)-> None:
        """Displaying point class members """
        print("int x: ", self.int_x, " int y: ", self.int_y)

# if __name__ == '__main__':
#     pt_instance = Point(5,10)
