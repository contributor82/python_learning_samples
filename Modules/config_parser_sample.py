import configparser

# Customize conversion of values by specifying a dictionary of converters from python docs.
class ConfigParserSample: 
    conv = {}
    cfg = None

    # Initializing converters map by lambda expression
    def __init__(self) -> None:
        self.conv['list'] = lambda v: [e.strip() for e in v.split() if e.strip()]
        self.cfg = configparser.ConfigParser(converters=self.conv)
    
    # reading input string 
    def input_string(self, inputStr: str) -> None: 
        try: 
            self.cfg.read_string(inputStr)
        except Exception as ex:
            print(ex)

    # Getting an option value for a given section 
    def get_string(self) -> None:
        try:   
            outStr: str = self.cfg.get('s', 'list')
            print(outStr)
        except Exception as ex:
            print(ex)
    
    # Getting section
    def get_section(self, sectionName: str) -> None:
        try:   
            section = self.cfg[sectionName]
            print("Section : ", section)
        except Exception as ex:
            print(ex)
    
    # Checking if section present
    def is_section_present(self, sectionName: str) -> None: 
        hasSection = self.cfg.has_section(sectionName)
        print(hasSection)

if __name__ == '__main__': 
    cpInstance = ConfigParserSample()
    cpInstance.input_string(""" [s] 
                                list = a b c d e f g """)
    cpInstance.get_string() 
    cpInstance.is_section_present("s")
    cpInstance.get_section("s")