"""Module for string concatenation approach"""

class StringConcatenations:
    """String concatenation class """
    str1: str = "String One"
    str2: str = "String Two"
    str3: str = "String Three"
    str4: str = "String Four"

    def string_concat_using_plus_operator(self) -> str:
        """String Concatenation using + operator method """
        return self.str1 + " " + self.str2 + " " + self.str3 + " " + self.str4


    def string_concat_using_join(self) -> str:
        """String concatenation using join method """
        # Adding all strings into a list/array
        mystrings: list[str] = [self.str1,self.str2,self.str3,self.str4]

        # Created an empty array
        process_strings: list[str] = [' ']

        # Running a loop to append list with specifier
        for str_specifier in mystrings:
            process_strings.append(str_specifier)
            process_strings.append(" ")

        # Using join to concatenate at one go to generate final string.
        final_str: str = ''.join(process_strings)

        return final_str

if __name__ == '__main__':
    sc_instance = StringConcatenations()
    result_str: str = sc_instance.string_concat_using_plus_operator()

    print(result_str)

    joined_strings: str = sc_instance.string_concat_using_join()
    print(joined_strings)
