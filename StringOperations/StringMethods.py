print('C:\n folder1\n folder2')

print('\\n is considered as new line character. ')

print ('To break long string lines while writing use "text" ')

text = ('Put several strings into parentheses '
       'to have them join together')
print(text)

word = 'python'

print ('First letter from word: ', word[0])

print('Last letter from word: ', word[5])

print('First three letters: ', word[:3]) # letters from the beginning position 0

print('First two letters from position 1 : ', word[1:3]) # letters from the beginning position 1

print("Getting string length using len string method: ", len("Hello World!"))

print("Original String: ", word, " Capitalized first letter of the string using capitalize string method: ", word.capitalize())

worldToCaseFold = 'NewPython'

print("Original String: ", worldToCaseFold, " Case folded given string using casefold string method : ", worldToCaseFold.casefold())

print("Original String: ", word, " Centered a given string by padding given character in remaining spaces: ", word.center(10,"n"))

inputStr = "String hiding inside string."

print("Original String: ", inputStr, "SubString: ring", " Substring count using count string method: ", inputStr.count("ring",1,30))

originalStr = "Original"

print("Original String: ", originalStr, " Encoded String using encode string method : ", originalStr.encode(encoding='utf-16',errors='strict'))

print("Original String: ", originalStr, " True if original string ends with given letter using endswith string method: ",  originalStr.endswith("l",1,10))

tabStr = '01\t012\t0123\t01234'

print("Original String: ", tabStr, "\n Expanding string with the specified tab size using expandtabs string method : ", tabStr.expandtabs(tabsize=8))

print("Original String: ", originalStr, " Finding substring position in the given string using find string method:  ", originalStr.find("gi",1,10))

print("Original String: ", originalStr, " Finding substring position in the given string using index string method:  ", originalStr.index("gi",1,10))

# print("Original String: ", originalStr, " Finding substring position in the given string using index string method ValueError if string not found:  ", originalStr.index("di",1,10))

str = "The sum of 1 + 2 is {0}"

print("Original String : ", str, " Formatted string using format string method:  ", str.format(1+2))

alphanumericString = "anmsdfkm1234ASDKSK"

print("Original String : ", alphanumericString, " Finding if the string is alphanumeric or not using isalnum string method: ", alphanumericString.isalnum() )

alphabeticString = "asdkjaakOASDKSD"

print("Original String : ", alphabeticString, " Finding if the string is alphabetic or not using isalnum string method: ", alphabeticString.isalpha() )


lowerStr = "LowerStr"

print("Original String : ", lowerStr, " Checking if string is lower using islower string method: ", lowerStr.islower() )

upperStr = "UPPERSTR"

print("Original String : ", upperStr, " Checking if string is upper using isupper string method: ", upperStr.isupper() )

whiteSpaceStr = "  " # True if all chars as white space.  False otherwise.

print("Original String : ", whiteSpaceStr, " Checking if string has white space using isspace string method: ", whiteSpaceStr.isspace() )

str1 = "String One" 
str2 = "Two"

print("Original Strings : First String: ", str1, " Second String: ", str2, " Joining string iterables using join string method: ", str1.join(str2) )























