import random
number = random.randint(1, 100)
print("Guess a number between 1 and 100")
guess = 0
while guess != number:
    guess = int(input("Enter a guess"))
    if guess < number:
        print("That is too low")
    elif guess > number:
        print("That is too high")
    elif guess == number:
        print("That is correct!!")
    else:
        print("Invalid")

