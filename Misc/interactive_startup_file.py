"""Module for Interactive startup file execution """
import os

class InteractiveStartupFileExec:
    """Interactive Startup file exec class """
    file_name: str | None

    def __init__(self) -> None:
        self.file_name = os.environ.get('PYTHONSTARTUP')

    def startup_file_exe(self) -> None:
        """Start up file exe method """
        try:
            startup_file: str

            if self.file_name and os.path.isfile(self.file_name):
                with open(self.file_name, encoding="UTF-8") as file_handle:
                    startup_file = file_handle.read()
                exec(startup_file)
            else:
                print("No startup file found. ")
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)

if __name__ == '__main__':
    isfe_instance = InteractiveStartupFileExec()
    isfe_instance.startup_file_exe()
