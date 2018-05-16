from vocabulary import Vocabulary
from hang import Hangman

def main():
    vocabulary = Vocabulary()
    hangman = Hangman(vocabulary)
    hangman.startGame()

if __name__ == '__main__':
    main()