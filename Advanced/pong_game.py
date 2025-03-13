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

def pong_game():
    game_components = setup_game()
    screen, ball, l_paddle, r_paddle, score_board = game_components
    l_score, r_score = 0, 0
 # Define movement functions
    def l_paddle_up():
        l_paddle.sety(l_paddle.ycor() + 20)

    def l_paddle_down():
        l_paddle.sety(l_paddle.ycor() - 20)

    def r_paddle_up():
        r_paddle.sety(r_paddle.ycor() + 20)

    def r_paddle_down():
        r_paddle.sety(r_paddle.ycor() - 20)

         # Map keyboard inputs to paddle movement
    screen.listen()
    screen.onkeypress(l_paddle_up, 'e')  # Left paddle moves up with 'e'
    screen.onkeypress(l_paddle_down, 'x')  # Left paddle moves down with 'x'
    screen.onkeypress(r_paddle_up, 'Up')  # Right paddle moves up with 'Up Arrow'
    screen.onkeypress(r_paddle_down, 'Down')  # Right paddle moves down with 'Down Arrow'