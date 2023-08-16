"""Module for point """
class Point:
    """Point class """
    int_x: int
    int_y: int

    def __init__(self, x_val:int, y_val:int) -> None:
        self.int_x = x_val
        self.int_y = y_val

# if __name__ == '__main__':
#     pt_instance = Point(5,10)
