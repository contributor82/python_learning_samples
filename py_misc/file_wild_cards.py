"""Module for file wild cards """
# Listing files in a specific directory.

import glob

class FileWildCards:
    """File wild cards class """
    def example_one(self, path_name: str) -> None:
        """Example One wild card method """
        data_structure_files: list[str] = glob.glob(path_name)
        print(data_structure_files)

    def example_two(self, file_type_and_path: str) -> None:
        """Example One wild card method """
        python_files: list[str] = glob.glob(file_type_and_path)
        print(python_files)

if __name__ == '__main__':
    fwc_instance = FileWildCards()
    fwc_instance.example_one('DataStructures\\*.*')
    fwc_instance.example_two('C:\\Data\\*.py')
