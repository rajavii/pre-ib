a = int(input("Enter first number"))
b = input("Enter operator")
c = int(input("Enter second number"))
if b == "+":
    d = a + c
    print(d)
elif b == "-":
    d = a - c
    print(d)
elif b == "*":
    d= a * c
    print(d)
elif b == "/":
    d = a / c
    print(d)
else:
    print("Invalid Input")
