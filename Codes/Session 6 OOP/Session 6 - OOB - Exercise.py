# Have a class SuperList, which works exactly same as list
# other than that len always return 1000

class SuperList(list):
    
    def __len__(self):
        return 1000
    

super_list1 = SuperList()
super_list1.append(5)
print(len(super_list1))

print(super_list1[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))

# Base of Python is object class, list inherits from object class
