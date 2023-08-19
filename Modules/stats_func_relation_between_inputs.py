"""Module for relation between inputs statistic functions """
from statistics import covariance, correlation, linear_regression
from statistics import LinearRegression

class StatFuncInputRelations:
    """Input relations statistic functions """

    def covariance_of_data(self, input_x: list[int], input_y: list[int]) -> float:
        """ Returns a joint variability of two inputs """
        # Both the inputs of same length (no less than 2)
        return covariance(input_x, input_y)

    def correlation_of_data(self, input_x: list[int], input_y: list[int]) -> float:
        """ Returns Pearson's correlation coefficient of two inputs """
        # Pearson's correlation coefficient r takes values -1 & +1,
        # measures the strength & the direction of the linear relationship.
        # + 1 very strong : +ve linear regression, -1 very strong
        # -ve linear regression, 0 no linear regression
        # Both the inputs of same length (no less than 2)
        return correlation(input_x, input_y)

    def linear_regression_of_data(self, input_x: list[int], input_y: list[int]) -> LinearRegression:
        """ Returns slope & intercept of simple linear regression """
        # Simple linear regression describes the relationship between an
        # independent variable x and a dependent variable y
        # in terms of this linear function: y = slope * x + intercept + noise
        # noise means the variability of the data
        # Both the inputs of same length (no less than 2)
        # independent variable x can't be constant
        return linear_regression(input_x, input_y)

if __name__ == '__main__':
    sfcir_instance = StatFuncInputRelations()
    covariance_input_x : list[int] = [1,2,3,4,5,6,7,8,9]
    covariance_input_y : list[int] = [1,2,1,2,3,4,1,3,4]
    print(' Covariance X : ', covariance_input_x, ' Covariance Y: ', covariance_input_y)
    print(' Covariance of X & Y: ',
          sfcir_instance.covariance_of_data(covariance_input_x, covariance_input_y))

    correlation_input_x : list[int] = [1,2,3,4,5,6,7,8,9]
    correlation_input_y :  list[int] = [1,2,1,2,3,4,1,3,4]
    print (' Correlation X : ', correlation_input_x,
           ' Correlation Y: ',correlation_input_y)
    print(' Correlation of X & Y: ',
          sfcir_instance.correlation_of_data(correlation_input_x, correlation_input_y))

    linear_reg_month: list[int] = [1,2,3,4,5,6,7,8,9,10,11]
    linear_reg_spendings: list[int] = [5000,10000,4000,8000,4500,9000,15000,3000,5000,2000,1000]
    print('Months : ', linear_reg_month)
    print('Spendings : ', linear_reg_spendings)
    slope, intercept = sfcir_instance.linear_regression_of_data(
        linear_reg_month, linear_reg_spendings)
    print('slope : ', slope, ' intercept: ', intercept)
    print('Spending prediction in 12th month : ', round(slope * 12 + intercept))
