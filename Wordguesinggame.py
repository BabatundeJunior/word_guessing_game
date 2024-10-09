"""
I added the creativity of randomly selecting the secret word for the user, 
by adding a list of words to choose from randomly. By importing random to do the selection
"""
import random
words = ["coding", "python", "code", "loop", "program"]
secret = random.choice(words)
#welcomes the user to the guessing game
print("Welcome to the Word Guessing Game!")
print(f"{"_ " * len(secret)}")
count = 0

#Using a loop to ask the user to guess the secret word till they get it correctly
while True:
    guess = input("Guess the word according to the number of spaces provided: ")
    count += 1
    if guess == secret:
        print("Great Job! You guessed it!")
        print(f"It took you {count} guesses.")
        break
    if len(guess) < len(secret):
        print("Too short! it must have the same number of letters as the secret word!")
        continue
    if len(guess) > len(secret):
        print("Too long! it must have the same number of letters as the secret word!")
        continue

    # Added hint functionality to give hints to the user
    hint = []
    for letter in range(len(secret)):
        if guess[letter] == secret[letter]:
            hint.append(guess[letter].upper())
        elif guess[letter] in secret:
            hint.append(guess[letter].lower())
        else:
            hint.append("_")
    print(f"A little hint for you  { " ".join(hint)}")
    print(
        """
        UPPERCASE letters mean the letter is correct and in the right position.
        lowercase letters mean the letter is in the word but in the wrong position.
        """
        )
