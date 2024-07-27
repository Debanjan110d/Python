#Guess the Number


import random

number = random.randint(1, 9)

chances = 0

guesses = 1

print("Guess a number (between 1 and 9):")

while chances < 5:

    guess = int(input())

    if guess == number:

        print("Congratulation YOU WON!!!")

        print("You guessed in", guesses, "guesses")

        break

    elif guess < number:

        print("Your guess was too low: Guess a number higher than", guess)

        guesses += 1

    else:

        print("Your guess was too high: Guess a number lower than", guess)

        guesses += 1

    chances += 1
    
if not chances < 4:

    print("YOU LOSE!!! The number is", number)

# Output:

# Guess a number (between 1 and 9):

# 5

# Your guess was too low: Guess a number higher than 5

