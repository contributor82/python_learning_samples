import os

class OperatingSystemInterface: 

    def get_current_working_dir(self) -> str: 
        return os.getcwd()
    
    def get_module_func_list(self) -> list[str]: 
        return dir(os)
    
    def get_module_help(self) -> None: 
        return help(os)
    
if __name__ == '__main__': 
    os_interface_instance = OperatingSystemInterface()
    print("Current Working directory: ", os_interface_instance.get_current_working_dir())
    print("Module Functions list: ", os_interface_instance.get_module_func_list())
    print("Module Help: ", os_interface_instance.get_module_help())