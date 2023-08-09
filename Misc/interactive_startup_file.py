"""Module for Interactive startup file execution """
import os

class InteractiveStartupFileExec:
    """Interactive Startup file exec class """

    def startup_file_exe(self) -> None:
        """Start up file exe method """
        try:
            file_name: str | None = os.environ.get('PYTHONSTARTUP')
            if file_name and os.path.isfile(file_name):
                with open(file_name, encoding="UTF-8") as file_handle:
                    startup_file: str = file_handle.read()
                exec(startup_file)
            else:
                print("No startup file found. ")
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)

if __name__ == '__main__':
    isfe_instance = InteractiveStartupFileExec()
    isfe_instance.startup_file_exe()
