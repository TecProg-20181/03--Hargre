import random
import string


class Vocabulary:
    WORDLIST_FILENAME = "words.txt"

    def __init__(self):
        self.wordlist = []
        self.loadWords()

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(self.WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        self.wordlist = str.split(line)
        print("  ", len(self.wordlist), "words loaded.")

    def getRandomWord(self):
        word = random.choice(self.wordlist).lower()
        return word

class Hangman:
    MAX_GUESSES = 8

    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.secretWord = ''
        self.remainingGuesses = self.MAX_GUESSES
        self.availableLetters = string.ascii_lowercase
        self.lettersGuessed = []

    def getValidWord(self):
        word = self.vocabulary.getRandomWord()
        while not self.isValidWord():
            self.secretWord = self.vocabulary.getRandomWord()
        return word

    def isValidWord(self):
        hasMoreGuessesThanUniqueLetters = self.MAX_GUESSES > self.getAmountOfUniqueLetters()
        isEmpty = not self.secretWord
        return hasMoreGuessesThanUniqueLetters and not isEmpty

    def getAmountOfUniqueLetters(self):
        differentLetters = set(self.secretWord)
        return len(differentLetters)

    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getAvailableLetters(self):
        for letter in self.availableLetters:
            if letter in self.lettersGuessed:
                self.availableLetters = self.availableLetters.replace(letter, '')

        return self.availableLetters

    def getGuessedWord(self):
        guessed = ''

        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed

    def printStart(self):
        print('Welcome to the game, Hangam!')
        print('I am thinking of a word that is', len(self.secretWord), ' letters long.')
        print('The word has', self.getAmountOfUniqueLetters(), 'different letters.')
        print('-------------')

    def handleEndGame(self):
        if self.isWordGuessed():
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', self.secretWord, '.')

    def mainLoop(self):
        while not self.isWordGuessed() and self.remainingGuesses > 0:
            print('You have ', self.remainingGuesses, 'guesses left.')

            available = self.getAvailableLetters()
            print('Available letters', available)

            letter = input('Please guess a letter: ')
            if letter in self.lettersGuessed:
                print('Oops! You have already guessed that letter: ')
            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)
                print('Good Guess: ')
            else:
                self.remainingGuesses -= 1
                self.lettersGuessed.append(letter)
                print('Oops! That letter is not in my word: ')

            guessed = self.getGuessedWord()
            print(guessed)
            print('------------')

    def startGame(self):
        self.getValidWord()
        self.printStart()
        self.mainLoop()
        self.handleEndGame()

def main():
    vocabulary = Vocabulary()
    hangman = Hangman(vocabulary)
    hangman.startGame()

main()
