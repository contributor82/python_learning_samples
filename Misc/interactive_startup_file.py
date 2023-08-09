
import os

class InteractiveStartupFileExec:

    def startup_file_exe(self):
        file_name = os.environ.get('PYTHONSTARTUP')
        if file_name and os.path.isfile(file_name):
            with open(file_name) as file_handle:
                startup_file = file_handle.read()
            exec(startup_file)
        else:
            print("No startup file found. ")


 if __name__ == '__main__':
    isfe_instance = InteractiveStartupFileExec()
    isfe_instance.startup_file_exe()
