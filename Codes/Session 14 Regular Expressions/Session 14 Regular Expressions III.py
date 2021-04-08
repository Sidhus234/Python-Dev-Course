# Example: start-up wants to collect email of customers
import re
pattern = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

email1 = "sidhus234@gmail.com"
email2 = "tmp@yahoo.com"
email3 = "eh3gvbdkjhveoq@vdfjk.in"
email4 = "tryout123@fdsv.comer"


a = re.search(pattern, email1)
print(a)

b = re.search(pattern, email2)
print(b)

c = re.search(pattern, email3)
print(c)

d = re.search(pattern, email4)
print(d)
# d is not a valid email