"""Module for String methods """

class StringMethods:
    """String methods class """

    def get_first_letter_from_string(self, input_str: str) -> str:
        """Get 1st letter from string method """
        return input_str[0]

    def get_last_letter_from_string(self, input_str: str) -> str:
        """Get last letter from string method """
        word_len: int = len(input_str)
        return input_str[word_len -1]

    def get_first_few_letters_from_string(self, input_str: str, letter_count: int) -> str:
        """Get few letters from string method using letter count """
        return input_str[:letter_count]

    def get_few_letters_from_string(self, input_str: str, start_pos: int, end_pos:int) -> str:
        """Get few letters from string method using start,end position """
        return input_str[start_pos: end_pos]

    def get_first_letter_in_cap_case(self, input_str: str) -> str:
        """Get 1st letter from in cap case method """
        return input_str.capitalize()

    def get_string_case_fold(self, input_str: str) -> str:
        """Get strin case fold method """
        return input_str.casefold()

    def get_string_centered_by_padding(self, input_str: str, width: int, padding_char: str) -> str:
        """Get string centered by padding method """
        return input_str.center(width,padding_char)

    def get_substring_count(self, input_str: str,
                            sub_input_str: str, start_pos: int, width: int) -> int:
        """Get sub string count method """
        return input_str.count(sub_input_str,start_pos, width)

    def get_encoded_string(self, input_str: str, encoding_format: str, error_level: str) -> bytes:
        """Get encoded string method """
        return input_str.encode(encoding=encoding_format, errors= error_level)

    #def get_decoded_string(self, input_str: str, decoding_format: str, error_level:str):
    #    return input_str.decode(decoding_format, error_level)

    def get_string_ends_with(self, letter : str, start: int, end: int) -> bool:
        """Get True/false if string ends with method """
        return original_str.endswith(letter,start,end)

    def get_expanded_string(self, input_str: str, size_num: int) -> str:
        """Get expanded string """
        return input_str.expandtabs(tabsize = size_num)

    def contains_white_space(self, input_str: str) -> bool:
        """Get True/false if string contains white spaces method """
        return input_str.isspace()

    def is_string_lower_case(self, input_str: str) -> bool:
        """Is string lower case method """
        return input_str.islower()

    def is_string_upper_case(self, input_str: str) -> bool:
        """Get string upper case method """
        return input_str.isupper()


if __name__ == '__main__':
    sm_instance = StringMethods()

    print('C:\n folder1\n folder2')
    print('\\n is considered as new line character. ')
    print ('To break long string lines while writing use "text" ')
    TEXT_STR: str = ('Put several strings into parentheses '
        'to have them join together')
    print(TEXT_STR)

    org_str: str = 'python'

    print('Original String: ', org_str,  ' First letter from string: ',
           sm_instance.get_first_letter_from_string(org_str))
    print('Original String: ', org_str,  'Last letter from word: ',
          sm_instance.get_last_letter_from_string(org_str))
    # letters from the beginning position 0
    print('Original String: ', org_str,  ' First three letters: ',
          sm_instance.get_first_few_letters_from_string(org_str,3))
    # letters from the beginning position 1
    print('Original String: ', org_str,  ' First two letters from position 1 : ',
          sm_instance.get_few_letters_from_string(org_str,1,3))
    print('Getting string length using len string method: ', len('Hello World!'))
    print('Original String: ', org_str,
          ' Capitalized first letter of the string using capitalize string method: ',
          sm_instance.get_first_letter_in_cap_case(org_str))

    word_to_case_fold: str = 'NewPython'

    print('Original String: ', word_to_case_fold,
          ' Case folded given string using casefold string method : ',
          sm_instance.get_string_case_fold(word_to_case_fold))

    print('Original String: ', org_str,
          ' Centered a given string by padding given character in remaining spaces: ',
          sm_instance.get_string_centered_by_padding(org_str,10, 'n'))

    nested_str: str = 'String hiding inside string.'

    print('Original String: ', nested_str,
          '  SubString: ring', ' Substring count using count string method: ',
          sm_instance.get_substring_count(nested_str, 'ring', 1,30))

    original_str: str = 'Original'

    print('Original String: ', original_str,
          ' Encoded String using encode string method : ',
          sm_instance.get_encoded_string(original_str, 'utf-16', 'strict') )

    # str_to_decode = b'x80abc'
    #str_to_decode = 'ê' # not converting to utf-8

    #print('Original String: ", str_to_decode,
    # " Decoded String using decode string method : ",
    # sm_instance.get_decoded_string(str_to_decode,"utf-8-sig", "strict'))
    print('Original String: ', original_str,
          ' True if original string ends with given letter using endswith string method: ',
          sm_instance.get_string_ends_with('l', 1, 10)  )

    tab_str: str = '01\t012\t0123\t01234'

    print('Original String: ', tab_str,
          ' \n Expanding string with the specified tab size using expandtabs string method : ',
          sm_instance.get_expanded_string(tab_str, 8) )

    # print('Original String: '", original_str,
    # "' Finding substring position in the given string using find string method:  ",
    # original_str.find("gi",1,10))

    # print('Original String: ", original_str,
    # " Finding substring position in the given string using index string method:  ",
    # original_str.index("gi",1,10))

    # print('Original String: ", original_str,
    # " Finding substring position in the given string
    # using index string method ValueError if string not found:  ",
    # original_str.index("di",1,10))

    # str = "The sum of 1 + 2 is {0}"

    # print('Original String : ",
    # str,
    # " Formatted string using format string method:  ", str.format(1+2))

    lower_str: str = 'lower_str'

    print(' Original String : ',
          lower_str,
          ' Checking if string is lower using islower string method: ',
          sm_instance.is_string_lower_case(lower_str) )

    upper_str: str = 'upper_str'

    print('Original String : ', upper_str,
          ' Checking if string is upper using isupper string method: ',
          sm_instance.is_string_upper_case(upper_str) )

    white_space_str: str = '  ' # True if all chars as white space.  False otherwise.

    print('Original String : ', white_space_str,
          ' Checking if string has white space using isspace string method: ',
          sm_instance.contains_white_space(white_space_str))
