# Short Circuiting

is_Friend = True
is_User = True

if (is_Friend and is_User):
    print("Best Friends forever")
    
if (is_Friend or is_User):
    print("Best Friends forever")
    
# Python will evaluate the first expression if second expression is after Or
