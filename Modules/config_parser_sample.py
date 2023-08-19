"""Module for configuration parser """
import configparser

# Customize conversion of values by specifying a dictionary of converters from python docs.

class ConfigParserSample:
    """ Config parser sample class """

    conv: dict[object, object] = {}
    cfg : configparser.ConfigParser

    def __init__(self) -> None:
        """Initializing converters """
        self.conv['list']  = lambda input_str : [process_str.strip() # type: ignore
                                                 for process_str in input_str.split() # type: ignore
                                                 if process_str.strip()]# type: ignore
        self.cfg = configparser.ConfigParser(converters=self.conv) # type: ignore

    # reading input string
    def input_string(self, input_str: str) -> None:
        """ Function to read input string """

        try:
            self.cfg.read_string(input_str)
        except configparser.ParsingError as parse_error:
            print(parse_error)
        except configparser.Error as config_parse_error:
            print(config_parse_error)

    # Getting an option value for a given section
    def get_string(self) -> None:
        """ Function to get an option value for a given section """
        try:
            out_str: str = self.cfg.get('s', 'list')
            print(out_str)
        except configparser.ParsingError as parse_error:
            print(parse_error)
        except configparser.Error as config_parse_error:
            print(config_parse_error)

    # Getting section
    def get_section(self, section_name: str) -> None:
        """ Function to get section """

        try:
            cfg_section : None | configparser.SectionProxy = self.cfg[section_name]
            print('Section : ', cfg_section)
        except configparser.NoSectionError as no_section_error:
            print(no_section_error)
        except configparser.Error as config_parse_error:
            print(config_parse_error)

    # Checking if section present
    def is_section_present(self, section_name: str) -> None:
        """ Function to check if section is present """

        has_section: bool = self.cfg.has_section(section_name)
        print(has_section)


if __name__ == '__main__':
    cp_instance = ConfigParserSample()
    cp_instance.input_string(''' [s]
                                list = a b c d e f g ''')
    cp_instance.get_string()
    cp_instance.is_section_present('s')
    cp_instance.get_section('s')
