"""Module for XML file operations"""
from xml.dom import pulldom
from xml.dom.minidom import Element
from xml.dom.pulldom import DOMEventStream
# import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError # Element,

class XMLFileOperations:
    """XML File operations class """
    xml_file_path: str = ''

    def __init__(self, file_path: str) -> None:
        """Initializing xml file path"""
        self.xml_file_path = file_path

    def parse_xml(self) -> None:
        """Parse XML document"""
        try:
            xml_document: DOMEventStream  = pulldom.parse(
                self.xml_file_path) # ET.parse(self.xml_file_path)
            for event, node in xml_document: #type: ignore
                if event == pulldom.START_ELEMENT:
                    xml_document.expandNode(node) #type: ignore
                    print(node.toxml()) #type: ignore
        except ParseError as xml_parse_error:
            print(xml_parse_error)
        except OSError as xml_parse_os_error:
            print(xml_parse_os_error)

    def get_node_occurrences(self, element: str)-> list[Element]:
        """Get node occurrences """
        node_occurrences: list[Element] = [Element('')]
        try:
            search_xml_document: DOMEventStream = pulldom.parse(self.xml_file_path)
            for node in search_xml_document: #type: ignore
                if node[0] == pulldom.START_ELEMENT and node[1].nodeName == element: # type: ignore
                    node_occurrences.append(node) #type: ignore
                    if len(node[1].childNodes) > 0: # type: ignore
                        for child_node in node[1].childNodes: #type: ignore
                            if child_node[1].nodeName == element: #type: ignore
                                node_occurrences.append(child_node) # type: ignore
        except ParseError as get_node_occ_parse_error:
            print(get_node_occ_parse_error)
        except ValueError as get_node_occ_value_error:
            print(get_node_occ_value_error)
        except TypeError as get_node_occ_type_error:
            print(get_node_occ_type_error)
        except AttributeError as get_node_attr_error:
            print(get_node_attr_error)

        return node_occurrences

    def get_num_of_nodes(self, element_name: str, dom_event_stream: DOMEventStream)-> int:
        """Get number of nodes """
        num_of_nodes: int =0
        for node in dom_event_stream: #type: ignore
            if node[0] == pulldom.START_ELEMENT and node[1].nodeName == element_name: # type: ignore
                dom_event_stream.expandNode(node) #type: ignore
                num_of_nodes += 1
                if len(node[1].childNodes) > 0: # type: ignore
                    for child_node in node[1].childNodes: # type: ignore
                        if child_node.nodeName == element_name: # type: ignore
                            dom_event_stream.expandNode(child_node) # type: ignore
                            num_of_nodes += 1
        return num_of_nodes


    def get_node_count(self, element: str)-> int:
        """Get node count """
        node_count: int = 0
        try:
            search_xml_document: DOMEventStream = pulldom.parse(self.xml_file_path)
            # node_count = self.get_num_of_nodes(element, search_xml_document)
            for node in search_xml_document: #type: ignore
                if node[0] == pulldom.START_ELEMENT and node[1].nodeName == element: #type: ignore
                    node_count += 1
                    if len(node[1].childNodes) > 0: #type: ignore
                        for child_node in node.childNodes: #type: ignore
                            if child_node[1].nodeName == element: #type: ignore
                                node_count += 1
        except ParseError as get_node_xml_parse_error:
            print(get_node_xml_parse_error)
        except ValueError as get_node_value_error:
            print(get_node_value_error)
        except TypeError as get_node_type_error:
            print(get_node_type_error)

        return node_count

if __name__ == '__main__':
    xml_file_ops_instance = XMLFileOperations('C:\\Data\\Project.xml')
    xml_file_ops_instance.parse_xml()
    print("\n\n ")

    print('Node Name: ', 'HTMLCodeStyleSettings')

    node_occurs: list[Element] = xml_file_ops_instance.get_node_occurrences('HTMLCodeStyleSettings')
    print('Node occurrences: ')
    index: int =0
    for node_occ in node_occurs:
        print(node_occ) # type: ignore

    print('codeStyleSettings Node count: ', xml_file_ops_instance.get_node_count('codeStyleSettings'))
