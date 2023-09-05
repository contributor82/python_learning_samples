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
                # event == pulldom.START_DOCUMENT and
                if node.nodeName == element: # type: ignore
                    search_xml_document.expandNode(node) #type: ignore
                    node_occurrences.append(node) #type: ignore
                else:
                    if len(node.childNodes) > 0: # type: ignore
                        for child_node in node.childNodes: #type: ignore
                            if child_node.nodeName == element: #type: ignore
                                search_xml_document.expandNode(child_node) #type: ignore
                                node_occurrences.append(node) # type: ignore

        except ParseError as get_node_occ_parse_error:
            print(get_node_occ_parse_error)
        except ValueError as get_node_occ_value_error:
            print(get_node_occ_value_error)
        except TypeError as get_node_occ_type_error:
            print(get_node_occ_type_error)

        return node_occurrences

    def get_node_count(self, element: str)-> int:
        """Get node count """
        node_count: int =0
        try:
            search_xml_document: DOMEventStream = pulldom.parse(self.xml_file_path)
            for node in search_xml_document: #type: ignore
                # event == pulldom.START_DOCUMENT and
                if node.nodeName == element: # type: ignore
                    search_xml_document.expandNode(node) #type: ignore
                    node_count += 1
                else:
                    if len(node.childNodes) > 0: # type: ignore
                        for child_node in node.childNodes: # type: ignore
                            if child_node.nodeName == element: # type: ignore
                                search_xml_document.expandNode(child_node) # type: ignore
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

    print('Node Name: ', 'indentOptions')

    node_occurs: list[Element] = xml_file_ops_instance.get_node_occurrences('indentOptions')
    print('Node occurrences: ')
    for node_occ in node_occurs:
        print(node_occ.toxml())

    print('Node count: ', xml_file_ops_instance.get_node_count('indentOptions'))
