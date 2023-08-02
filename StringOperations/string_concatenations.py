# String Concatenation approach

class StringConcatenations: 

    str1 = "String One"
    str2 = "String Two"
    str3 = "String Three"
    str4 = "String Four"

    def string_concat_using_plus_operator(self) -> str: 
        # String Concatenation
        return self.str1 + " " + self.str2 + " " + self.str3 + " " + self.str4

    
    def string_concat_using_join(self) -> str: 
        # Adding all strings into a list/array
        mystrings = [self.str1,self.str2,self.str3,self.str4]

        # Created an empty array
        process_strings = [' ']

        # Running a loop to append list with specifier 
        for str_specifier in mystrings: 
            process_strings.append(str_specifier)
            process_strings.append(" ")

        # Using join to concatenate at one go to generate final string. 
        final_str = ''.join(process_strings)

        return final_str

if __name__ == '__main__': 
    sc_instance = StringConcatenations()
    result_str = sc_instance.string_concat_using_plus_operator()

    print(result_str)

    joined_strings = sc_instance.string_concat_using_join()
    print(joined_strings)
