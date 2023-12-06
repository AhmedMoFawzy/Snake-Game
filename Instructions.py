from turtle import *
from time import *
from random import *

# Initial setup
delay = 0.1  # Time delay for the game loop
score = 0  # Player's score
high_score = 0  # Highest score achieved
segments = []  # List to store the snake's body segments

# Screen setup
win = Screen()  # Creating the game window
win.title("Ziad Wael Mohamed ElGammal")  # Setting the window title
win.bgcolor("#8c8c8c")  # Setting the background color
win.setup(650, 650)  # Setting up the window size
win.tracer(0)  # Turning off screen updates for smoother rendering

# Drawing the game border
border = Turtle()  # Creating a turtle for the game border
# ... (Code to draw the border)

# Creating the snake's head
head = Turtle()  # Creating a turtle for the snake's head
# ... (Code to set up the snake's head)

# Creating the snake's food
food = Turtle()  # Creating a turtle for the food
# ... (Code to set up the food)

# Displaying the score
scorepen = Turtle()  # Creating a turtle for displaying the score
# ... (Code to set up the score display)

# Functions for handling directions
# ... (Functions to control snake's movement)

# Listening for keyboard inputs
listen()  # Listening for keyboard input
# ... (Code to bind arrow keys to movement functions)

# Main game loop
while True:
    win.update()  # Update the game window

    # Handling collisions with the game border
    # ... (Code to check if the snake hits the border)

    # Handling collision with the food
    # ... (Code to detect if the snake eats the food)

    # Adding new segments to the snake
    # ... (Code to add new segments when the snake eats food)

    # Checking for collisions with the snake's own body
    # ... (Code to detect if the snake collides with itself)

    # Moving the snake
    move()  # Function to move the snake

    # Controlling game speed
    sleep(delay)  # Introducing a delay to control the game speed

