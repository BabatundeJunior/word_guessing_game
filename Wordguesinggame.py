"""
I added creativity of randomly selecting the secret word for the user, 
by adding a list for words to randomly select from. By importing random to do the selection
"""
print("Welcome to the Word Guessing Game!")
import random
words = ["coding", "python", "code", "loop", "program"]
secret = random.choice(words)
#welcomes the user to the guessing game
print("Welcome to the Word Guessing Game!")
print(f"{"_ " * len(secret)}")
count = 0

#Using a loop to ask the user to guess the secret word till they get it correctly
while True:
    guess = input("Guess the word: ")
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

    # added hint functanality to give hints to the user
    hint = []
    for letter in range(len(secret)):
        if guess[letter] == secret[letter]:
            hint.append(guess[letter].upper())
        elif guess[letter] in secret:
            hint.append(guess[letter].lower())
        else:
            hint.append("_")
    print(f"A little hint for you {" ".join(hint)}")
    print(
        """
        small letters show the letters are in the secrete word while capital 
        letters show that is the position of the letter in the secret word.
        """
        )



    