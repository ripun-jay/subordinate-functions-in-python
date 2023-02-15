"""
Data Types:-
int
str
floot
boolene
"""

"""
data structure:-
List
"""

pets = ["dog", "cow", "lion", "elephant"]
agelimit = [15, 20, 14, 18, 36, 8]
random_list= ["name", 26, True, 27.5]

#sort the list
print(agelimit.sort())

#access element from list
print(pets[2])

"""
list slicing - some additional functions are available for list DS but not for list like .sort()"""

print(random_list[2])

for element in random_list:
    print(f"data type of '{element}' is '{type(element)}")

lenth = len(pets)    
print(pets[0:lenth])  #return whole list

#extended slicing
print(pets[0:3:2])
print(pets[::-1]) 
#do not use more -ve then -1 for 3rd argument

#add element in list

#following will return None >> trying to print action
#None is a data type of its own (NoneType)
"""
print(pets.append("goat"))
print(pets.append("cow"))

print(pets.insert(0, "ant"))
print(pets.insert(2, "snake"))

#remove element from list
print(pets.pop())
print(pets.remove("ant"))

"""
print(type(None))

names = ["ripun", "sophi", "muggle", "bell", "sam"]

names.append("jules")
print(names)

names.insert(2, "lauren")
print(names)

names.pop()
print(names)

names.remove("bell")
print(names)

names.pop(2)
print(names)