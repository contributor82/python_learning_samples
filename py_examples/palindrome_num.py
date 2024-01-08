"""Module for palindrome number"""


class PalindromeNum:
    """Class for palindrome number"""
    num: int

    def __init__(self, num: int) -> None:
        """Constructor for palindrome number"""
        self.num = num

    def is_palindrome(self) -> bool:
        """Method to check if number is palindrome"""
        num_str = str(self.num)
        rev_str: str = num_str[::-1]
        if num_str == rev_str:
            return True
        return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    palindrome_num_instance = PalindromeNum(num)
    print(palindrome_num_instance.is_palindrome())

    palindrome_num = PalindromeNum(num)
    print(f' Is Number {num} palindrome : ')
    print(palindrome_num.is_palindrome())
