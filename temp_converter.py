x = int(input("Enter temperature to be converted"))
y = input("Enter current unit")
if y. upper() == "C":
    temp = (x * 9 / 5) + 32
    print(temp, "Degree F")
elif y.upper() == "F":
    temp = (x - 32) * 5 / 9
    print(temp, "Degree C")
else:
    print("Invalid")
