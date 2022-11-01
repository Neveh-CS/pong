"""
if you get stuck or dont understand any of the turtle functions
you can read all the other functions built into turtle in their documentaion 
https://www.geeksforgeeks.org/turtle-programming-python/
"""

# RE CREATE THIS WHOLE SCRIPT ON YOUR OWN AND TRY TO MESS WITH IT AND CUSTOMIZE IT

# import the turtle module
import turtle

# create the canvas and set its color, size and title
wn = turtle.Screen()
wn.title('PONG by Yehuda')
wn.bgcolor('black')
wn.setup(width=800, height=600)
# the .tracer() method sets how long it takes to 
# transition between changes we make to the canvas
# 0 is instant
wn.tracer(0)


# variables to keep track of the score
score_a = 0
score_b = 0

# create a new turtle (paddle a)
paddle_a = turtle.Turtle()
# set speed to 0 (fastest) (0-10, 10 being slowest)
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# set initial position of paddle
paddle_a.goto(-350, 0)

# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# set the delta (velocity) this is the amount that 
# we move the ball during each "frame" of the animation
ball.dx = .01
ball.dy = .01

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))



# functions for moving the paddles up and down along the y axis
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding to call the paddle moving functions
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# main game loop
# this is the loop that "runs" the game 
# each time this while loop loops that results in 1 frame of "animation"
# as long as this loop continues to loop, we have continued gameplay
# this is a weird type of loop that wont end unless stopped manually
# {note the lack of exit condition for the loop, its just True instead of a normal while loop} 
while True:
    # this updates the canvas at the beginning of each iteration of the loop
    wn.update()
    
    # set the value of the x coordinate to the current x plus the delta (also the y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # check if ball hits ceiling or floor
    if ball.ycor() > 290:
        ball.sety(290)
        # reverse the direction of the delta (a "bounce")
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # check if ball passes thru right side 
    if ball.xcor() > 390:
        # put the ball back in the center
        ball.goto(0, 0)
        # flip delta
        ball.dx *= -1
        # increment score
        score_a += 1
        # clear old score and replace it with updated score
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # same thing just for the other side
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

        
    # check if ball hits the paddle and "bounce" it the other way
    # check if the x and y coordinates of the ball are within the x and y of the padle
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
    
    # same thing but negative so it works for the other paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        
        

"""
things to try;
    try making the initial direction of the ball random
    try making the ball go faster as the game goes on
    try making the background show a net or some shit

"""