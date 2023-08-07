from statistics import median, mean, fmean, geometric_mean, harmonic_mean, median_low, median_high, median_grouped, mode, multimode, quantiles
from math import isnan
from itertools  import filterfalse
from fractions import Fraction 
from decimal import Decimal

class StatsFuncAvgCentralLocations: 
    # Statistic functions of average & measures of central location

    def sort_data(self, data: list[float]) -> list[float]:
        ### Sorting data values ### 
        return sorted(data)

    def median_of_data(self, data: list[float]) -> float: 
       ### Returns the middle value of the data values or 
       ### the avg of middle of two values from the data values ###

        return median(data)

    def mean_of_data(self, data: list[ Fraction | Decimal | float]) -> float: 
        ### Sum of the data values divided by number of data values ###
        return mean(data)

    def fmean_of_data(self, data: list[float]) -> float: 
        ### Faster than mean, always returns float.###
        return fmean(data)

    def geometric_mean_of_data(self, data: list[float]) -> float: 
        ### The central tendency or typical value of data values as opposed to arithmatic mean ###
        return geometric_mean(data)

    def harmonic_mean_of_data(self, data: list[int| float], weight: list[int |float]) -> float: 
        ### Reciprocal of the data values ### 
        # 3/(1/a + 1/b + 1/c) when a,b,c values are given 

        return harmonic_mean(data, weights=weight)

    def median_low_of_data(self, data: list[float]) -> float: 
        ### Returns low median of numeric data values ### 
        # When number of data values are odd then middle value 
        # When number of data values are even then low of two middle values
        return median_low(data)

    def median_high_of_data(self, data: list[float]) -> float: 
        ### Returns high median of numeric data values ### 
        # When number of data values are odd then middle value 
        # When number of data values are even then high of two middle values
        return median_high(data)

    def median_grouped_of_data(self, data: list[float]) -> float: 
        ### Returns median of grouped continuous numeric data values using interpolation ### 
        # Default class interval is 1, but changing the value would change the result.
        return median_grouped(data, interval=1)

    def strip_nan_values(self, data:list[float]) -> list[float]:
        ### Removes NaN from data values ### 
        return list(filterfalse(isnan, data))

    def stat_mode(self, data: list[int | str]) -> int | str: 
        ### Returns the single most data point of discrete or nominal data ###
        # there are multiple modes with the same frequency, returns the first one encountered in the data
        
        return mode(data)

    def stat_multimode(self, data: str) -> list[str]: 
        ### Returns a list of most occurring values 
        # returns more than one result if there are multiple modes. 
        return multimode(data)

    def stat_quantiles(self, data : list[int], interval: int, method_val: any) -> list[float]: 
        ### Divides data into n continuous intervals and returns a list of n-1 cut points ###
        # For meaninful results, the data points should be greater than n intervals
        # method values : exclusive or inclusive. 
        return quantiles(data,n=interval, method=method_val)

if __name__ == '__main__': 
    stats_funcs_instance = StatsFuncAvgCentralLocations()

    data = [20.7, float('NaN'), 19.2, 18.3, float('NaN'), 14.4]

    print("data elements : ", data)

    print("sorted data : ", stats_funcs_instance.sort_data(data))

    print("median of data : ", stats_funcs_instance.median_of_data(data))

    clean_data = stats_funcs_instance.strip_nan_values(data)
    print("strip NaN values from data:  ", clean_data)

    print("Sorted clean data:  ", stats_funcs_instance.sort_data(clean_data))

    print("mean of data : ", stats_funcs_instance.mean_of_data(clean_data))

    fraction_data: list[Fraction | Decimal | float] = [Fraction(3,7) , Fraction(1,21),Fraction(5,3), Fraction(1,3)]

    print("mean of fraction data : ", stats_funcs_instance.mean_of_data(fraction_data))

    decimal_data : list [Fraction | Decimal | float] = [Decimal("0.25"), Decimal("0.178"), Decimal("0.26"), Decimal("0.65") ]

    print("mean of decimal data : ", stats_funcs_instance.mean_of_data(decimal_data))

    print("Fast, floating arithmatic mean of data : ", stats_funcs_instance.fmean_of_data(clean_data))

    # Suppose a car travels 40 km/hr for 5 km, and when traffic clears, speeds-up to 60 km/hr for the remaining 30 km of the journey. 
    # What is the average speed?
    car_speed_in_kmhr : list [int | float] = [40,60]
    distance_traveled_in_km : list[ int | float] = [5,30]
    print("harmonic mean of data : ", stats_funcs_instance.harmonic_mean_of_data(car_speed_in_kmhr, distance_traveled_in_km ))

    print("geometric mean of data : ", stats_funcs_instance.geometric_mean_of_data(clean_data))

    print("median high of data : ", stats_funcs_instance.median_high_of_data(clean_data))

    print("median low of data : ", stats_funcs_instance.median_low_of_data(clean_data))

    print("median grouped of data : ", stats_funcs_instance.median_grouped_of_data(clean_data))

    numeric_data_elements : list[int | str] = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
    print("numeric data elements: ", numeric_data_elements)
    print("mode of numeric data: ", stats_funcs_instance.stat_mode(numeric_data_elements))

    alphabetic_data_elements : list[int | str] = ["blue","blue","blue","red","red", "green", "red"]
    print("alphabetic elements: ", alphabetic_data_elements)
    print("mode of alphabetic data elements: ", stats_funcs_instance.stat_mode(alphabetic_data_elements))

    alphabetic_multidata_elements : str  = "aabbccdddddeeeeefffffg"
    print("Numeric multidata elements: ", alphabetic_multidata_elements)
    print("mode of data: ", stats_funcs_instance.stat_multimode(alphabetic_multidata_elements))

    sample_data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
        100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
        106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
        111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
        103, 107, 101, 81, 109, 104]

    print ("sample data for quantile : ", sample_data)
    
    result = [round (q,1) for q in stats_funcs_instance.stat_quantiles(sample_data,10,'exclusive')]

    print (" Quantile of sample data: ", result)








