class PlayerCharacter:
    # Class Object Attributes
    membership = True
    def __init__(self, name, age):
        if(self.membership):
            self.name = name
            self.age = age
        
    
    def run(self):
        print('run')
        
    def shout(self):
        print(f'my name is {self.name}')
    
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

player2.attach = 50

help(player1)

# Class Object Attribute is static. It will be true and exist for all objects of class
# membership is a class object attribute
print(player1.membership)
print(player2.membership)

# class attributes are dynamic (like name and age in this example)

print(player1.name)

player1.shout()
player2.shout()