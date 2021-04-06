from collections import Counter, defaultdict, OrderedDict

# Counter allows count number of things (char, numbers) in iterable

li = [1,2,3,4,5,6,7]
print(Counter(li))

li = [1,2,3,4,5,6,7,8,1,2,3,5,6,7,8]
print(Counter(li))

sentence = "blah blah blah blah thinking about Python"
print(Counter(sentence))


# defaultdict: allows us to give default value to keys that are not present in dictionary
dictionary = {'a':1, 'b':2}
print(dictionary['a'])

# If we try to access something that doesn't exist we get an error
dictionary = defaultdict(lambda: 5, {'a':1, 'b':2})
print(dictionary['c'])
print(dictionary['a'])

# OrderedDict: retains order in which we insert things. default dictionaries
# in python are unordered. Using OrderedDict has performance issues
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3 = OrderedDict()
d3['b'] = 2
d3['a'] = 1

print(d==d2)
print(d==d3)

d = dict()
d['a'] = 1
d['b'] = 2

d2 = dict()
d2['a'] = 1
d2['b'] = 2

d3 = dict()
d3['b'] = 2
d3['a'] = 1
print(d==d2)
print(d==d3)

# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/
