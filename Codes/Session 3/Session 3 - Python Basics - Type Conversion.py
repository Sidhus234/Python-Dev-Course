a = str(100)
type(a)

a = int(a)
type(a)
a

# Type Conversion: convert one type to another

name = 'Gursewak Singh'
age = 29
relationship_status = 'single'
relationship_status = 'it\'s complicated'
print(relationship_status)

from datetime import date
birth_year = input('Which year were you born?')
age = date.today().year - int(birth_year)
age
