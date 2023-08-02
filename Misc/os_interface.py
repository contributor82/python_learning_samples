import os

class OperatingSystemInterface: 

    def get_current_working_dir(self) -> str: 
        return os.getcwd()
    
    def get_module_func_list(self) -> list[str]: 
        return dir(os)
    
    def get_module_help(self) -> None: 
        return help(os)
    
if __name__ == '__main__': 
    osInterfaceInstance = OperatingSystemInterface()
    print("Current Working directory: ", osInterfaceInstance.get_current_working_dir())
    print("Module Functions list: ", osInterfaceInstance.get_module_func_list())
    print("Module Help: ", osInterfaceInstance.get_module_help())