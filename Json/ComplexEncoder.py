# Complex Json Encoder
import json

# class ComplexEncoder has not been recognized. 

class ComplexEncoder(json.JSONEncoder): 

    def default(self, obj): 
        if isinstance(obj,complex): 
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)
    
    # print( json.dumps(2+ 1j, cls=  ComplexEncoder  )) - ComplexEncoder type is not recognized. 

    # ComplexEncoder().encode(2 + 1j)

    # list(ComplexEncoder().iterencode(2 + 1j))