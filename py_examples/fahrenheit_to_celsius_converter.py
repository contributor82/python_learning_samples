"""Fahrenheit to Celsius converter """


class FtoCConverter:
    """Fahrenheit to celsius converter"""
    fahrenheit: float

    def __init__(self, f_value: float) -> None:
        """Initialize defaults"""
        self.fahrenheit = f_value

    def f_to_c_conversion(self) -> float:
        """Fahrenheit to celsius conversion"""
        celsius = (self.fahrenheit - 32) / 1.8

        return celsius


if __name__ == '__main__':
    fahrenheit: float = float(input("Enter fahrenheit value : "))
    f_to_c_converter = FtoCConverter(fahrenheit)
    celsius = f_to_c_converter.f_to_c_conversion()
    print(f' Fahrenheit : {fahrenheit} Celsius : { celsius}')
