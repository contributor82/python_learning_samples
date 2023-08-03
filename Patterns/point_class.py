class Point: 
    x: int
    y: int

    def __init__(self) -> None: 
        pass

    def __init__(self, x:int, y:int) -> None: 
        self.x=x
        self.y=y

if __name__ == '__main__': 
    pt_instance = Point(5,10)