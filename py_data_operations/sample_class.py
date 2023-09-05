"""Module for sample class"""

class SampleClass:
    """ Sample class """
    sample_int: int
    sample_str: str

    def __init__(self) -> None:
        """ Initialize Sample class members """
        self.sample_int = 0
        self.sample_str = 'Sample class'

    def get_sample_int(self)-> int:
        """ Get sample int method """
        return self.sample_int

    def get_sample_str(self)-> str:
        """ Get sample str method """
        return self.sample_str


if __name__ == '__main__':
    sample_class_instance = SampleClass()
