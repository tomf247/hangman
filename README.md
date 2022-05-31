# Hangman

[logo](https://github.com/tomf247/hangman/blob/041172e7feacbf84e9efb6589abcca3f4a06eed0/docs/screenshots/hangman_logo.jpg "Hangman Logo")

Hangman is a Python terminal game, which will run anywhere a Python command line interpreter is available.

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

- Game state is maintained in a class structure.

### Future Features

- Load word list from a data file.
- Two player game.
- Further user interaction and feedback.

## Data Model

Two classes are used in the application. The Hangman class initializes the board and maintains game state, while the Main class solicits player interaction.

Methods are used to update lists and counts.

## Testing

Testing included the following steps:

- Passed the code though a Python linter and confirmed there were no issues.
- Checked that only valid letters and not other characters are accepted.
- Tested on both a local terminal promt and the Heroku terminal.

## Bugs

### Solved Bugs

- The underscore character does not display in the Heroku CLI. This was a challenge
as I relied on the number of underscores to show the length of the word being guessed. I fixed this by substituting the underscore with a hyphen character.

- I had an "index-out-of-range" error when displaying the ASCII art. This was solved by subtracting 1 from the length of the array.

### Remaining Bugs

- No remaining bugs.

## Validator Testing

### PEP8

- The code passes all tests at www.pep8online.com.

## Deployment

This app was deployed to Heroku using Code Institute's terminal emulator.

### Steps for deployment

- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks as `Python` and `NodeJS` in that order.
- Link the Heroku app to the repository
- Click on Deploy

## Credits

I referred to www.stackexchange.com frequently, both for syntax as well as design principles.
The ASCII array used in the app was found on www.stackexchange.com and is in the public domain.
I created my own version of the app, but studied code samples which influenced portions of the app.

The client terminal is supplied by Code Institute.





