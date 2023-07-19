class Widget: 
    widgetName = ''
    x=0
    y=0

    def __init__(self, name: str) -> None:
        self.widgetName = name
        self.x =0
        self.y=0

    def size(self) -> tuple[int, int]:
        self.x = 50
        self.y = 50
        
        return (self.x, self.y)
    
    def resize(self,resizeX: int,resizeY: int) -> tuple[int, int]: 
        self.x = resizeX
        self.y = resizeY
        
        return (self.x,self.y)

    def dispose(self) -> None: 
        self.dispose()
