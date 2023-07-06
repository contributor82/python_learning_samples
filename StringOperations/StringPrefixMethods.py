
class StringPrefixMethods: 
    
    def string_removeprefix(self, originalStr, prefixStr):
        return originalStr.removeprefix(prefixStr)

    def string_removesuffix(self, originalStr, suffixStr):
        return originalStr.removesuffix(suffixStr)


spmInstance = StringPrefixMethods()

originalStr = "TestAdded" 
print("Original String: ", originalStr, " String After Removing prefix 'Test' using removeprefix string method. ", spmInstance.string_removeprefix(originalStr,"Test") ) 
print("Original String: ", originalStr, " String After Removing suffix 'Added' using removesuffix string method. ", spmInstance.string_removesuffix(originalStr,"Added")) 


