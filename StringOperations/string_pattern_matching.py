
# Regular Expressions
import re as regularExpression

class StringPatternMatching: 

    def regex_findall(self): 
        result_non_overlapping_strings = regularExpression.findall(r'\bf[a-z]*','which foot or hand fell fastest')
        return result_non_overlapping_strings
    
    def regex_sub(self): 
        result = regularExpression.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
        return result

    def string_replace(self): 
        return 'tea for too'.replace('too','two')
    
    def is_digit_string(self, input_str: str): 
        result = False
        #[0-9] OR \d
        is_digit_pattern_match = regularExpression.match('[0-9]', input_str) 
        if  is_digit_pattern_match != None: 
                result =  True 
        return result
    
    def is_non_digit_string(self, input_str: str): 
        result = False
        #[^0-9] OR \D
        is_non_digit_pattern_match = regularExpression.match('[^0-9]', input_str) 
        if  is_non_digit_pattern_match != None: 
                result =  True 
        return result
    
    def is_alphanumeric(self, input_str: str): 
        result = False
        #[a-zA-Z0-9_] OR \w
        is_alphanumeric_pattern_match = regularExpression.match('[a-zA-Z0-9_]', input_str) 
        if  is_alphanumeric_pattern_match != None: 
                result =  True 
        return result
    
    def is_non_alphanumeric(self, input_str: str): 
        result = False
        #[^a-zA-Z0-9_] OR \w
        is_non_alphanumeric_pattern_match = regularExpression.match('[^a-zA-Z0-9_]', input_str) 
        if  is_non_alphanumeric_pattern_match != None: 
                result =  True 
        return result
    
    def is_string_prefix_with(self, prefix: str, input_str: str): 
         result = False
         prefix_str =  "^" + prefix
         is_str_prefix_with_pattern_match = regularExpression.search(prefix_str, input_str)
         if is_str_prefix_with_pattern_match != None: 
            result = True
         return result

    def detect_double_words(self, input_str: str): 
        result = ''
        try: 
            searchPattern = regularExpression.compile(r'\b(\w+)\s+\1\b')
            result = searchPattern.search(input_str).group()
        except Exception as ex:
            result = ex
        return result
    
         
spm_instance = StringPatternMatching()
print(spm_instance.regex_findall())
print(spm_instance.regex_sub())
print("909037863858 has all digits  only: ",  spm_instance.is_digit_string('909037863858'))
print("ALPSDKNaskdknkasdn has characters only: ", spm_instance.is_non_digit_string('ALPSDKNaskdknkasdn'))
print("kksdfkn_ANALSN_ has alphanumeric characters only : ", spm_instance.is_alphanumeric('kksdfkn_ANALSN_'))
print("&&#$*U&%21123 has non-alphanumeric characters : ", spm_instance.is_non_alphanumeric('&&#$*U&%21123'))
print(" Hello World! is this string prefix with word 'Hello' : ", spm_instance.is_string_prefix_with('Hello', 'Hello World!'))
print('Using string replace on tea for too string:' ,spm_instance.string_replace())
print('Paris is the the most beautiful place:' ,spm_instance.detect_double_words('Paris is the the most beautiful place'))