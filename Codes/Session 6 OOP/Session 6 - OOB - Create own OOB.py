# oop
# Name should be singular (not plural)

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print('run')
    
    
player1 = PlayerCharacter("John", 10)
print(player1)

# __init__ method also called constructor/init method.
# __init__ runs whenever we create an object of class
player1.run()

# self is way of Python to understand to that anything "self" belongs to class
print(player1.name)

player2 = PlayerCharacter("Cindy", 24)
print(player2.name)

# To get memory of objects
print(player1)
print(player2)
