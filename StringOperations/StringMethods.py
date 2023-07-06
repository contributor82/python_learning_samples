import unicodedata

class StringMethods: 
    
    def get_first_letter_from_string(self, inputStr): 
       return inputStr[0]
    
    def get_last_letter_from_string(self, inputStr): 
        wordLen = len(inputStr)
        return inputStr[wordLen -1]
    
    def get_first_few_letters_from_string(self, inputStr, letterCount): 
        return inputStr[:letterCount]

    def get_few_letters_from_string(self, inputStr, startPos, endPos): 
        return inputStr[startPos: endPos]
    
    def get_first_letter_in_cap_case(self, inputStr): 
        return inputStr.capitalize()
    
    def get_string_case_fold(self, inputStr): 
        return inputStr.casefold()
    
    def get_string_centered_by_padding(self, inputStr, width, paddingChar): 
        return inputStr.center(width,paddingChar)

    def get_substring_count(self, inputStr, str, startPos, width): 
        return inputStr.count(str,startPos, width)
    
    def get_encoded_string(self, inputStr, encodingFormat, errorLevel): 
        return inputStr.encode(encoding=encodingFormat, errors= errorLevel) 

    def get_decoded_string(self, inputStr, decodingFormat, errorLevel): 
        return inputStr.decode(decodingFormat, errorLevel)
    
    def get_string_ends_with(self, letter, start, end):
        return originalStr.endswith(letter,start,end)
    
    def get_expanded_string(self, inputStr, sizeNum): 
        return inputStr.expandtabs(tabsize = sizeNum)

smInstance = StringMethods()

print('C:\n folder1\n folder2')

print('\\n is considered as new line character. ')

print ('To break long string lines while writing use "text" ')

text = ('Put several strings into parentheses '
       'to have them join together')
print(text)

str = 'python'

print ("Original String: '", str,  "' First letter from string: ", smInstance.get_first_letter_from_string(str))

print("Original String: '", str,  "'Last letter from word: ", smInstance.get_last_letter_from_string(str))

print("Original String: '", str,  "' First three letters: ", smInstance.get_first_few_letters_from_string(str,3)) # letters from the beginning position 0

print("Original String: '", str,  "' First two letters from position 1 : ", smInstance.get_few_letters_from_string(str,1,3)) # letters from the beginning position 1

print("Getting string length using len string method: ", len("Hello World!"))

print("Original String: '", str, "' Capitalized first letter of the string using capitalize string method: ", smInstance.get_first_letter_in_cap_case(str))

worldToCaseFold = 'NewPython'

print("Original String: '", worldToCaseFold, "' Case folded given string using casefold string method : ", smInstance.get_string_case_fold(worldToCaseFold))

print("Original String: '", str, "' Centered a given string by padding given character in remaining spaces: ", smInstance.get_string_centered_by_padding(str,10, "n"))

inputStr = "String hiding inside string."

print("Original String: '", inputStr, "'  SubString: ring", " Substring count using count string method: ", smInstance.get_substring_count(inputStr, "ring", 1,30))

originalStr = "Original"

print("Original String: '", originalStr, "' Encoded String using encode string method : ", smInstance.get_encoded_string(originalStr, 'utf-16', 'strict') )

stringToDecode = b'x80abc'

print("Original String: ", stringToDecode, " Decoded String using decode string method : ",  smInstance.get_decoded_string(stringToDecode,"utf-8", "strict"))

print("Original String: '", originalStr, "' True if original string ends with given letter using endswith string method: ", smInstance.get_string_ends_with("l", 1, 10)  )

tabStr = '01\t012\t0123\t01234'

print("Original String: '", tabStr, "' \n Expanding string with the specified tab size using expandtabs string method : ",  smInstance.get_expanded_string(tabStr, 8) )

# print("Original String: '", originalStr, "' Finding substring position in the given string using find string method:  ",  originalStr.find("gi",1,10))

# print("Original String: ", originalStr, " Finding substring position in the given string using index string method:  ", originalStr.index("gi",1,10))

# print("Original String: ", originalStr, " Finding substring position in the given string using index string method ValueError if string not found:  ", originalStr.index("di",1,10))

# str = "The sum of 1 + 2 is {0}"

# print("Original String : ", str, " Formatted string using format string method:  ", str.format(1+2))

# lowerStr = "LowerStr"

# print("Original String : ", lowerStr, " Checking if string is lower using islower string method: ", lowerStr.islower() )

# upperStr = "UPPERSTR"

# print("Original String : ", upperStr, " Checking if string is upper using isupper string method: ", upperStr.isupper() )

# whiteSpaceStr = "  " # True if all chars as white space.  False otherwise.

# print("Original String : ", whiteSpaceStr, " Checking if string has white space using isspace string method: ", whiteSpaceStr.isspace() )

# str1 = "String One" 
# str2 = "Two"

# print("Original Strings : First String: ", str1, " Second String: ", str2, " Joining string iterables using join string method: ", str1.join(str2) )























