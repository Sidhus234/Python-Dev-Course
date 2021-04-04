
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
        
    @classmethod
    def adding_things(cls, num1, num2):
        return num1+num2
    
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 10)

print(player1.adding_things(2,3))

# adding_things is class method because we can use it without initiating a class
print(PlayerCharacter.adding_things(4,5))

# Its rarely used but can be used


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
        
    def age(self):
        print(f'my age is {self.age}')
        
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1+num2)

player3 = PlayerCharacter.adding_things(15,5)
print(player3.age)


# STATIC Method
# static method doesn't have access to the class

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
        
    def age(self):
        print(f'my age is {self.age}')
        
    @staticmethod
    def adding_things( num1, num2):
        return (num1+num2)

print(PlayerCharacter.adding_things(15,5))