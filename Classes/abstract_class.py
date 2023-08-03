from abc import ABC, abstractmethod

# Abstarct class Car
class Car(ABC): 

    @abstractmethod
    def get_name(self)-> str: 
        return "Car: Abstract"

    @classmethod
    def get_num_wheels(self) -> int: 
        return 0 

    @classmethod
    def get_num_doors(self) -> int: 
        return 0

    #@classmethod
    #def __subclasshook__(cls, __subclass: type):
    #    result = None
    #    if cls is Car: 
    #        if any("get_name" in B.__dict__ for B in __subclass.__mro__): 
    #            result = True
    #        else: 
    #            result = NotImplemented

    #    return result    

    class Subclass:  

        @classmethod
        def get_name(self)-> str: 
            return "Sub class"
            
            

# Derived class Sedan from Abstract class Car
class Sedan(Car): 
    wheels: int = 2
    doors: int = 4

    @classmethod
    def get_name(self)-> str: 
        return "sedan"

    @classmethod
    def get_num_wheels(self) -> int: 
        return self.wheels

    @classmethod
    def get_num_doors(self)-> int: 
        return self.doors

# Registering virtual subclass of ABC as Car's Subclass
Car.register(Car.Subclass) # registers virtual subclass of ABC

if __name__ == '__main__': 
    print("Abstract class Car: Is instance created : ", isinstance((), Car))
    sedan_instance = Sedan()

    if isinstance(sedan_instance, Sedan): 
        print("Derived class Sedan instance created" )
        print("Sedan doors: ", sedan_instance.get_num_doors())
        print("Sedan wheels: ", sedan_instance.get_num_wheels())
        print("get_name call ", sedan_instance.get_name())

        print("Is Car.Subclass is a subclass", issubclass(Car.Subclass, ABC))
        subclass_instance =  Car.Subclass()
        if isinstance(subclass_instance, Car.Subclass): 
            print("Abstract class Car's subclass Subclass instance created. ")
            print("get_name call ", subclass_instance.get_name())
           # print(sedan_instance.__subclasshook__()) # exception because it looks for tuple as subclass even though there is no subclass 


