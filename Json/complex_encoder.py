""" Module for Complex json encoder """
import json

class ComplexEncoder(json.JSONEncoder):
    """ class ComplexEncoder has not been recognized. """

    def default(self, obj: object) -> any:
        """ default for checking object complexity """
        if isinstance(obj,complex):
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':

    complex_encode_instance = ComplexEncoder()
    # ComplexEncoder type is not recognized.
    print( json.dumps(2+ 1j, cls=type(complex_encode_instance)))
    complex_encode_instance.encode(2+1j)
    lst = list(complex_encode_instance.iterencode(2+1j))
    print(lst)
