"""Module for lambda expressions in python """

class LambdaExpressions:
    """Lambda expression class"""

    def make_incrementor(self, num: int) -> object:
        """ Returns an incrementor for the given number """
        return lambda x: x + num # type: ignore

    def sort_list_using_lambda_expression(self,
                                          lst_data: list[tuple[int, str]] ,
                                          sort_key:object) -> list[tuple[int,str]]:
        """ Returns a sorted list for the given sort key. """
        return sorted(lst_data, key=sort_key) # type: ignore

if __name__ == '__main__':
    lambda_exp_instance = LambdaExpressions()
    incrementor: object = lambda_exp_instance.make_incrementor(10)
    print("Make incrementor for 10 using lambda expressions : ", incrementor(0), # type: ignore
          incrementor(1)) # type: ignore
    pairs : list [tuple[int, str]] = [(1, 'one'), (3,'three'), (5,'five'), (2,'two'), (4, 'four')]
    sorted_pairs: list[tuple[int, str]] =  lambda_exp_instance.sort_list_using_lambda_expression(
        pairs,
        lambda pair: pair[0]) # type: ignore
    print("pairs before sorting: ", pairs)
    print("pairs after sorting: ", sorted_pairs)
