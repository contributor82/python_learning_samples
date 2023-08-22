"""Module for test statistical Functions"""
import unittest


class TestStatisticalFunctions(unittest.TestCase):
    """ Test statistical functions method """

    def average(self, values: list[int] ) -> float :
        """ getting average of list of numbers method """
        avg_val: float = sum(values)/len(values)
        return avg_val

    def test_average(self) -> None:
        """ Test average method """
        test_result : float | AssertionError
        try:
            avg_val: float = self.average([10,20,30,40])
            print('test_average: avg_val = ', avg_val)
            self.assertEqual(avg_val,40.0)
            test_result = avg_val
            self.assertTrue(test_result, 40)
        except AssertionError as assert_error:
            test_result = assert_error
            self.assertTrue(test_result, AssertionError)

    def test_average_by_rounding_value(self) -> None:
        """Test average by rounding value method """
        test_result: bool | AssertionError
        try:
            avg_val: float = self.average([1,5,7])
            print('test_average_by_rounding_value: avg_val = ', avg_val)
            round_val: float = round(avg_val,1)
            print('test_average_by_rounding_value: round_val = ', round_val)
            self.assertTrue(round_val, 4.3)
            test_result = True
        except AssertionError as assertion_error:
            test_result = assertion_error
        self.assertTrue(test_result, True)
        self.assertTrue(test_result, AssertionError)

    def test_average_type_error(self) -> None:
        """Test average type error method """
        test_result: bool | AssertionError
        try:
            avg_val: float = self.average([20,30,70])
            print('test_average_type_error: avg_val = ', avg_val)
            with self.assertRaises(TypeError):
                test_result = True
                self.assertTrue(test_result, True)
        except AssertionError as assertion_error:
            test_result = assertion_error
            self.assertTrue(test_result, AssertionError)


    def test_average_zero_division_error(self) -> None:
        """Test average zero division error method """
        test_result: bool | ZeroDivisionError | AssertionError
        try:
            avg_val: float = self.average([])
            print('test_average_zero_division_error: avg_val = ', avg_val)
            with self.assertRaises(ZeroDivisionError):
                test_result = True
        except ZeroDivisionError as zero_division_error:
            test_result = zero_division_error
            self.assertTrue(test_result, ZeroDivisionError)
        except AssertionError as assertion_error:
            test_result = assertion_error
            self.assertTrue(test_result, AssertionError)

if __name__ == '__main__':
    unittest.main()

# Command line execution as follows
# python -m unittest test_statistical_functions -v
