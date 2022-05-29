import random


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


game_word = random_word()

while True:

    user_input = input('\nEnter a letter: ')
    if user_input == '0':
        print('The word was ' + game_word)
        print('bye!')
        exit()

    if user_input >= 'a' and user_input <= 'z' \
       or user_input >= 'A' and user_input <= 'Z':

        print(user_input, 'is a valid letter.')
        print('you typed:', user_input)
    else:
        print(user_input, 'is not a valid letter')
