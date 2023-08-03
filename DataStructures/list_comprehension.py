# List comprehensions
# Ways to fill list such as loop/append, maps/lambda expressions and bracket structure & range specified.

class ListComprehensions: 

    def list_appending(self, squares: list[int], range_val : int): 
        for i in range(range_val):
            squares.append(i**2)
        return squares
    
    def list_appending_expression(self, range_val: int):
        return [x**2 for x in range(range_val)]

    def list_appending_using_lambda_expression(self, range_val: int): 
        return list(map(lambda x:x**2,range(range_val)))
    
    def list_remove_duplicates(self, item_list: list[int]): 
        if item_list: 
            item_list.sort()
            last = item_list[-1]
            for i in range(len(item_list)-2, -1, -1): 
                if last == item_list[i]: 
                    del item_list[i]
                else: 
                    last = item_list[i]

        return item_list

lc_instance =  ListComprehensions()

squares = [int]
print("Initial Squares list: ",squares)
squares = lc_instance.list_appending(squares, 10) 
print("After appending list using loop & append  function: ",squares)

new_squares = []
print("Initial Squares list: ",new_squares)

new_squares = lc_instance.list_appending_using_lambda_expression(10)
print("After appending list using lambda expression: ",new_squares)

new_squares_two = []
print("Initial Squares list: ",new_squares_two)

new_squares_two = lc_instance.list_appending_expression(10)
print("After appending list using for loop: ",new_squares)

duplicated_items_in_list = [1,2,1,4,2,4,3,5,6,7,3,4,8,9,8,5,10]
print("Duplicated Items list: ", duplicated_items_in_list)
print("After removing duplicates from given list: ", lc_instance.list_remove_duplicates(duplicated_items_in_list))
