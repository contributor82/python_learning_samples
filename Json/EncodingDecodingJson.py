# Encoding and decoding Json contents. 

import json

class JsonOperations: 
    data = {'Height':5.3, 'Weight': 65}  # Json data
    encoded_json = ''
    decoded_json = ''
    dct = ''
    
    def encoding_json(self): 

        # Compact encoding 
        self.encoded_json = json.dumps(self.data, separators=(',',':'), sort_keys=True, indent=4)
        return self.encoded_json
    
    def decoding_json(self): 
        # Basic decoding
        self.decoded_json = json.loads(self.encoded_json)
        return self.decoded_json
    
    def specialized_decoding_json(self, dict): 
        self.dct = dict
        if '__complex__' in self.dct : 
            return complex(self.dct["real"], self.dct['imag'])
        return self.dct
    

jsonOperationsInstance = JsonOperations()

print("Original Data: ", jsonOperationsInstance.data)

print("After encoding : ", jsonOperationsInstance.encoding_json())

print("After decoding: ", jsonOperationsInstance.decoding_json())


jsonStr = {"__complex__": True, "real": 1, "imag": 2}

print(jsonOperationsInstance.specialized_decoding_json(jsonStr))

