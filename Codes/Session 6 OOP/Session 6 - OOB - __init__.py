
class PlayerCharacter:
    # Class Object Attributes
    membership = True
    def __init__(self, name='anonymous', age=0):
        if(age > 18):
            self.name = name
            self.age = age
        
    
    def run(self):
        print('run')
        
    def shout(self):
        print(f'my name is {self.name}')
    
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 10)

player2.shout()