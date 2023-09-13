"""Module for decorator client """

from decorator_wrapper import DecoratorWrapper

class DecoratorClient:
    """Decoratort client class """
    decorator_wrapper: DecoratorWrapper

    def __init__(self) -> None:
        """Initializing decorator wrapper """
        self.decorator_wrapper = DecoratorWrapper()

    def update_system(self)-> None:
        """Update system """
        self.decorator_wrapper.update_system()

if __name__ == "__main__":
    decorator_client_instance =  DecoratorClient()
    decorator_client_instance.update_system()
