
# Listing files in a specific directory. 

import glob

class FileWildCards: 

    def example_one(self, path_name: str) -> None: 
        # Example One
        data_structure_files = glob.glob(path_name)
        print(data_structure_files)

    def example_two(self, file_type_and_path: str) -> None: 
        # Example Two
        python_files = glob.glob(file_type_and_path)

        print(python_files)

if __name__ == '__main__': 
    fwc_instance = FileWildCards()
    fwc_instance.example_one('DataStructures\\*.*')
    fwc_instance.example_two('C:\\Data\\*.py')