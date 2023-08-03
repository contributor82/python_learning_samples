
# Listing files in a specific directory. 

import glob

class FileWildCards: 

    def example_one(self) -> None: 
        # Example One
        data_structure_files = glob.glob('DataStructures\\*.*')
        print(data_structure_files)

    def example_two(self) -> None: 
        # Example Two
        python_files = glob.glob('C:\\Data\\*.py')

        print(python_files)

if __name__ == '__main__': 
    fwc_instance = FileWildCards()
    fwc_instance.example_one()
    fwc_instance.example_two()