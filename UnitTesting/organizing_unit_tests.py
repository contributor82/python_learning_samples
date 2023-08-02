import unittest

import sys
sys.path.append("\\UnitTesting\\WidgetClass.py")
from WidgetClass import Widget

class DefaultWidgetSizeTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.widget = Widget('The Widget')
    
    def test_default_widget_size(self) -> None:
        self.assertEqual(self.widget.size(), (50, 50), 'Default sizing')
    
    def test_widget_resize(self) -> None:
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100, 150), 'Wrong size after resize')
    
    def tearDown(self) -> None:
        self.widget.dispose()

def suite() -> unittest.TestSuite: 
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