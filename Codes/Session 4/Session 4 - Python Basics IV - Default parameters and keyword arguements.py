# Positional arguements are required to be in same order as defined in function

# Keyword arguements
def say_hello(name, emoji):
    print(f"Helloo {name} {emoji}")
    return

say_hello(emoji=":P", name="Garry")
# above is bad practice as order is reversed

say_hello(name="Garry", emoji=":p")


# Default parameters

def say_hello(name="John", emoji=":D"):
    print(f"hello {name} {emoji}")
    return
    
say_hello("John", ":P")
say_hello("John")

say_hello()
