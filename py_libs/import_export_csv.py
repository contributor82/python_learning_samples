"""Import and export csv file"""

import pandas as pd

# Currently pd lib read csv causing an error.


class PandaUse:
    """Panda Use class for csv file import & export"""
    name: str = ""

    def __init__(self) -> None:
        """Constructor of pandas class"""
        self.name = "pandas"

    def print_name(self) -> None:
        """Prints the name of the class"""
        print("Name is : ", self.name)

    def read_csv_file(self, file_name: str) -> None:
        """Read csv file"""
        print("Reading csv, file name: ", file_name)
        arr = pd.read_csv(file_name, header=0).values  # type : ignore
        print("Array from csv file: ", arr)  # type : ignore

    def read_csv_file_cols(self, file_name: str) -> None:
        """Read csv file columns"""
        print("Reading csv, file name: ", file_name)
        arr = pd.read_csv(file_name,  # type : ignore
                          usecols=['Artist', 'Plays']).values  # type : ignore
        print("Array from csv file: ", arr)  # type : ignore


if __name__ == "__main__":
    import_export_csv_instance = PandaUse()
    import_export_csv_instance.print_name()
    import_export_csv_instance.read_csv_file('C:\\Data\\music.csv')
    import_export_csv_instance.read_csv_file_cols('C:\\Data\\music.csv')
