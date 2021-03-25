# Stakc overlfow link: https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

is_old = "Hello"

if is_old:
    print("String present")
    
is_old = ""
if is_old:
    print("True")
else:
    print("False")
    
    
#All values are considered "truthy" except for the following, which are "falsy":
#
#None
#False
#0
#0.0
#0j
#Decimal(0)
#Fraction(0, 1)
#[] - an empty list
#{} - an empty dict
#() - an empty tuple
#'' - an empty str
#b'' - an empty bytes
#set() - an empty set
#an empty range, like range(0)
#objects for which
#obj.__bool__() returns False
#obj.__len__() returns 0
    
password = '123'
username = 'johnny'

if password and username:
    print("All filled")
else:
    print("Need to complete forms")