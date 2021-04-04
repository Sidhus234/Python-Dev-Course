
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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print('Ran really fast')
        
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
hb1.sign_in()
