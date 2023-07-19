
# Listing files in a specific directory. 

import glob

class FileWildCards: 

    def example_one(self) -> None: 
        # Example One
        dataStructureFiles = glob.glob('DataStructures\\*.*')
        print(dataStructureFiles)

    def example_two(self) -> None: 
        # Example Two
        pythonLearningFiles = glob.glob('C:\\MyLearning\\python-learning\\*.*')

        print(pythonLearningFiles)

if __name__ == '__main__': 
    fwcInstance = FileWildCards()
    fwcInstance.example_one()
    fwcInstance.example_two()