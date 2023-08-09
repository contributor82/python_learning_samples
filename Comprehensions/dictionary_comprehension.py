
class DictionaryComprehensions: 
    ### Dictionary Comprehensions class ###

    def get_dict_comprehension(self, range_val: int) -> dict[int, int]: 
        ### dict comprehensions ###
        # Here a number will be taken from the given range
        # it will start making its square. 
        return {num: num ** 2 for num in range(range_val)}

if __name__ == '__main__':
    dc_instance = DictionaryComprehensions()
    print("Dictionary comprehension for the given range: ", dc_instance.get_dict_comprehension(10))
