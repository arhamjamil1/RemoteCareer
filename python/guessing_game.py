import random
secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Congratulations! You guessed the correct number.")
elif guess < secret:
    print("Too low! Try again.")
else:
        print("Too high! Try again.")