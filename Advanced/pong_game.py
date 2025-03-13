import turtle
import os

# Initialize Turtle Screen
def setup_game():
    screen = turtle.Screen()
    screen.title('Pong Arcade Game')  # Set window title
    screen.bgcolor('white')  # Set background color
    screen.setup(width=1000, height=600)  # Set window dimensions

# Define paddles
    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    l_paddle.shape('square')
    l_paddle.color('red')
    l_paddle.shapesize(stretch_wid=6, stretch_len=2)
    l_paddle.penup()
    l_paddle.goto(-400, 0)

    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    r_paddle.shape('square')
    r_paddle.color('black')
    r_paddle.shapesize(stretch_wid=6, stretch_len=2)
    r_paddle.penup()
    r_paddle.goto(400, 0)

  # Define ball
    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = -5

     # Define scoreboard
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color('blue')
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    score_board.write('Left Player: 0 -- Right Player: 0', align='center', font=('Arial', 24, 'normal'))

    return screen, ball, l_paddle, r_paddle, score_board