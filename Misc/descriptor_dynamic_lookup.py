"""Module for descriptor protocol """
import os

# Dynamic lookup
class DirectorySize:
    """ Directory size """
    dir_list: list[str]

    def __get__(self, obj: object, objtype : object | None = None) -> int:
        """get directory size """
        self.dir_list = os.listdir(obj.dir_path) # type: ignore
        return len(self.dir_list) # type: ignore

    def display_dir_list(self)-> None:
        """Display directory size"""
        print('Directory list : ', self.dir_list)


class Directory:
    """ Directory """
    dir_size = DirectorySize()
    dir_path: str

    def __init__(self, dirpath: str) -> None:
        """Initializing dir"""
        self.dir_path = dirpath

    def display_dir_path(self)-> None:
        """Display directory path """
        print('Directory path : ', self.dir_path)

    def display_dir_size(self)-> None:
        """Display directory size """
        print('Directory size: ', self.dir_size)


if __name__ == '__main__':

    input_dir_path: str = 'C:\\Data'
    dir_instance = Directory(input_dir_path)
    # A call to _get_ will be placed upon dir_size member invocation.
    # Directory instance will also be passed with it to access its members
    # Pulling the number of files present in the given directory path.
    # print('Directory size: ", dir_instance.dir_size) # type: ignore
    dir_instance.display_dir_path()
    dir_instance.display_dir_size()
