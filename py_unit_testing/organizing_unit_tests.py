"""Module for organizing unit tests """
import unittest
import importlib

widget_class = importlib.import_module('widget_class', 'py_unit_testing')
Widget = widget_class.Widget

class DefaultWidgetSizeTestCase(unittest.TestCase):
    """ Default widget size test case class """
    widget: Widget

    def set_up(self) -> None:
        """Set up widget method """
        self.widget = Widget('The Widget')

    def test_default_widget_size(self) -> None:
        """ Test default widget size method """
        self.set_up()
        self.assertEqual(self.widget.size_widget(), (50, 50), 'Default sizing')

    def test_widget_resize(self) -> None:
        """ Test widget resize method """
        self.set_up()
        self.widget.resize_widget(100,150)
        self.assertEqual(self.widget.size_widget(), (100, 150), 'Wrong size after resize')

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
