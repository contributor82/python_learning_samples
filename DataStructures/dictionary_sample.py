""" Module for Dictionary sample """

class DictionarySample:
    """Dictionary Sample class"""

    def dictioanry_merge(self, input_dict_x : dict[str, object],
                         input_dict_y: dict[str, object])-> dict[str, object] | RuntimeError:
        """ Dictionary Merge method """
        result : dict[str, object] | RuntimeError
        try:
            result = input_dict_x | input_dict_y
        except RuntimeError as run_time_error:
            result = run_time_error
        return result

    def create_dictionary(self, input_keys: list[str],
                          input_values: list[object] )-> dict[str, object] | RuntimeError:
        """ Create a dictionary """
        result : dict[str, object] | RuntimeError
        try:
            result =  dict(zip(input_keys, input_values))
        except RuntimeError as run_time_error:
            result = run_time_error
        return result

    def sort_dictionary(self, input_dict:
                                 dict[str, object]) -> dict[str,object] | RuntimeError:
        """ Sort dictionary elements """
        sorted_dict: dict[str, object] = {'':''}
        result : dict[str, object] | RuntimeError
        try:
            for key, val in sorted(input_dict.items()):
                sorted_dict[key] = val
            del sorted_dict['']
            result = sorted_dict
        except RuntimeError as run_time_error:
            result = run_time_error
        return result

    def reverse_dictionary(self,
                           input_dict: dict[str, object]) ->  dict[str, object] | RuntimeError:
        """ Reverse dictionary content order """
        dict_reversed: dict[str, object] = {'':''}
        result : dict[str, object] | RuntimeError
        try:
            for key, val in reversed(input_dict.items()):
                dict_reversed[key] = val
            del dict_reversed['']
            result = dict_reversed
        except RuntimeError as run_time_error:
            result = run_time_error
        return result

    def get_dictionary_item(self,
                            input_dict: dict[str, object]) ->  tuple[str, object] | RuntimeError:
        """Get dictionary item """
        item: tuple[str, object] | RuntimeError
        try:
            item = input_dict.popitem()
        except RuntimeError as run_time_error:
            item = run_time_error
        return item



if __name__ == '__main__':

    dict_sample_instance = DictionarySample()

    dict_x:dict[str, object] = {"Key1": "Value1 from X", "Key2": "Value2 from X"}
    dict_y:dict[str, object] = {"Key3": "Value3 from Y", "Key4": "Value4 from Y"}

    print(" Dictionary X: ", dict_x)
    print(" Dictionary Y: ", dict_y)
    dict_merge:dict[str,object] | RuntimeError = dict_sample_instance.dictioanry_merge(dict_x,
                                                                                        dict_y)
    print("Merged Dictionary : ", dict_merge)

    str_list: list[str] = ['one', 'two', 'three']
    num_list: list[object] = [1,2,3]

    print(" Key List: ", str_list)
    print(" Value List: ", num_list)
    new_dict:dict[str,object] | RuntimeError = dict_sample_instance.create_dictionary(str_list,
                                                                                       num_list)
    print("Creating Dictionary from Keys & Values list : ", new_dict)

    print("Dictionary before reversing elements: ", dict_x)
    reverse_dict:dict[str, object] | RuntimeError =  dict_sample_instance.reverse_dictionary(dict_x)
    print("Dictionary after reversing elements: ", reverse_dict)

    dict_x.clear()
    dict_x = {"Key1": "Value1 from X", "Key2": "Value2 from X",
              "Key4": "Value4 from X", "Key3": "Value3 from X"}

    print("Dictionary before sorting : ", dict_x)
    sort_dict:dict[str,object] | RuntimeError =  dict_sample_instance.sort_dictionary(dict_x)
    print("Dictionary after sorting : ", sort_dict)

    vehicle_types: dict[str, object] = {"Type1": "Two wheeler", "Type2": "Three wheeler",
                                        "Type3": "Four wheeler", "Type4": "Six wheeler",
                                        "Type5": "Eight Wheeler"}
    print("Dictionary as input : ", vehicle_types)
    vehicle_item:tuple [str,object]|RuntimeError = dict_sample_instance.get_dictionary_item(
        vehicle_types)
    print("Popped item from dictionary: ", vehicle_item)
