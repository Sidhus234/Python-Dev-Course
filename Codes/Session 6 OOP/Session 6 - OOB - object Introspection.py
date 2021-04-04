# dir(instancename) gives all things it has access to
# . uses dir(instancename) uses this to show what all we have access to

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


print(dir(wizard1))
