import unittest

class Widget: 
    widgetName = ''
    x=0
    y=0

    def __init__(self, name):
        self.widgetName = name
        self.x =0
        self.y=0

    def size(self):
        self.x = 50
        self.y = 50
        
        return (self.x, self.y)
    
    def resize(self,resizeX,resizeY): 
        self.x = resizeX
        self.y = resizeY
        
        return (self.x,self.y)

    def dispose(self): 
        self.dispose()


class DefaultWidgetSizeTestCase(unittest.TestCase):
    
    def setUp(self):
        self.widget = Widget('The Widget')
    
    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'Default sizing')
    
    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100, 150), 'Wrong size after resize')
    
    def tearDown(self):
        self.widget.dispose()

def suite(): 
    suite = unittest.TestSuite()
    suite.addTest(DefaultWidgetSizeTestCase('test_default_widget_size'))
    suite.addTest(DefaultWidgetSizeTestCase('test_widget_resize'))
    return suite

# if not with suite use following
# if __name__ == '__main__': 
#     unittest.main()

# if suite created then use following 
if __name__ == '__main__': 
    runner = unittest.TextTestRunner()
    runner.run(suite())