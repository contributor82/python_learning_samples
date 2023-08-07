from statistics import median, mean, fmean, geometric_mean, harmonic_mean, median_low, median_high, median_grouped
from math import isnan
from itertools  import filterfalse

class StatsFuncAvgCentralLocations: 
    # Statistic functions of average & measures of central location

    def sort_data(self, data: list[float]) -> list[float]:
        ### Sorting data values ### 
        return sorted(data)

    def median_of_data(self, data: list[float]) -> float: 
       ### Returns the middle value of the data values or 
       ### the avg of middle of two values from the data values ###

        return median(data)

    def mean_of_data(self, data: list[float]) -> float: 
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

    print("Fast, floating arithmatic mean of data : ", stats_funcs_instance.fmean_of_data(clean_data))


    # Suppose a car travels 40 km/hr for 5 km, and when traffic clears, speeds-up to 60 km/hr for the remaining 30 km of the journey. 
    # What is the average speed?
    car_travels_in_kmhr : list [int | float] = [40,60]
    weight : list[ int | float] = [5,30]
    print("harmonic mean of data : ", stats_funcs_instance.harmonic_mean_of_data(car_travels_in_kmhr, weight ))

    print("geometric mean of data : ", stats_funcs_instance.geometric_mean_of_data(clean_data))

    print("median high of data : ", stats_funcs_instance.median_high_of_data(clean_data))

    print("median low of data : ", stats_funcs_instance.median_low_of_data(clean_data))

    print("median grouped of data : ", stats_funcs_instance.median_grouped_of_data(clean_data))







