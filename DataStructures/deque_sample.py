"""Module for Deque sample """
# List as Queue
# Queue - First In, First Out
# Deque object initialized from left-to-right
# Generalization of stacks & queues
# Thread-safe, double ended, pops from either side of deque

from collections import deque


class DequeSample:
    """ Deque sample class. """

    dq_instance : deque[str]

    def __init__(self) -> None:
        self.dq_instance =deque({"Element 1", "Element 2", "Element 3"})

    def print_deque(self, deque_action: str) -> None:
        """ Printing deque """
        print("Deque Action: ", deque_action, " Deque elements: ", self.dq_instance)

    def append_deque(self, element: str) -> None:
        """ Append deque """
        self.dq_instance.append(element)     # type: ignore

    def pop_from_right_side(self) -> str:
        """ pop queue element from right side """
        return self.dq_instance.pop()  # type: ignore

    def pop_from_left_side(self) -> str:
        """ pop queue element from left side """
        return self.dq_instance.popleft()  # type: ignore


if __name__ == '__main__':

    ds_Instance = DequeSample()
    ds_Instance.append_deque("Element 4")
    ds_Instance.append_deque("Element 5")
    ds_Instance.append_deque("Element 6")
    ds_Instance.append_deque("Element 7")

    ds_Instance.print_deque(" 'Initial' ")
    print("pop from left side: ", ds_Instance.pop_from_left_side())

    ds_Instance.print_deque(" 'After pop left' ")
    print("pop from right side: ", ds_Instance.pop_from_right_side())
    ds_Instance.print_deque(" 'After pop' ")
