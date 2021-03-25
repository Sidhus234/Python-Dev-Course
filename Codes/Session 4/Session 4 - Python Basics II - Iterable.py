# Iterable: Object or collection that can be iterated over
# Iterable: String, list, set, dictionary, tuple
# Iterate: one by one check each item in the collection

# Int, float, char can't be iterable

user = {
        'name': 'Golem',
        'age': 50,
        'can_swim': False
        }

for key, value in user.items():
    print(key, value)


for item in user.values():
    print(item)
    
for item in user.keys():
    print(item)