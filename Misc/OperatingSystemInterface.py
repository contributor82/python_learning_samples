import os

class OperatingSystemInterface: 

    def get_current_working_dir(self): 
        return os.getcwd()
    
    def get_module_func_list(self): 
        return dir(os)
    
    def get_module_help(self): 
        return help(os)
    

osInterfaceInstance = OperatingSystemInterface()
print("Current Working directory: ", osInterfaceInstance.get_current_working_dir())
    
print("Module Functions list: ", osInterfaceInstance.get_module_func_list())

print("Module Help: ", osInterfaceInstance.get_module_help())