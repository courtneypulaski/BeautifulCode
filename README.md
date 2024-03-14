# PATTERN GUESSING GAME
### Video Demo:  https://youtu.be/G9_GTQYDD7U
### Summary Description:
This project is a game that mimicks the 1970 game Mastermind. In this version, the user is able to choose the number of spaces to guess (anywhere from 3 to 8), and the number of colors to use to guess with (anywhere from two to six). Then the game randomly chooses a pattern of the given length, and prompts the user for a guess. The user is given feedback in the form of a result. In Hard Mode, the user only gets a count of how many colors in their guess were in the right location, or in the pattern but in a different location; In Easy Mode, it resembles Wordle where the user is told which colors are in the right place, in the wrong place, or not in the pattern at all. The user gets a certain number of guesses, and then the pattern is revealed to the user if they did not guess it.
### Detailed Description
#### Program Start
When the program starts, a series of prompts is shown to the user. At any point during this initialization, the user is able to end the program by typing "quit" or pressing CTRL + D. The user is also able to press "help" to get more information.
+ First the user is prompted for a number of spaces, between 3 and 8. If the user gives a response other than a number between 3 and 8, they are prompted again. Typing "help" gives a prompt explaining to enter a number from 3-8.
+ Once a valid number of spaces is entered, the user is prompted for a number of colors, between 2 and 6. The six available colors are red, orange, yellow, green, blue, and purple, and the number of colors selected will determine how many of them are used. Typing "help" will give information about what colors are available to choose from.
+ Once a valid number of colors is entered, the user is prompted for whether they want to play in hard mode or not. Typing "help" will explain the difference.
    - If the user chooses yes (Y/y), then the result from a guess will be given generally, with just a count of how many colors are in the correct positions, and how many colors are in the pattern but in a different position.
    - If the user chooses no (N/n), then the result from a guess will be given more specifically, with each position being given a response so the user knows which colors are in the right position, the wrong position, or not in the pattern.

When the user chooses Yes or No for hard mode, then the game begins.
#### Starting the Game
The game starts by selecting a subset of the six available colors - red, orange, yellow, green, blue, purple. It randomly chooses a number of these colors based on the user's selection, and then randomly generates a pattern of the length the user provided. The number of guesses is based on the options selected. It starts with a base of 3 guesses. Hard Mode adds 2 additional guesses, a length of 5 or more adds 1 more, a length of 7 or more adds 1 more than that, and selecting 5 or more colors adds 1 more. The maximum number of guesses is a game with 7 or 8 spaces, 5 or 6 colors, in hard mode with 8 guesses.
#### Getting a Guess
The user is prompted for a guess, told how many guesses they have total, how many spaces there are, and what the available colors are. The user is able to type quit at any point during getting a guess, and the game ends and the pattern is revealed.
* The guess must be a list of color names, separated by commas.
* The color names must be among the names in the given list.
* If these two things are not true, then the user is prompted again without using up a guess.

Once a valid guess is received, then it is checked against the pattern.
#### Checking the Guess
The given guess is checked against the pattern.
* First the guess is checked to see how many colors are correct in the right spot.
* Then, the guess is checked to see how many colors are in the pattern but in the wrong place. This is to avoid a wrong place obfuscating a right place. If there are too many of a color in the guess, then any extra are marked as incorrect.

The result is a string of numbers: 1 means correct place, 2 means incorrect place, 3 means not in the pattern.
The result is then translated to a more user friendly format depending on the mode.
* In hard mode, the user is only told how many are correct and how many are in the wrong place.
* In easy mode, the user is told exactly which ones are correct, in the wrong place, or incorrect.

This user friendly result is given to the user, and if they still have guesses remaining, they are given another chance to guess and the process repeats.
#### Ending the Game
There are a few ways that the game ends
* During any guess, the user can type quit to end the game early. The pattern will be revealed.
* If the user guesses correctly, then the user is given a "You Win!" message, the pattern is revealed, and the game ends.
* If the user does not guess correctly and uses up all their guesses, then the game will end and the pattern will be revealed.

The user can rerun the program to play again.
