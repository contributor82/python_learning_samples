"""Module for Union type operator """


from typing import Union


class UnionTypeOperator:
    """Union Type Operator """

    def square_using_union(self, num: Union[int, float])-> Union[int, float]:
        """Square using union operator"""
        return num ** 2

    def square_using_pipe(self, num_val: int | float)-> int | float:
        """Square using | operator """
        return num_val ** 2


if __name__ == '__main__':
    union_op_instance = UnionTypeOperator()
    print('5 square is using Union[int, float] : ', union_op_instance.square_using_union(5))
    print('5 square is using int | float or pipe : ', union_op_instance.square_using_pipe(5))
