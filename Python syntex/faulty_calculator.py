#reture fault result calculator for some expression
#1+1 = 11,  2+2= 5

while True:
    n1 = float(input("Enter First number:  "))
    n2 = float(input("Enter Second number:  "))
    op = input("Enter operator")

    result = {
        "+": n1+n2,
        "-": n1-n2,
        "*": n1*n2,
        "/": n1/n2
    }

    if (n1 == 1. and n2 == 1. and op == "+"):
        print("Result:  11")
    elif (n1 == 2. and n2 == 2. and op == "+"):
        print("Result:  5")
    else:
        print(f"result: {result[op]}")
