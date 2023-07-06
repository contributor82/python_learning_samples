
# Regular Expressions
import re as regularExpression

class StringPatternMatching: 

    def regex_findall(self): 
        resultNonOverlappingStrings = regularExpression.findall(r'\bf[a-z]*','which foot or hand fell fastest')
        return resultNonOverlappingStrings
    
    def regex_sub(self): 
        result = regularExpression.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
        return result

    def string_replace(self): 
        return 'tea for too'.replace('too','two')
    
    def is_digit_string(self, inputStr): 
        result = False
        #[0-9] OR \d
        isDigitPatternMatch = regularExpression.match('[0-9]', inputStr) 
        if  isDigitPatternMatch != None: 
                result =  True 
        return result
    
    def is_non_digit_string(self, inputStr): 
        result = False
        #[^0-9] OR \D
        isNonDigitPatternMatch = regularExpression.match('[^0-9]', inputStr) 
        if  isNonDigitPatternMatch != None: 
                result =  True 
        return result
    
    def is_alphanumeric(self, inputStr): 
        result = False
        #[a-zA-Z0-9_] OR \w
        isAlphanumericPatternMatch = regularExpression.match('[a-zA-Z0-9_]', inputStr) 
        if  isAlphanumericPatternMatch != None: 
                result =  True 
        return result
    
    def is_non_alphanumeric(self, inputStr): 
        result = False
        #[^a-zA-Z0-9_] OR \w
        isNonAlphanumericPatternMatch = regularExpression.match('[^a-zA-Z0-9_]', inputStr) 
        if  isNonAlphanumericPatternMatch != None: 
                result =  True 
        return result
    
    def is_string_prefix_with(self, prefix, inputStr): 
         result = False
         prefix_str =  "^" + prefix
         isStringPrefixWithPatternMatch = regularExpression.search(prefix_str, inputStr)
         if isStringPrefixWithPatternMatch != None: 
            result = True
         return result

    def detect_double_words(self, inputStr): 
        result = ''
        try: 
            searchPattern = regularExpression.compile(r'\b(\w+)\s+\1\b')
            result = searchPattern.search(inputStr).group()
        except Exception as ex:
            result = ex
        return result
    
         
spmInstance = StringPatternMatching()
print(spmInstance.regex_findall())
print(spmInstance.regex_sub())
print("909037863858 has all digits  only: ",  spmInstance.is_digit_string('909037863858'))
print("ALPSDKNaskdknkasdn has characters only: ", spmInstance.is_non_digit_string('ALPSDKNaskdknkasdn'))
print("kksdfkn_ANALSN_ has alphanumeric characters only : ", spmInstance.is_alphanumeric('kksdfkn_ANALSN_'))
print("&&#$*U&%21123 has non-alphanumeric characters : ", spmInstance.is_non_alphanumeric('&&#$*U&%21123'))
print(" Hello World! is this string prefix with word 'Hello' : ", spmInstance.is_string_prefix_with('Hello', 'Hello World!'))
print('Using string replace on tea for too string:' ,spmInstance.string_replace())
print('Paris is the the most beautiful place:' ,spmInstance.detect_double_words('Paris is the the most beautiful place'))