"""Module for checking Armstrong number"""


class ArmstrongNum:
    """Armstrong number class"""
    num: int

    def __init__(self, number: int) -> None:
        self.num = number
        self.digits = list(str(number))
        self.power = len(self.digits)
        self.sum = 0

    def check(self) -> bool:
        """Check if the number is Armstrong number"""
        for digit in self.digits:
            self.sum += int(digit) ** self.power
        return self.sum == self.num


if __name__ == "__main__":

    armstrong_num_instance = ArmstrongNum(120)

    if armstrong_num_instance.check() == True:
        print("120 is a Armstrong number")
    else:
        print("120 is not a Armstrong number")

    armstrong_num_instance = ArmstrongNum(153)

    if armstrong_num_instance.check() == True:
        print("153 is a Armstrong number")
    else:
        print("153 is not a Armstrong number")

    armstrong_num_instance = ArmstrongNum(1634)
    if armstrong_num_instance.check() == True:
        print("1634 is a Armstrong number")
    else:
        print("1634 is not a Armstrong number")

    armstrong_num_instance = ArmstrongNum(54748)
    if armstrong_num_instance.check() == True:
        print("54748 is a Armstrong number")
    else:
        print("54748 is not a Armstrong number")

    # print(ArmstrongNum(407).check())
    # print(ArmstrongNum(371).check())
    # print(ArmstrongNum(9474).check())
    # print(ArmstrongNum(54746).check())
    # print(ArmstrongNum(54747).check())
    # print(ArmstrongNum(54749).check())
