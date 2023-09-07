"""Module for Client One """
from facade_class import Facade

class ClientOne:
    """Client one class"""
    generate_request: Facade

    def __init__(self) -> None:
        self.generate_request = Facade()


    def create_request(self)-> None:
        """create request """
        self.generate_request.get_client_request(['One','Two'])

    def process_request(self)-> None:
        """Process request """
        self.generate_request.process_client_request()

if __name__ == '__main__':
    client_one = ClientOne()
    client_one.create_request()
    client_one.process_request()
