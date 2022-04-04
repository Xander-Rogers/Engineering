#!PythonProjects/env python
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: collision_detection.py
"""
Example of how a Python programs can use mathematical arguments, and functions from libraries such as pygame, to detect
collision on a very basic 2D level.
"""
# import required libraries
import pygame
import random
import sys

# Initialize all of the pygame objects into the program
pygame.init()

# Define the colors used for the program
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Set the dimensions of the screen
width = 450
height = 450

# Set the size of pixel height of the blocks
pixel = 64

# Set screen height
screen = pygame.display.set_mode((width, height))

# Set caption of the screen
pygame.display.set_caption("COLLISION DETECTION")

# Load the image of the game icon
gameIcon = pygame.image.load("duck.png")

# Set icon
pygame.display.set_icon(gameIcon)

# Load the player image
playerImage = pygame.image.load("player.png")

# Set the position of the player
playerXPosition = (width / 2) - (pixel / 2)

# Set so that the player will be at height above the bottom of the screen
playerYPosition = height - pixel - 10

# Set player position initially to 0
playerXPositionChange = 0


# Define a function for setting the image at particular coordinates on the screen
def player(x, y):
    # Set player image to the screen as an object
    screen.blit(playerImage, (x, y))


# Load the block image
block_img = pygame.image.load("block.png")

# Set random position of the block on the screen
blockXPosition = random.randint(0, (width - pixel))

blockYPosition = 0 - pixel

# Set the 'falling speed' of the block on the screen
blockXPositionChange = 0
blockYPositionChange = 2


# Create a function for setting the block image at coordinates on the screen
def block(x, y):
    # Set block image to the screen as an object
    screen.blit(block_img, (x, y))


# Define a function for collision detection
def collision():
    # Make the block position a global variable: Normally not a 'pythonic' idea since the use of classes can eliminate
    # the need for globals.
    global blockYPosition

    # Check conditions of the block and player images
    if playerYPosition < (blockYPosition + pixel):

        if ((blockXPosition < playerXPosition < (blockXPosition + pixel))
                or (blockXPosition < (playerXPosition + pixel) < (blockXPosition + pixel))):
            blockYPosition = height + 1000


# Set to True to initialize game functions onto the screen
running = True

while running:

    # Set the screen to fill as the color white (this can be changed to any color desired)
    screen.fill(white)

    # Loop through all events of the program
    for event in pygame.event.get():

        # Check the pygame quit status
        if event.type == pygame.QUIT:
            # Exit the game
            sys.exit(0)

        # Movement of player based on the key input
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                playerXPositionChange = 5

            if event.key == pygame.K_LEFT:
                playerXPositionChange = -5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerXPositionChange = 0

        # Boundaries of the player image if the image: Starts at right of the screen,
        # stays at right of the screen, and doesn't go past that boundary
        if playerXPosition >= (width - pixel):
            playerXPosition = (width - pixel)

        # Boundaries of the player image if the image: starts at left end, stays at left end, and doesn't go past
        # that boundary
        if playerXPosition <= 0:
            playerXPosition = 0

        # Multiple block movement, one after another, and the conditions implemented.
        if height - 0 <= blockYPosition <= (height + 200):
            blockYPosition = 0 - pixel

            # Randomly assign value in range
            blockXPosition = random.randint(0, (width - pixel))

        # Movement of player image after change made
        playerXPosition += playerXPositionChange

        # Movement of block image after change made
        blockYPosition += blockYPositionChange

        # player function is called
        player(playerXPosition, playerYPosition)

        # block function is called
        block(blockXPosition, blockYPosition)

        # collision function is called
        collision()

        # Update the screen using the pygame update display function
        pygame.display.update()

# EOF
