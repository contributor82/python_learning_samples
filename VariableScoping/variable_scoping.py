"""Module for Variable scope testing """

class ScopeTest:
    """Scope test """
    spam: str = "Initial variable assignment"

    def variable_scope(self) -> None:
        """Variable scoping """

        def do_local() -> None:
            """local scope is restricted to function only"""
            spam = "local spam" #type: ignore

        def do_nonlocal() -> None:
            """nonlocal scope remains in enclosed scope"""
            nonlocal spam
            spam =  "nonlocal spam"

        def do_global() -> None:
            """global variable scoping """
            # global scope is at the module level and not under the function level.
            # even though the call has been placed, its reflected value would be accessed
            # at module level.
            global spam #type: ignore
            spam = "global spam"

        spam = "test spam" #type: ignore

        # Variable value won't change after do_local due to variable scope restriction
        do_local()
        print("After local assignment:", spam)

        # Variable value will change as variable is nonlocal in context
        do_nonlocal()
        print("After nonlocal assignment:", spam)

        # Variable value will change but won't show its
        # changes since the display is at function level and
        # not outside
        do_global()
        print("After global assignment:", spam)

if __name__ == '__main__':
    var_scope_instance = ScopeTest()
    print ("Initial variable assigment: ", var_scope_instance.spam)

    var_scope_instance.variable_scope()
    # Since spam variable became global, its changed
    # value will be displayed at module level to access
    print("In global scope:", spam) #type: ignore
