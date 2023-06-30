State Guessing Game
This is a Python program that allows you to play a state guessing game using the turtle and pandas libraries. The program displays a map of the United States and prompts you to enter the names of different states. You can keep guessing the names of states until you correctly guess all 50 states or choose to exit the game.

Prerequisites
Python 3.x
turtle library
pandas library
Installation
Install Python 3.x from the official Python website: https://www.python.org/downloads/


Usage
Download the source code file state_guessing_game.py and the CSV file 50_states.csv.

Place both files in the same directory.

Open a terminal or command prompt and navigate to the directory where the files are located.

The program will display a window with a map of the United States. The window will prompt you to enter the name of a state.

Enter the name of a state and press Enter.

If your guess is correct, the program will mark the state on the map and display the number of correct guesses out of 50.

Continue guessing state names until you correctly guess all 50 states or choose to exit the game.

To exit the game, type "Exit" (without quotes) as your guess and press Enter.

If you choose to exit the game, the program will display a list of the states you missed.

Click on the game window to close it.



Notes
The program uses a map image file called blank_states_img.gif. Ensure that the file is present in the same directory as the source code file.

The program reads state data from the 50_states.csv file. Make sure to have this file in the same directory as the source code file.

The program relies on the turtle library for graphical display and interaction. The turtle library is included in the Python standard library, so no additional installation is required.

The pandas library is used to read and process the state data from the CSV file. It needs to be installed using the command pip install pandas if not already installed.

The game will continue until you correctly guess all 50 states or choose to exit by typing "Exit" as your guess



Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request.
