import random

listOfWords = ['APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE',
               'ENSURING', 'FORMALISING', 'GLITCHES', 'HARMINE', 'INDENTATION', 'JACKED',
               'KALPACS', 'LAUNDRY', 'MASKED', 'NETTED', 'OXFORD', 'PARODY', 'QUOTIENTS',
               'RACERS', 'SADNESS', 'THYREOID', 'UNDUE', 'VENT', 'WEDGED', 'XERIC', 'YOUTHHOOD',
               'ZIFFS']

if __name__ == "__main__":
    word = random.choice(listOfWords)

    turns = 6
    guesses = ''
    print(word)

    print("Guess the characters.")

    while turns > 0:
        fails = 0
        for letter in word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                fails += 1
        print("")
        if fails == 0:
            print("Congratulations! You win")
            print("The word is: ", word)
            break

        guessWord = input("Choose a character.")
        guessWord = guessWord.upper()
        guesses += guessWord

        if guessWord not in word:
            turns -= 1

            print("Wrong")
            print("You have", turns, "more guesses")

            if turns == 0:
                print("You loose")
                playGame = input("Do you want to play again?(Y/N)")
                if (playGame[0].lower() == 'y'):
                    turns = 6
                    guesses = ''
                    word = random.choice(listOfWords)
                    print('Guess the characters')
