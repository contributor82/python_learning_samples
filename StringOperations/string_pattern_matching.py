
"""Module for regular expressions"""
import re as regExp
from typing import LiteralString

class StringPatternMatching:
    """ Module for String pattern matching """

    def regex_findall(self) -> list[str | int]:
        """Regular expression to find all non overlapping strings method """
        result_non_overlapping_strings: list[str| int] = regExp.findall(
            r'\bf[a-z]*','which foot or hand fell fastest')
        return result_non_overlapping_strings

    def regex_sub(self) -> str:
        """Getting string by replacing left most occurrances of the pattern in the string method """
        result: str = regExp.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
        return result

    def string_replace(self) -> LiteralString:
        """String replacement method """
        return 'tea for too'.replace('too','two')

    def is_digit_string(self, input_str: str) -> bool:
        """Is digit string method """
        result: bool = False
        #[0-9] OR \d
        is_digit_pattern_match: regExp.Match[str] | None = regExp.match(
             '[0-9]', input_str)
        if is_digit_pattern_match is not None:
            result =  True
        return result

    def is_non_digit_string(self, input_str: str) -> bool:
        """ Is non digit string method """
        result = False
        #[^0-9] OR \D
        is_non_digit_pattern_match: regExp.Match[str] | None = regExp.match(
             '[^0-9]', input_str)
        if  is_non_digit_pattern_match is not None:
            result =  True
        return result

    def is_alphanumeric(self, input_str: str) -> bool:
        """Is alphanumeric method """
        result = False
        #[a-zA-Z0-9_] OR \w
        is_alphanumeric_pattern_match: regExp.Match[str] | None = regExp.match(
            '[a-zA-Z0-9_]', input_str)
        if is_alphanumeric_pattern_match is not None:
            result =  True
        return result

    def is_non_alphanumeric(self, input_str: str) -> bool:
        """Is non alphanumeric method """
        result = False
        #[^a-zA-Z0-9_] OR \w
        is_non_alphanumeric_pattern_match: regExp.Match[str] | None = regExp.match(
            '[^a-zA-Z0-9_]', input_str)
        if is_non_alphanumeric_pattern_match is not None:
            result =  True
        return result

    def is_string_prefix_with(self, prefix: str, input_str: str) -> bool:
        """Is string prefix with method """
        result = False
        prefix_str: str =  "^" + prefix
        is_str_prefix_with_pattern_match: regExp.Match[str] | None = regExp.search(
            prefix_str, input_str)
        if is_str_prefix_with_pattern_match is not None:
            result = True
        return result

    def detect_double_words(self, input_str: str) -> str:
        """Detect double words method """
        final_str: str | None = ""
        search_pattern: regExp.Pattern[str] = regExp.compile(r'\b(\w+)\s+\1\b')
        result: regExp.Match[str] | None = search_pattern.search(input_str)
        if result is not None:
            final_str = result.group()
        return final_str

if __name__ == '__main__':
    try:
        spm_instance = StringPatternMatching()
        print(spm_instance.regex_findall())
        print(spm_instance.regex_sub())
        print("909037863858 has all digits  only: ",
            spm_instance.is_digit_string('909037863858'))
        print("ALPSDKNaskdknkasdn has characters only: ",
            spm_instance.is_non_digit_string('ALPSDKNaskdknkasdn'))
        print("kksdfkn_ANALSN_ has alphanumeric characters only : ",
            spm_instance.is_alphanumeric('kksdfkn_ANALSN_'))
        print("&&#$*U&%21123 has non-alphanumeric characters : ",
            spm_instance.is_non_alphanumeric('&&#$*U&%21123'))
        print(" Hello World! is this string prefix with word 'Hello' : ",
            spm_instance.is_string_prefix_with('Hello', 'Hello World!'))
        print('Using string replace on tea for too string:',
            spm_instance.string_replace())
        print('Paris is the the most beautiful place:',
            spm_instance.detect_double_words('Paris is the the most beautiful place'))
    except regExp.error as regexp_error:
        print(regexp_error)
