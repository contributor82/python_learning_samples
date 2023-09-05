""" Module for List comprehensions """
# Ways to fill list such as loop/append, maps/lambda expressions
# and bracket structure & range specified.

class ListComprehensions:
    """ List comprehensions class """

    def list_appending(self, squares: list[int], range_val: int) -> list[int]:
        """ Appending list method """
        for i in range(range_val):
            squares.append(i**2)
        return squares

    def list_appending_expression(self, range_val: int) -> list[int]:
        """ Appending list using expression method """
        return [x**2 for x in range(range_val)]

    def list_appending_using_lambda_expression(self, range_val: int) -> list[int]:
        """ Appending list using lambda expression method """
        return list(map(lambda x: x**2, range(range_val)))

    def list_remove_duplicates(self, item_list: list[int]) -> list[int]:
        """ Removing duplicates from list method """
        if item_list:
            item_list.sort()
            last: int = item_list[-1]
            for i in range(len(item_list)-2, -1, -1):
                if last == item_list[i]:
                    del item_list[i]
                else:
                    last = item_list[i]

        return item_list

if __name__ == '__main__':
    lc_instance = ListComprehensions()

    squares_list: list[int] = [0]
    print('Initial Squares list: ', squares_list)
    squares_list = lc_instance.list_appending(squares_list, 10)
    print('After appending list using loop & append  function: ', squares_list)

    empty_squares: list[str] = []
    print('Initial Squares list: ', empty_squares)

    new_squares: list[int] = lc_instance.list_appending_using_lambda_expression(10)
    print('After appending list using lambda expression: ', new_squares)

    empty_squares_two : list[str] = []
    print('Initial Squares list: ', empty_squares_two)

    new_squares_two: list[int] = lc_instance.list_appending_expression(10)
    print('After appending list using for loop: ', new_squares_two)

    duplicated_items_in_list: list[int] = [
        1, 2, 1, 4, 2, 4, 3, 5, 6, 7, 3, 4, 8, 9, 8, 5, 10]
    print('Duplicated Items list: ', duplicated_items_in_list)
    print('After removing duplicates from given list: ',
        lc_instance.list_remove_duplicates(duplicated_items_in_list))
