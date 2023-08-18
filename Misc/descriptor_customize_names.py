"""Module for descriptor manyears_old attribute """
import logging

# Converts function into bound methods

logging.basicConfig(level=logging.INFO)

class LoggedAccess:
    """Logged Access """
    public_make : str
    private_make : str
    # def __init__(self) -> None:
    #     """Initializing logging """

    def __set_name__(self, owner: object, make: str) -> None:
        self.public_make = make
        self.private_make = "_" + make

    def __get__(self, obj: object, objtype: object | None = None)-> None | object:
        """Logging and getting  years_old """
        value = getattr(obj, self.private_make) # Getting a maked attribute
        logging.info('Accessing %r giving %r', self.public_make, value)
        return value

    def __set__(self, obj: object, value: object) -> None:
        """Logging and setting persson years_old """
        logging.info('Updating %r to %r', self.public_make, value)
        setattr(obj, self.private_make, value) # Sets the maked attribute


class Vehicle:
    """Vehicle class """
    make: object | None = LoggedAccess()
    years_old: object | None = LoggedAccess()

    def __init__(self, vehicle_make: str, vehicle_years_old: int) -> None:
        """Initializing years_old and make """
        self.make = vehicle_make
        self.years_old = vehicle_years_old


    def birthday(self) -> None:
        """Vehicle's birthday so increasing years_old by one """
        self.years_old = self.years_old + 1 #type: ignore

    def display_vehicle_dtls(self)-> None:
        """Display person details """
        print("make: ", self.make, " years_old: ", self.years_old)

if __name__ == '__main__':
    vars(vars(Vehicle)['make'])
    vars(vars(Vehicle)['years_old'])
    vehicle_first_instance = Vehicle('Vehicle one', 26)
    # print("Using Manyears_old attribute: Vehicle make: ",
    #       vehicle_one.make, " years_old: ", vehicle_one.years_old) #type: ignore
    vehicle_first_instance.birthday()
    vehicle_first_instance.display_vehicle_dtls()
    # print("After birthday call, Vehicle make: ",
    #       vehicle_one.make, " years_old: ", vehicle_one.years_old) #type: ignore
    vehicle_second_instance = Vehicle('Vehicle second', 28)
    vehicle_second_instance.birthday()
    vehicle_second_instance.display_vehicle_dtls()
