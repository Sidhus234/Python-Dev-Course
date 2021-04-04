some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']
some_list_nodup = list(set(some_list))
print(some_list_nodup)

noduplist = []
duplist = []

for x in some_list:
    if(x in noduplist):
        duplist.append(x)
    else:
        noduplist.append(x)

print(noduplist)
print(duplist)