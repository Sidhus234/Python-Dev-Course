# Inheritance: allows new objects to take on properties of existing objects

# Users
# - Wizards
# - Archers
# - Ogres
 
class User:
    def sign_in(self):
        print('logged in')

# If we don't have any variables , we skip __init__ method
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


# Pass the class name while creating class for inheritance
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()
archer1.sign_in()
wizard1.sign_in()

# Parent class and children class
# Children classes are also called sub classes or derived class
wizard1 = Wizard('Merlin', 50)
isinstance(wizard1, Wizard)
isinstance(wizard1, User)
# Func isinstance tells whether any variable is part of class

# Python comes with base class object
# Everyvariable out there is inherited from base class "object"
isinstance(wizard1, object)
