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
        for strSpecifier in mystrings: 
            process_strings.append(strSpecifier)
            process_strings.append(" ")

        # Using join to concatenate at one go to generate final string. 
        finalStr = ''.join(process_strings)

        return finalStr

if __name__ == '__main__': 
    scInstance = StringConcatenations()
    resultStr = scInstance.string_concat_using_plus_operator()

    print(resultStr)

    joinedStrings = scInstance.string_concat_using_join()
    print(joinedStrings)
