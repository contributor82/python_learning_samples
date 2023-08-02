import unicodedata

class StringMethods: 
    
    def get_first_letter_from_string(self, input_str: str): 
       return input_str[0]
    
    def get_last_letter_from_string(self, input_str: str): 
        wordLen = len(input_str)
        return input_str[wordLen -1]
    
    def get_first_few_letters_from_string(self, input_str: str, letter_count: int): 
        return input_str[:letter_count]

    def get_few_letters_from_string(self, input_str: str, startPos: int, endPos:int): 
        return input_str[startPos: endPos]
    
    def get_first_letter_in_cap_case(self, input_str: str): 
        return input_str.capitalize()
    
    def get_string_case_fold(self, input_str: str): 
        return input_str.casefold()
    
    def get_string_centered_by_padding(self, input_str: str, width: int, padding_char: str): 
        return input_str.center(width,padding_char)

    def get_substring_count(self, input_str: str, x: str, startPos: int, width: int): 
        return input_str.count(x,startPos, width)
    
    def get_encoded_string(self, input_str: str, encoding_format: str, error_level: str): 
        return input_str.encode(encoding=encoding_format, errors= error_level) 

    #def get_decoded_string(self, input_str: str, decoding_format: str, error_level:str): 
    #    return input_str.decode(decoding_format, error_level)
    
    def get_string_ends_with(self, letter : str, start: int, end: int):
        return original_str.endswith(letter,start,end)
    
    def get_expanded_string(self, input_str: str, size_num: int): 
        return input_str.expandtabs(tabsize = size_num)
    
    def contains_white_space(self, input_str: str): 
        return input_str.isspace()
    
    def is_string_lower_case(self, input_str: str): 
        return input_str.islower()
    
    def is_string_upper_case(self, input_str: str): 
        return input_str.isupper()


if __name__ == '__main__': 
    sm_instance = StringMethods()

    print('C:\n folder1\n folder2')

    print('\\n is considered as new line character. ')

    print ('To break long string lines while writing use "text" ')

    text = ('Put several strings into parentheses '
        'to have them join together')
    print(text)

    str = 'python'

    print ("Original String: '", str,  "' First letter from string: ", sm_instance.get_first_letter_from_string(str))

    print("Original String: '", str,  "'Last letter from word: ", sm_instance.get_last_letter_from_string(str))

    print("Original String: '", str,  "' First three letters: ", sm_instance.get_first_few_letters_from_string(str,3)) # letters from the beginning position 0

    print("Original String: '", str,  "' First two letters from position 1 : ", sm_instance.get_few_letters_from_string(str,1,3)) # letters from the beginning position 1

    print("Getting string length using len string method: ", len("Hello World!"))

    print("Original String: '", str, "' Capitalized first letter of the string using capitalize string method: ", sm_instance.get_first_letter_in_cap_case(str))

    worldToCaseFold = 'NewPython'

    print("Original String: '", worldToCaseFold, "' Case folded given string using casefold string method : ", sm_instance.get_string_case_fold(worldToCaseFold))

    print("Original String: '", str, "' Centered a given string by padding given character in remaining spaces: ", sm_instance.get_string_centered_by_padding(str,10, "n"))

    input_str = "String hiding inside string."

    print("Original String: '", input_str, "'  SubString: ring", " Substring count using count string method: ", sm_instance.get_substring_count(input_str, "ring", 1,30))

    original_str = "Original"

    print("Original String: '", original_str, "' Encoded String using encode string method : ", sm_instance.get_encoded_string(original_str, 'utf-16', 'strict') )

    # str_to_decode = b'x80abc'
    #str_to_decode = 'ê' # not converting to utf-8

    #print("Original String: ", str_to_decode, " Decoded String using decode string method : ",  sm_instance.get_decoded_string(str_to_decode,"utf-8-sig", "strict"))

    print("Original String: '", original_str, "' True if original string ends with given letter using endswith string method: ", sm_instance.get_string_ends_with("l", 1, 10)  )

    tab_str = '01\t012\t0123\t01234'

    print("Original String: '", tab_str, "' \n Expanding string with the specified tab size using expandtabs string method : ",  sm_instance.get_expanded_string(tab_str, 8) )

    # print("Original String: '", original_str, "' Finding substring position in the given string using find string method:  ",  original_str.find("gi",1,10))

    # print("Original String: ", original_str, " Finding substring position in the given string using index string method:  ", original_str.index("gi",1,10))

    # print("Original String: ", original_str, " Finding substring position in the given string using index string method ValueError if string not found:  ", original_str.index("di",1,10))

    # str = "The sum of 1 + 2 is {0}"

    # print("Original String : ", str, " Formatted string using format string method:  ", str.format(1+2))

    lower_str = "lower_str"

    print("Original String : ", lower_str, " Checking if string is lower using islower string method: ", sm_instance.is_string_lower_case(lower_str) )

    upper_str = "upper_str"

    print("Original String : ", upper_str, " Checking if string is upper using isupper string method: ", sm_instance.is_string_upper_case(upper_str) )

    white_space_str = "  " # True if all chars as white space.  False otherwise.

    print("Original String : ", white_space_str, " Checking if string has white space using isspace string method: ",  sm_instance.contains_white_space(white_space_str))
























