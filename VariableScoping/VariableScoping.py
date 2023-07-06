
class ScopeTest:
    spam = "Initial variable assignment"
   
    def variable_scope(self):

        # local scope is restricted to function only
        def do_local():
            spam = "local spam"


        # nonlocal scope remains in enclosed scope
        def do_nonlocal():
            nonlocal spam 
            spam =  "nonlocal spam"
        
        # global scope is at the module level and not under the function level.
        # even though the call has been placed, its reflected value would be accessed
        # at module level.
        def do_global():
            global spam
            spam = "global spam"
            
        spam = "test spam"

        # Variable value won't change after do_local due to variable scope restriction
        do_local()
        print("After local assignment:", spam)

        # Variable value will change as variable is nonlocal in context
        do_nonlocal()
        print("After nonlocal assignment:", spam)

        # Variable value will change but won't show its changes since the display is at function level and 
        # not outside
        do_global()
        print("After global assignment:", spam)
   

scopeTestObj = ScopeTest()
print ("Initial variable assigment: ", scopeTestObj.spam)

scopeTestObj.variable_scope()
# Since spam variable became global, its changed value will be displayed at module level to access
print("In global scope:", spam)


# scopeTestObj.spam = "test spam"
# print ("After changing variable assigment from outside: ", scopeTestObj.spam)

# scopeTestObj.do_local()
# print("After local assignment by using nonlocal:", scopeTestObj.spam)

# scopeTestObj.do_nonlocal()
# print("After nonlocal assignment:", scopeTestObj.spam)

# scopeTestObj.do_global()
# print("After global assignment:", scopeTestObj.spam)

# print("In global scope:", scopeTestObj.spam)


# def scope_test():

#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)

#     do_nonlocal()
#     print("After nonlocal assignment:", spam)

#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)


