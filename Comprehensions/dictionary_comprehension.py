
class DictionaryComprehensions: 
    ### Dictionary Comprehensions class ###

    # Here a number will be taken from the given range
    # it will start making its square. 
    def get_dict_comprehension(self, rangeValue: int) -> dict[int, int]: 
        ### dict comprehensions ###
        return {num: num ** 2 for num in range(rangeValue)}

if __name__ == '__main__':
    dc_instance = DictionaryComprehensions()
    print("Dictionary comprehension for the given range: ", dc_instance.get_dict_comprehension(10))
