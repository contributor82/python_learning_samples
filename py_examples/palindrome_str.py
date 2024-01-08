"""Module for palindrome string check."""


class PalindromeStr:
    """Class for palindrome string check."""
    string: str

    def __init__(self, string: str) -> None:
        """Initialize class."""
        self.string = string

    def check(self) -> bool:
        """Check if string is palindrome."""
        print(f'Checking {self.string} string...')
        print(f'String reverse is {self.string[::-1]} ...')
        return self.string == self.string[::-1]


if __name__ == '__main__':
    string = input('Enter string: ')
    palindrom_str_instance = PalindromeStr(string)
    print(f'Is {string} palindrome?')
    print(palindrom_str_instance.check())
