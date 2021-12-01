import random

# rand = 42
rand = random.randint(1, 99)
print("This is an interactive guessing game!\nYou have to",
      "enter a number between 1 and 99 to find out the secret number.",
      "\nType 'exit' to end the game.\nGood luck!\n")
attempts = 1
while (1):
    print("What's your guess between 1 and 99?\n>> ", end='')
    guess = input()
    try:
        guess = int(guess)
        if (guess == rand):
            if (rand == 42):
                print("The answer to the ultimate question of life,",
                      "the universe and everything is 42.")
            if (attempts == 1):
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!",
                      f"""\nYou won in {attempts} attempts!""")
            break
        elif (guess < rand):
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        if (guess == "exit"):
            print("Goodbye!")
            break
        else:
            print("That's not a number.")
    attempts += 1
