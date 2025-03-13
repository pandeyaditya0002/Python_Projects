import turtle
import os

# Initialize Turtle Screen
def setup_game():
    screen = turtle.Screen()
    screen.title('Pong Arcade Game')  # Set window title
    screen.bgcolor('white')  # Set background color
    screen.setup(width=1000, height=600)  # Set window dimensions
