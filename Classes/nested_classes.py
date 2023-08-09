class ParentClass: 
    ### Parent class ### 

    int_parent_member: int = 1
    str_parent_member: str = "Parent Class String member"

    def __init__(self) -> None:
        pass

    def parent_display(self) -> str:
        ### Parent display ###
        return self.str_parent_member
    
    # Inner class or child class or even called as nested class since it is inside the parent class. 
    class ChildClass:
        ### Child class ###

        int_child_member: int = 2
        str_child_member: str = "Child Class String member"

        def __init_subclass__(cls) -> None:
            pass

        def child_display(self) -> str: 
            ### Child display ###
            return self.str_child_member
    

if __name__ == '__main__':  
    parent_instance = ParentClass()
    print("Parent class String value: ", parent_instance.parent_display())
    child_instance = parent_instance.ChildClass()
    print("Child class String value: ", child_instance.child_display())
