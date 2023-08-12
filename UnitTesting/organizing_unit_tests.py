"""Module for organizing unit tests """
import unittest
from widget_class import Widget


class DefaultWidgetSizeTestCase(unittest.TestCase):
    """ Default widget size test case class """
    widget: Widget

    def set_up(self) -> None:
        """Set up widget method """
        self.widget = Widget('The Widget')

    def test_default_widget_size(self) -> None:
        """ Test default widget size method """
        self.assertEqual(self.widget.size(), (50, 50), 'Default sizing')

    def test_widget_resize(self) -> None:
        """ Test widget resize method """
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100, 150), 'Wrong size after resize')

    def tear_down(self) -> None:
        """ Test tear down method """
        self.widget.dispose()

def suite() -> unittest.TestSuite:
    """Running test suite """
    test_suite : unittest.TestSuite = unittest.TestSuite()
    test_suite.addTest(DefaultWidgetSizeTestCase('test_default_widget_size'))
    test_suite.addTest(DefaultWidgetSizeTestCase('test_widget_resize'))
    return test_suite

# if not with suite use following
# if __name__ == '__main__':
#     unittest.main()

# if suite created then use following
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
