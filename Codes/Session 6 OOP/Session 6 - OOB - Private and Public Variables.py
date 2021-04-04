# Public and Private

# Some languages allow private variables
# In python there is no true private variables
# We use _variable name, and it means it should be private variable
# There is no gurantee and _ 
# __init__ is Dunder method, and no user writes their own dunder methods

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def run(self):
        return self
    
    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.speak()

player1.name = '!!!'
player1.speak = 'BOOOO'

print(player1.speak)