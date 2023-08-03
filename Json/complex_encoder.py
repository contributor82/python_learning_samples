# Complex Json Encoder
import json

# class ComplexEncoder has not been recognized. 

class ComplexEncoder(json.JSONEncoder): 

    def default(self, obj: complex) -> any: 
        if isinstance(obj,complex): 
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)
    

if __name__ == '__main__': 

    complex_encode_instance = ComplexEncoder()
    print( json.dumps(2+ 1j, cls=type(complex_encode_instance)  ))  # ComplexEncoder type is not recognized. 
    complex_encode_instance.encode(2+1j)
    lst = list(complex_encode_instance.iterencode(2+1j))
    print(lst)
