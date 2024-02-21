"""Module for KM to miles converter"""


class KMToMilesConverter:
    """ Class for KM to Miles Converter """
    kms: float

    def __init__(self, kilometers: float) -> None:
        self.kms = kilometers

    def convert_km_to_miles(self) -> float:
        """Conversion of km to miles"""
        km_to_miles_conv_factor = 0.621371

        miles: float = self.kms * km_to_miles_conv_factor

        return miles


if __name__ == '__main__':
    kms = float(input('Enter kilometers: '))
    km_to_miles_converter = KMToMilesConverter(kms)
    miles = km_to_miles_converter.convert_km_to_miles()

    print(f' Kilometers : {kms} Miles: {miles}')
