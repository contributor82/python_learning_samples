import configparser

# Customize conversion of values by specifying a dictionary of converters from python docs.


class ConfigParserSample:
    ### Config parser sample class ###

    conv: dict[object, object] = {}
    cfg = None

    # Initializing converters map by lambda expression
    def __init__(self) -> None:
        self.conv['list'] = lambda v: [e.strip()
                                       for e in v.split() if e.strip()]
        self.cfg = configparser.ConfigParser(converters=self.conv)

    # reading input string
    def input_string(self, input_str: str) -> None:
        ### Function to read input string ###

        try:
            self.cfg.read_string(input_str)
        except Exception as ex:
            print(ex)

    # Getting an option value for a given section
    def get_string(self) -> None:
        ### Function to get an option value for a given section ###
        try:
            outStr: str = self.cfg.get('s', 'list')
            print(outStr)
        except Exception as ex:
            print(ex)

    # Getting section
    def get_section(self, section_name: str) -> None:
        ### Function to get section ###

        try:
            section : None | configparser.SectionProxy = self.cfg[section_name]
            print("Section : ", section)
        except Exception as ex:
            print(ex)

    # Checking if section present
    def is_section_present(self, section_name: str) -> None:
        ### Function to check if section is present ###

        hasSection: bool = self.cfg.has_section(section_name)
        print(hasSection)


if __name__ == '__main__':
    cp_instance = ConfigParserSample()
    cp_instance.input_string(""" [s] 
                                list = a b c d e f g """)
    cp_instance.get_string()
    cp_instance.is_section_present("s")
    cp_instance.get_section("s")
