"""Module for string identifier """
from keyword import iskeyword


class StringIdentifier:
    """String identifier class """

    def is_string_valid_identifier(self, input_str: str) -> bool:
        """Is string valid Python string identifier check method """
        return input_str.isidentifier()

    def is_string_keyword(self, input_str: str) -> bool:
        """Is string a keyword check method """
        return iskeyword(input_str)


if __name__ == '__main__':
    # Verify if string is valid.
    str_identifier_instance = StringIdentifier()
    str_to_validate: str = 'Hello'
    print('Original String: ', str_to_validate, 'Is String valid identifier : ',
          str_identifier_instance.is_string_valid_identifier(str_to_validate))
    print('Original String: ', str_to_validate, 'Is string keyword: ',
          str_identifier_instance.is_string_keyword(str_to_validate))
