""" Module for encoding and decoding json contents """

import json

class JsonOperations:
    """Json operations class """

    encoded_json: str = ''
    decoded_json: str = ''
    dct: dict[str, bool | int]

    def encoding_json(self, input_data: dict[str, float | int] ) -> str:
        """Encoding json method """
        # Compact encoding
        self.encoded_json: str = json.dumps(input_data,
                                            separators=(',',':'), sort_keys=True, indent=4)
        return self.encoded_json

    def decoding_json(self):
        """Decoding json method """
        # Basic decoding
        self.decoded_json = json.loads(self.encoded_json)
        return self.decoded_json

    def specialized_decoding_json(self,
                                  data_dict :
                                  dict[str, bool | int]) -> complex | dict[str, bool | int]:
        """Specialized decoding json method """
        self.dct = data_dict
        if '__complex__' in self.dct :
            return complex(self.dct["real"], self.dct['imag'])
        return self.dct


if __name__ == '__main__':
    try:
        json_ops_instance = JsonOperations()
        json_data : dict[str, float | int] = {'Height':5.3, 'Weight': 65}  # Json data
        print("Original Data: ", json_data)
        print("After encoding : ", json_ops_instance.encoding_json(json_data))
        print("After decoding: ", json_ops_instance.decoding_json())
        json_str: dict[str, bool | int] = {"__complex__": True, "real": 1, "imag": 2}
        print(json_ops_instance.specialized_decoding_json(json_str))
    except TypeError as type_error:
        print(type_error)
    except RecursionError as recursion_error:
        print(recursion_error)
    except json.JSONDecodeError as json_decode_error:
        print(json_decode_error)
    except OSError as os_error:
        print(os_error)
