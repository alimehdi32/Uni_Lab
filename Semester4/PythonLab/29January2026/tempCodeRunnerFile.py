print("Ali Mehdi - 24BCS008")

import random

num = random.randint(1, 100)

for i in range(5):
    guess = int(input("Enter your guess: "))
    
    if guess == num:
        print("Correct! You guessed it.")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
else:
    print("Game Over! Number was:", num)