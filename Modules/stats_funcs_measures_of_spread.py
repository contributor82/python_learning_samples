"""Module for Measures of spread statistic functions """
from statistics import pstdev, pvariance, variance


class StatFuncMeasuresOfSpread:
    """ Statistic functions class for measures of spread """

    def population_std_deviation_of_data(self, input_data: list[int | float],
                                         mean_of_data: int | None = None) -> int | float:
        """ Returning the population of standard deviation """
        return pstdev(input_data, mean_of_data)

    def variance_of_data(self, input_data: list[int | float],
                         mean_of_data: int | None = None) -> int | float:
        """ Returns the sample variance of data """
        # If mean of data has already been calculated
        # then pass it to xbar to avoid recalculating.
        return variance(input_data, xbar=mean_of_data)

    def population_variance_of_data(self, input_data: list[int | float],
                                    mean_of_data: int | None = None) -> int | float:
        """ Returns the population variance of data """
        return pvariance(input_data, mean_of_data)

if __name__ == '__main__':
    sf_measure_of_spread_instance = StatFuncMeasuresOfSpread()

    sample_data: list[int | float] = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    print('Input data for population of standard deviation : ', sample_data)
    print('population of standard deviation outcome: ',
          sf_measure_of_spread_instance.population_std_deviation_of_data(sample_data))

    sample_data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print('Input data for variance : ', sample_data)
    print('variance of data: ',
          sf_measure_of_spread_instance.variance_of_data(sample_data))

    sample_data = [0.25, 0.75, 0.35, 0.45, 0.50]
    print('Input data for population of variance : ', sample_data)
    print('population of standard deviation outcome: ',
          sf_measure_of_spread_instance.population_variance_of_data(sample_data))
