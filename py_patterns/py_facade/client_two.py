"""Module for Client Two """
from facade_class import Facade

class ClientTwo:
    """Client two class"""
    generate_request: Facade

    def __init__(self) -> None:
        """Initializing generate request """
        self.generate_request = Facade()

    def create_request(self)-> None:
        """create request """
        self.generate_request.get_client_request(['Two','Four'])

    def process_request(self)-> None:
        """Process request """
        self.generate_request.process_client_request()

if __name__ == '__main__':
    client_two = ClientTwo()
    client_two.create_request()
    client_two.process_request()
