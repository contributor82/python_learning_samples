"""Module for string format mapping """
# Here Default class has been created accepting dictionary Key Value pair and returns a pair.
# String formmat_mpa further grabs key and maps with associated value.

class Default(dict[str, int| str]):
    """Default class """
    def __missing__(self, key: object) -> object:
        return key

if __name__ == '__main__':
    input_str: str = "{name} is from {country}"
    print(input_str.format_map(Default(name="John", country="USA")))
    print(Default(one=1))
