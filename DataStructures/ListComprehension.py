# List comprehensions
# Ways to fill list such as loop/append, maps/lambda expressions and bracket structure & range specified.

class ListComprehensions: 

    def list_appending(self, squares, rangeVal): 
        for i in range(10):
            squares.append(i**2)
        return squares
    
    def list_appending_expression(self, rangeVal):
        return [x**2 for x in range(rangeVal)]

    def list_appending_using_lambda_expression(self, rangeVal): 
        return list(map(lambda x:x**2,range(rangeVal)))


lcInstance =  ListComprehensions()

squares = []
print("Initial Squares list: ",squares)
squares = lcInstance.list_appending(squares, 10) 
print("After appending list using loop & append  function: ",squares)

newSquares = []
print("Initial Squares list: ",newSquares)

newSquares = lcInstance.list_appending_using_lambda_expression(10)
print("After appending list using lambda expression: ",newSquares)

newSquaresTwo = []
print("Initial Squares list: ",newSquaresTwo)

newSquaresTwo = lcInstance.list_appending_expression(10)
print("After appending list using for loop: ",newSquares)
