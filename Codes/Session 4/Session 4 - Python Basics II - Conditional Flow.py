# Conditional Logic based on True False
is_old = True
is_licenced = False

if is_old and is_licenced:
    print("Can Drive")
elif is_old:
    print("You are old but can't drive")        
else:
    print("Can't drive")

