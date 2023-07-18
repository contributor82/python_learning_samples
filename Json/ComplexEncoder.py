# Complex Json Encoder
import json

# class ComplexEncoder has not been recognized. 

class ComplexEncoder(json.JSONEncoder): 

    def default(self, obj): 
        if isinstance(obj,complex): 
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)
    

if __name__ == '__main__': 

    complexEncoderInstance = ComplexEncoder()
    print( json.dumps(2+ 1j, cls=type(complexEncoderInstance)  ))  # ComplexEncoder type is not recognized. 
    complexEncoderInstance.encode(2+1j)
    lst = list(complexEncoderInstance.iterencode(2+1j))
    print(lst)
