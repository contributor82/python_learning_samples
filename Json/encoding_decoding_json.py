# Encoding and decoding Json contents. 

import json

class JsonOperations: 
    data = {'Height':5.3, 'Weight': 65}  # Json data
    encoded_json = ''
    decoded_json = ''
    dct = ''
    
    def encoding_json(self) -> str: 

        # Compact encoding 
        self.encoded_json = json.dumps(self.data, separators=(',',':'), sort_keys=True, indent=4)
        return self.encoded_json
    
    def decoding_json(self): 
        # Basic decoding
        self.decoded_json = json.loads(self.encoded_json)
        return self.decoded_json
    
    def specialized_decoding_json(self, dict : dict[str, bool | int]) -> complex | dict[str, bool | int]: 
        self.dct = dict
        if '__complex__' in self.dct : 
            return complex(self.dct["real"], self.dct['imag'])
        return self.dct
    

if __name__ == '__main__':
    json_ops_instance = JsonOperations()
    print("Original Data: ", json_ops_instance.data)
    print("After encoding : ", json_ops_instance.encoding_json())
    print("After decoding: ", json_ops_instance.decoding_json())
    json_str = {"__complex__": True, "real": 1, "imag": 2}
    print(json_ops_instance.specialized_decoding_json(json_str))

