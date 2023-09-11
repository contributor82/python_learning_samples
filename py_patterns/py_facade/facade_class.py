"""Module for facade """

from sub_system import Subsystem
from subsystem_one import SubsystemOne
from subsystem_two import SubsystemTwo
from subsystem_three import SubsystemThree
from subsystem_four import SubsystemFour


class Facade:
    """Facade class"""
    sub_sys_one: SubsystemOne = SubsystemOne()
    sub_sys_two: SubsystemTwo = SubsystemTwo()
    sub_sys_three: SubsystemThree = SubsystemThree()
    sub_sys_four: SubsystemFour = SubsystemFour()
    sub_sys: Subsystem
    client_request: list[Subsystem] = []
    facade_instance: object = None

    # def __init__(self) -> None:
    #     """Initializing client request """
    #     self.client_request = []

    def __new__(cls) -> object:
        """Getting only single instance of facade """
        returnable_obj: object
        if cls.facade_instance is None:
            cls.facade_instance = super().__new__(cls)

        returnable_obj = cls.facade_instance # type: ignore
        return returnable_obj # type: ignore


    def get_client_request(self, request: list[str]) -> None:
        """Get Client Request """

        if len(request) > 0:
            for request_param in request:
                if request_param == 'One':
                    self.client_request.append(self.sub_sys_one)
                elif request_param == 'Two':
                    self.client_request.append(self.sub_sys_two)
                elif request_param == 'Three':
                    self.client_request.append(self.sub_sys_three)
                elif request_param == 'Four':
                    self.client_request.append(self.sub_sys_four)
        else:
            print('No request available')


    def process_client_request(self) -> None:
        """Process Client Request """

        if len(self.client_request) > 0: # type: ignore
            for request_item in self.client_request:
                if request_item is self.sub_sys_one:
                    self.sub_sys_one.operation_one()
                elif request_item is self.sub_sys_two:
                    self.sub_sys_two.operation_one()
                    self.sub_sys_two.operation_two()
                elif request_item is self.sub_sys_three:
                    self.sub_sys_three.operation_one()
                    self.sub_sys_three.operation_two()
                    self.sub_sys_three.operation_three()
                elif request_item is self.sub_sys_four:
                    self.sub_sys_four.operation_one()
                    self.sub_sys_four.operation_two()
                    self.sub_sys_four.operation_three()
                    self.sub_sys_four.operation_four()
                else:
                    print('No request')


if __name__ == '__main__':
    facade_instance = Facade()
