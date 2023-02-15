"""
Mutable - can change
Immutable - can not change
"""

tp = (1,2,3,4)
print(tp)

#tuple is immuatable

"""
tp[1] = 5  
TypeError: 'tuple' object does not support item assignment
"""

#for tuple of single element , is important

tp1 = (5) 
print(tp1)  #it is not tuple

tp2 = (5,)  #it is tuple
print(tp2)

#swap data
a=1
b=2
a,b=b,a
print(a,b)

#python list function documentation
