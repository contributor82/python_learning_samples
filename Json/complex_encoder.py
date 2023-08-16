""" Module for Complex json encoder """
import json

class ComplexEncoder(json.JSONEncoder):
    """ class ComplexEncoder has not been recognized. """

    def default(self, o: object) -> object:
        """ default for checking object complexity """
        if isinstance(o,complex):
            return [o.real, o.imag]
        return json.JSONEncoder.default(self, o)


if __name__ == '__main__':
    try:
        complex_encode_instance = ComplexEncoder()
        # ComplexEncoder type is not recognized.
        print( json.dumps(2+ 1j, cls=type(complex_encode_instance)))
        complex_encode_instance.encode(2+1j)
        lst = list(complex_encode_instance.iterencode(2+1j))
        print(lst)
    except ValueError as value_error:
        print(value_error)
    except TypeError as type_error:
        print(type_error)
    except RecursionError as recursion_error:
        print(recursion_error)
    except OSError as os_error:
        print(os_error)
