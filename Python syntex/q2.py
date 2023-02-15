datatype = {
    "intigers": "numbers without desimal points",
    "float": "numbers with desimal point",
    "string": "non-numeric",
    "boolean": "True or False",
    "NoneTpye" : "value not exist",
}

ui = input("Enter datatype to know about:   ")
print(f"{ui} include '{datatype[ui]}'")