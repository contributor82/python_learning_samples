# Test Statistical Functions
import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def average(self, values: any) -> float: 
        return sum(values)/len(values)

    def test_average(self): 
        try:
            avgVal = self.average([10,20,30,40])
            print('test_average: avgVal = ', avgVal)
            self.assertEqual(avgVal,40.0)
        except Exception as ex:  
            return ex.__str__()
        
    def test_average_by_rounding_value(self) -> str | None:
        try:
            avgVal = self.average([1,5,7])
            print('test_average_by_rounding_value: avgVal = ', avgVal)
            roundVal = round(avgVal,1)
            print('test_average_by_rounding_value: roundVal = ', roundVal)
            self.assertEqual(roundVal, 4.3)
        except Exception as ex: 
            return ex.__str__()
            
    def test_average_type_error(self) -> None:
        avgVal = self.average(20,30,70)
        print('test_average_type_error: avgVal = ', avgVal)
        with self.assertRaises(TypeError): avgVal

    def test_average_zero_division_error(self) -> None: 
        avgVal = self.average([])
        print('test_average_zero_division_error: avgVal = ', avgVal)
        with self.assertRaises(ZeroDivisionError): avgVal
        

if __name__ == '__main__':
    unittest.main()

# Command line execution as follows
# python -m unittest TestStatisticalFunctions -v
