# There are two ways to initiate variables of Parent class from derived class
# 1. call <<ParentClassName>>.__init(self, <<varname>>)
# 2. super().__init__(<<varname>>)
# super() is a new method 

class User:
    
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')
    

# If we don't have any variables , we skip __init__ method
        
class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


def player_attack(char):
    char.attack()

# Pass the class name while creating class for inheritance
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

print(wizard1.email)
print(archer1.email)
