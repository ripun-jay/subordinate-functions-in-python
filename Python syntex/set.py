#set is the collection of well defined objects

s1 = set()
print(type(s1)) 

#building set from list
numbers = [1,2,3,4,5]
s = set(numbers)
print(s, type(s))

#adding element in set
s1.add(1)
s1.add(1)
s1.add(2)
print(s1)

#remove from set
s1.remove(1)
print(s1)

#set has only unique elements

set1 = set([1,2,3,4])
set2 = set([3,4,5,6])

print(set1.union({4,5,2,9}))

print(set1.union(set2))
print(set1.intersection(set2))

print(min(set1))
print(max(set1))
print(len(set1))

#.isdisjoint
print(set1.isdisjoint(set2))
print(s1.isdisjoint(set2))


