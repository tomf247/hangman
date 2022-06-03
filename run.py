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
   /|\\  |
        |
       ===''', '''
    +---+
    O   |
   /|\\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\\  |
   / \\  |
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
        Add the letter to the guessed or missed list
        """
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        """
        Checks to see if game is over
        """
        return self.hangman_won() or (len(self.missed_letters) == 6)

    def hangman_won(self):
        """
        If all letters have been guessed, the game is won.
        """
        if '-' not in self.hide_word():
            return True
        else:
            return False

    def hide_word(self):
        """
        Determine if a guessed letter or an underscore/hyphen displays
        """
        char_to_show = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                char_to_show += '-'
            else:
                char_to_show += letter
        return char_to_show

    def show_game_status(self):
        """
        Update ASCII art to reflect game state, and show score board counts
        """
        print(ASCII_ART[len(self.missed_letters)])
        print('\nWord: ' + self.hide_word() + '\n')
        remaining_guesses = (6 - len(self.missed_letters))
        print(str(remaining_guesses) + ' guesses left. \n')
        print('Letters Missed: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letters Guessed: ', )
        for letter in self.guessed_letters:
            print(letter, )


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

    print('=== > H A N G M A N! <===')
    game = Hangman(random_word())
    while not game.hangman_over():
        game.show_game_status()
        user_input = input('\nEnter a letter, or "0" to quit: \n')
        if user_input == "0":
            print(f'The word was {game.word}')
            print("bye!")
            return

        elif(user_input >= 'a' and user_input <= 'z' and
                len(user_input) == 1) or \
                (user_input >= 'A' and user_input <= 'Z' and
                    len(user_input) == 1):
            game.guess(user_input)
        else:
            print(f'{user_input} is not a valid letter')

    game.show_game_status()
    if game.hangman_won():
        print('\nWell done! You won the game!')
    else:
        print('\nYou lost this game')
        print(f'The word was {game.word}')
        print('\nGoodbye!\n')


if __name__ == '__main__':
    main()
