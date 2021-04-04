class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
action_figure = Toy('red', 0)
print(action_figure.__str__())

# __methods__ is a dunder methods
# More details on dunder methods: https://docs.python.org/3/reference/datamodel.html#special-method-names

# Modify what __str__ does for this class

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
                'name': 'YoYo',
                'has_pets': False
                }
        
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return('yes??')
        
    def __getitem__(self, i):
        return self.my_dict[i]
    
action_figure = Toy('red', 0)
print(action_figure.__str__())

# In above example we have modified the __str__ and __len__ dunder method

print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])