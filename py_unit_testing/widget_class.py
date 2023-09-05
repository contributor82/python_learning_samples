"""Module for widget class """
class Widget:
    """Widget class"""
    widget_name: str = ''
    x_val : int =0
    y_val : int =0

    def __init__(self, name: str) -> None:
        """Initialize class members """
        self.widget_name = name
        self.x_val =0
        self.y_val =0

    def size_widget(self) -> tuple[int, int]:
        """Sizing members method """
        self.x_val = 50
        self.y_val = 50

        return (self.x_val, self.y_val)

    def resize_widget(self,resize_x: int,resize_y: int) -> tuple[int, int]:
        """Resizing members method """
        self.x_val = resize_x
        self.y_val = resize_y

        return (self.x_val,self.y_val)

    def dispose(self) -> None:
        """Disposing class instance """
        self.dispose() # type: ignore

if __name__ == '__main__':
    widget_instance = Widget('Widget class')
