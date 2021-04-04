# Polymorphism: Many forms
# Object classes can share same method names, and the methods can behave 
# differently depending on who calls them

# Here attack() method works differently depending on who calls it

class User:
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')

# If we don't have any variables , we skip __init__ method
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


def player_attack(char):
    char.attack()

# Pass the class name while creating class for inheritance
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

player_attack(wizard1)
player_attack(archer1)
# Though there is attack() method in User class, it is overwritten by atack
# method in sub or derived classes

# Polymorphism allows us to change methods (inherited from parent clas)

