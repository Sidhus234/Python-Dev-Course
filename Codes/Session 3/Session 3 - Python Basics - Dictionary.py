# Dictionary: Hash Tables
dictionary = {
        'a': 1,
        'b': 2
        }
# dict has key value pair

dictionary['a']
dictionary['c']

# dict is unordered key value pair. They are not next to each other in memory

print(dictionary)

# Dictionary: Hash Tables
dictionary = {
        'a': [1,2,3,4],
        'b': "apple"
        }

dictionary['a'][0]
dictionary['b'][4]

dictionary = {
        1:1,
        2:2}

dictionary[1]


dictionary = {
        True: "Apple",
        False: "Banana"
        }

# dict key should be immutable. Key shouldnot change. Hence we can't use list as key

dictionary = {
        [100]: "APPLE",
        1: "carrot"
        }

# Key has to be unique in dict. It will be overwritten if given second time

user = {
        'basket': [1,2,3],
        'greet': 'hello',
        'age': 20
        }

user['age']
print(user.get('get', 55))

user2 = dict(name='JohnJohn')

# Dict methods: https://www.w3schools.com/python/python_ref_dictionary.asp

'basket' in user
'size' in user.keys()

20 in user.values()

user.items()

user.clear()

print(user)
# .clear() clears the dict

user = {
        'basket': [1,2,3],
        'greet': 'hello',
        'age': 20
        }

user2 = user.copy()
user.pop('age')
user

user.popitem()
# last item is popped


user.update({'age': 55})

user
