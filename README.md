# Hangman
[logo](https://github.com/tomf247/hangman/blob/073fa4407dbdf58e06946c171259d1204fe0776f/docs/screenshots/hangman-logo.jpg "Hangman Logo")

Hangman is a Python terminal game, which will run anywhere a Pythpn command line interpreter is available.

The object of the program is to guess the word the computer has selected, within the allowed number of guesses permitted.

[Here is a link to the application](https://tf-hangman.herokuapp.com/)

## How to play

The game is based on the traditional game as described on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

A hanging stick figure is progressively revealed for every incorrect guess. Only solving the correct word will prevent the figure from hanging.

The player is allowed six incorrect guesses, after which the game is over. However if the player solves the secret word, a message is displayed showing the player has won.

At the end of each game the player has an option to play again, or quit the game.

## Features

### Existing Features

![alt text](https://github.com/tomf247/hangman/blob/3a42be5305e053bcb8dc24937ef670ac8f10280c/docs/screenshots/hangman_start.png "Random Word Generator")

- Random Word Generator: The app selects a random word at the start. This word is not revealed until the game is over.
- Accepts user guesses.

![alt text](https://github.com/tomf247/hangman/blob/3a5a75960142dd7dae52b2c1f4c3cb743632aae1/docs/screenshots/hangman_progression.png "Guessed letters display")

- Maintains list of correct guesses.
- Maintains list of incorrect guesses.
- Counts the number of guess attempts.


![alt text](https://github.com/tomf247/hangman/blob/a99faa3b31847d4f9219d513d9cb3cfd9cefde9e/docs/screenshots/hangman_error_checking.png "Error checking")

- Only upper or lowercase letters from "a" to "z" permitted.
- Any other keystroke is rejected.



