# Encapsulation: is binding of data and functions to manipulate that data
# This is kept in one big code (class) called attributes and methods
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        return self
    
    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.speak()
print(player1.age)
print(player1.name)

# If we don't have any methods, (and only attributes) it's same as dict
player2 = {'name': 'andrei', 'age': 100}
print(player2['name'])
print(player2['age'])
