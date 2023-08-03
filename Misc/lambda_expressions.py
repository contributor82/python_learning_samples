
# Lambda Expressions in python

from typing import Literal


class LambdaExpressions: 

    # Returns an incrementor for the given number
    def make_incrementor(self, num: int) -> any:
        return lambda x: x + num

    # Returns a sorted list for the given sort key. 
    def sort_list_using_lambda_expression(self,lst_data: list[tuple[Literal[1]]] , sort_key: any): 
        return sorted(lst_data, key=sort_key)

if __name__ == '__main__': 
    lambda_exp_instance = LambdaExpressions()
    incrementor = lambda_exp_instance.make_incrementor(10)
    print("Make incrementor for 10 using lambda expressions : ", incrementor(0), incrementor(1))

    pairs = [(1, 'one'), (3,'three'), (5,'five'), (2,'two'), (4, 'four')]
    sorted_pairs =  lambda_exp_instance.sort_list_using_lambda_expression(pairs, lambda pair: pair[0])
    print("pairs before sorting: ", pairs)
    print("pairs after sorting: ", sorted_pairs)

