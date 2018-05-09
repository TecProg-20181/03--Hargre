import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def getRandomWord(wordlist):
    word = random.choice(wordlist).lower()
    return word

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed

def getAvailableLetters(lettersGuessed):
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    return available

def getAmountOfUniqueLetters(secretWord):
    differentLetters = set(secretWord)
    return len(differentLetters)

def isValidWord(secretWord, guesses):
    hasMoreGuessesThanUniqueLetters = guesses > getAmountOfUniqueLetters(secretWord)
    return hasMoreGuessesThanUniqueLetters

def hangman(wordlist):
    secretWord = getRandomWord(wordlist)
    guesses = 8
    lettersGuessed = []

    while not isValidWord(secretWord, guesses):
        secretWord = getRandomWord(wordlist)

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('The word has', getAmountOfUniqueLetters(secretWord), 'different letters.')
    print('-------------')

    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print('You have ', guesses, 'guesses left.')

        available = getAvailableLetters(lettersGuessed)
        print('Available letters', available)

        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            print('Oops! You have already guessed that letter: ')
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print('Good Guess: ')
        else:
            guesses -= 1
            lettersGuessed.append(letter)
            print('Oops! That letter is not in my word: ')

        guessed = getGuessedWord(secretWord, lettersGuessed)
        print(guessed)
        print('------------')

    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ', secretWord, '.')

def main():
    wordlist = loadWords()
    hangman(wordlist)

main()
