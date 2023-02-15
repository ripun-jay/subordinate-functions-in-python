var1 = 6
var2 = 63

var3 = int(input("Enter a number:  "))

if var3 > var2:
    print("Greater")
if var3 == var2:
    print("Equal")
else:
    print("Lesser")

#using elif is more conviniant because python execute all if statement
if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

list1 = [1,2,3,4,5]
if var3 in list1:
    print("in list1")
else:
    print("not in list1")

print(5 in list1)  #return boolean
