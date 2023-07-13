
class IntField: 
    name = ''

    def __get__(self, instance, owner): 
        return instance.__dict__[self.name]
    
    def __set__(self,instance, value): 
        if not isinstance(value, int): 
            raise ValueError(f"Expecting integer in {self.name}")
        instance.__dict__[self.name] = value

    def __set__name(self, instance, name): 
        self.name = name

# class Model: 
intField = IntField()
intField.__set__name
