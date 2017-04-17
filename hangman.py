# Hangman

# mrsenequ : 10401788 : Matthew Seneque

import random
from wordList import wordList

lettersLeft = ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

word = random.choice(wordList)

hang = ["\n   \n\n         9 guesses left\n\n\n...... ",
        "\n   \n\n         8 guesses left\n\n\n|\.... ",
        "\n|   \n|\n|        7 guesses left\n|\n|\n|\.... ",
        "____\n|   `\n|\n|        6 guesses left\n|\n|\n|\.... ",
        "____\n|   `O\n|\n|        5 guesses left\n|\n|\n|\.... ",
        "____\n|   `O\n|    |\n|    ^   4 guesses left\n|\n|\n|\.... ",
        "____\n|   `O\n|   /|\n|    ^   3 guesses left\n|\n|\n|\.... ",
        "____\n|   `O\n|   /|\ \n|   .^   2 guesses left\n|   ]\n|\n|\.... ",
        "____\n|   `O\n|   /|\ \n|   .^.  1 guess left\n|   ] [\n|\n|\.... ",
        "____\n|   |\n|   O\n|  /|\  YOU ARE DEAD\n|   |\n|  /|  \n|\.... "]


i = 0
lettersUsed = ''
wordsUsed = ''

print('\nWELCOME TO PY HANGMAN')

while True:
    # print correct hangman diagram
    print (hang[i])

    # print the guess history
    print("      ", end="")
    for letter in word:
        if letter in lettersLeft:
            print("_", end="")
        else:
            print(letter, end="")
    print ("  ", len(word), "letter word\n\nLetters used:", lettersUsed, "\n\nWords guessed:", wordsUsed)

    # check if word has been guessed
    if (set(lettersUsed).intersection(word) == set(word)):
        print ("\n\n   YOU WIN !!! \n\n")
        break

    # stop if the guess limit has been reached
    if i == len(hang) - 1:
        print ('\nYou have run out of guesses\n\n\n   YOU LOOSE !!! \n\n')
        print(" The word was", word.upper(), "\n")
        break

    # let the user input their guess
    guess = input('\n\nGuess a letter or guess the word: ')
    guess = guess.lower()

    # proceed if the user enters a single letter from the letters left
    if (len(guess) == 1) and (guess in lettersLeft):

        # the guess is a single letter
        if len(guess) == 1:
            lettersLeft.remove(guess)
            lettersUsed = lettersUsed + ' ' + guess

        # guess matches single letter from the word
        if (guess in word) and (len(guess) == 1):
            continue

    elif guess == word:
        print ("\n\n   YOU WIN !!! \n\n")
        break

    elif len(guess) > 1:
        wordsUsed = wordsUsed + ' ' + guess
        print ('\n You have chosen the wrong word\n')

    else:
        continue

    i = i + 1
