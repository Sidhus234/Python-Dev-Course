# Abstraction: means hiding of information or abstracting information and
# giving access to only things that are necessary, and hide rest under blanket
# (As user doesn't need them)

# built in functions - we don't know they are implemented but we can use them

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


# Abstracts thing that we don't care much about how it is implemented but we can use it

player1.name ='!!!'
player1.speak = 'boo'
print(player1.speak())

# speak method has been overwritten