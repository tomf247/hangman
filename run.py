import random


ASCII_ART = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


class Hangman:
    """
    Initialize and set the game paramaters.
    """
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        """
        Add the letter to the relevant list
        """
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)
		
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        else:    
            return False

    def hide_word(self):
        """
        Determine if a guessed letter or a blank space displays
        """

        char_to_show = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                char_to_show += '_'
            else:
                char_to_show += letter
        return char_to_show

    def show_game_status(self):
        """
        Prompts the player for a letter, validates it,
        and checks the game status.
        """
        print (ASCII_ART[len(self.missed_letters)])
        print ('Word: ' + self.hide_word())
        print ('Letters Missed: ', )
        for letter in self.missed_letters:
            print (letter, )
        print()
        print ('Letters Guessed: ', )
        for letter in self.guessed_letters:
            print (letter, )
        print()


def random_word():
    """
    Selects a random word for the game
    """
    words = [
        'finch',
        'pigeon',
        'pheasant',
        'duck',
        'owl',
        'crow',
        'sparrow',
        'robin'
    ]
    return words[random.randint(0, len(words)-1)]

def main():
    """
    Start the game, and wait for player to
    select a letter
    """

    game = Hangman(random_word())
    while True:
        game.show_game_status()
        user_input = input('\nEnter a letter: ')
        if user_input == '0':
            print('The word was ' + game.word)
            print('bye!')
            return

        if user_input >= 'a' and user_input <= 'z' \
        or user_input >= 'A' and user_input <= 'Z':

            print(user_input, 'is a valid letter.')
            print('you typed:', user_input)
        else:
            print(user_input, 'is not a valid letter')


    game.show_game_status()	
    if game.hangman_won():
        print ('\nWell done! You win.')
    else:
        print ('\You lost this game.')
        print (f'The word was {self.word}')
		
    print ('\nGoodbye!\n')

if __name__ == '__main__':
    main()