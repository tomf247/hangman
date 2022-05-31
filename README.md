# Hangman

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

- Random Word Generator: The app selects a random word at the start. This word is not revealed until the game is over.
- Accepts user guesses
- Maintains list of correct guesses
- Maintains list of incorrect guesses
- Counts the number of guess attempts


You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!