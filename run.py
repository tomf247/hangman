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


print(random_word())

