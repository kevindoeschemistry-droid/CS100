# Bro Code #8: string slicing
# Week 1
# https://www.youtube.com/watch?v=XKHEtdqhLK8&t=2458s

#slicing = create a substring by extracting elements from anotheer string
#indexing[] or slice()
# [start:stop:step]

name = "Bro Code"

first_name = name[0:3]
last_name = name[4:8]
funky_name = name[::2]
reversed_name = name[::-1]

website1 = "http://google.com"
website2 = "http://yahoo.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)