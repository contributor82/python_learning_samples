
import os

class InteractiveStartupFileExec: 

    def startup_file_exe(self): 
        filename = os.environ.get('PYTHONSTARTUP')
        if filename and os.path.isfile(filename): 
            with open(filename) as fileObj: 
                startup_file = fileObj.read()
            exec(startup_file)
        else:
            print("No startup file found. ")

 if __name__ == '__main__':  
    isfe_instance = InteractiveStartupFileExec()
    isfe_instance.startup_file_exe()
