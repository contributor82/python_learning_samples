

class DictionaryComprehensions: 

    # Here a number will be taken from the given range
    # it will start making its square. 
    def get_dict_comprehension(self, rangeValue): 

        return {num: num ** 2 for num in range(rangeValue)}

dcInstance = DictionaryComprehensions()
print("Dictionary comprehension for the given range: ", dcInstance.get_dict_comprehension(10))
