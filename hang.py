import string
from vocabulary import Vocabulary

class Hangman:
    MAX_GUESSES = 8

    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.secretWord = ''
        self.remainingGuesses = self.MAX_GUESSES
        self.availableLetters = string.ascii_lowercase
        self.lettersGuessed = []

    def getValidWord(self):
        try:
            word = self.vocabulary.getRandomWord()
            while not self.isValidWord():
                self.secretWord = self.vocabulary.getRandomWord()
            return word
        except IndexError:
            print("Can't choose a word, emtpy file!!!")
            quit()

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

    def getLetter(self):
        letter = input('Please guess a letter: ')
        
        while letter not in string.ascii_letters:
            letter = input('Invalid input. Characters from a-z only, please: ')

        return letter.lower()

    def mainLoop(self):
        while not self.isWordGuessed() and self.remainingGuesses > 0:
            print('You have ', self.remainingGuesses, 'guesses left.')

            available = self.getAvailableLetters()
            print('Available letters', available)

            letter = self.getLetter()

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
