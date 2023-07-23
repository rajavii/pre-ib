n = int(input("Enter number of subjects"))
b = 0
print("Enter the score received in each subject below")
for i in range(0, n):
    a = int(input("Enter grade out of 100"))
    b = b + a
avg = b / n
print(avg)
if (avg >= 90) and (avg < 100):
    print("You got A+")
elif (avg >= 80) and (avg < 90):
    print("You got A")
elif (avg >= 70) and (avg < 80):
    print("You got B+")
elif (avg >= 60) and (avg < 70):
    print("You got B")
elif (avg >= 50) and (avg < 60):
    print("You got C+")
elif (avg >= 40) and (avg < 50):
    print("You got C")
elif avg < 40:
    print("You failed")
else:
    print("Invalid Grade")
