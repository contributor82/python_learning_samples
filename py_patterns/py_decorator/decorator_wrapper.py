"""Module for decorator wrapper class"""

from sub_decorator_one import SubDecoratorOne
from sub_decorator_two import SubDecoratorTwo
from sub_system_class_one import SubSystemClassOne

# Wrapper class for decorator
class DecoratorWrapper:
    """Decorator wrapper class """
    sub_sys_cls_one: SubSystemClassOne
    sub_decorator_one: SubDecoratorOne
    sub_decorator_two: SubDecoratorTwo

    def update_system(self)-> None:
        """Update system """
        self.sub_sys_cls_one = SubSystemClassOne()

        # decorate step 1
        self.sub_decorator_one = SubDecoratorOne(self.sub_sys_cls_one)
        self.sub_decorator_one.method_one()
        self.sub_decorator_one.method_two()

        # decorate step 2
        self.sub_decorator_two = SubDecoratorTwo(self.sub_sys_cls_one)
        self.sub_decorator_two.method_one()
        self.sub_decorator_two.method_two()
