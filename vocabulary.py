import random

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