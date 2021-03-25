# List is ordered sequence of objects
li = [1,2,3,4,5]
li2 = ['a', 'b',' c', 'd']
li3 = ['a', 1,2,'apple', 'True']

# Data Structure: Way to organise information
amazon_cart = ['notebooks', 'sunglasses']
amazon_cart[0]
amazon_cart[1]
amazon_cart[3]


# List Slicing
amazon_cart = [
        'notebooks', 
        'sunglasses',
        'toys',
        'grapes']

amazon_cart[0::2]

# Lists are mutable (one element can be changed)
amazon_cart[0] = 'baby powder'
amazon_cart

amazon_cart[0:3]

# To copy a list use [:] otherwise both will refer to same thing
new_list = amazon_cart
new_list[0] = 'apple'
new_list
amazon_cart

new_list = amazon_cart[:]
new_list[0] = 'cat'
new_list
amazon_cart


basket = [1,2,3,4,5]
print(len(basket))
# List methods: https://www.w3schools.com/python/python_ref_list.asp
basket.append(100)
basket
# append changes the list inplace

basket.insert(0, 100)
basket
# insert modifies the list inplace

basket.extend([100, 1001, 101])
basket

# Removing things
basket.pop(0)
basket
basket.pop(-1)
basket
# pop also removes element inplace
# pop removes the element at given index

# remove takes out the given element
basket.remove(4)
basket


basket.clear()
basket
# Clear removes everything in the list


basket = [1,2,3,4,5]
basket.index(2)
# .index returns the index of given element

basket.index(1, 2,5)
basket.index(1, 0,5)

# Key word is a word we use in python which mean something
# https://www.w3schools.com/python/python_ref_keywords.asp
1 in basket
'x' in basket
'i' in 'Gursewak'


basket.count(1)
# 1 only exisits once in list basket

basket = [3,4,5,2,1,2,5,3,9]
basket.sort()
basket
# .sort() edits the same list
# sorted produces a new array 
new_basket = sorted(basket)
basket
new_basket

new_basket1 = basket.copy()
basket.reverse()
basket

basket.sort()
basket.reverse()
basket

basket[::-1]

# generate list quickly
li = list(range(1,100))
li


sentence = ' '
sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
sentence


new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])
new_sentence

# List unpacking
a,b,c = [1,2,3]
a
b
c


a,b,c = 1,2,3


a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
a
b
c
other
d

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
friends.sort()
friends
