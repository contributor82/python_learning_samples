"""Module for Operating system interface """
import os

class OperatingSystemInterface:
    """Operating system interface class """
    def get_current_working_dir(self) -> str:
        """Getting current working directory method """
        return os.getcwd()

    def get_module_func_list(self) -> list[str]:
        """Getting module functions list method """
        return dir(os)

    #def get_module_help(self) -> None:
    #    """Getting module help """
    #    print('Module Help: ', help(os))

if __name__ == '__main__':
    os_interface_instance = OperatingSystemInterface()
    print('Current Working directory: ', os_interface_instance.get_current_working_dir())
    print('Module Functions list: ', os_interface_instance.get_module_func_list())
    # os_interface_instance.get_module_help()
