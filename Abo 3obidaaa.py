
# Ahmed Mohamed Fawzy Abd El-Hady (IT Department)
# Code: 808965876

from turtle import *
from time import *
from random import *

from winsound import *

# Initials
levels = numinput("Levels", "Please Choose Level\n     1.Easy \n     2.Medium \n     3.Hard", 1, 1, 3)
if levels == 1:
    delay = 0.17
elif levels == 2:
    delay = 0.1
else:
    delay = 0.04

score = 0
high_score = 0
segments = []

# Screen
win = Screen()
win.title("UnSet Team")
win.bgpic("image1.png")
win.setup(650, 650)
win.tracer(0)

# Game Border
border = Turtle()
border.hideturtle()
border.width(4)
border.color("#000000")
border.up()
border.goto(-250, 250)
border.down()
border.setx(250)
border.sety(-250)
border.setx(-250)
border.sety(250)

# Snake Head
head = Turtle()
head.shape("circle")
head.color("black", "#376b02")
head.up()
head.direction = "Stop"  # direction New Attribute set its value "stop" added to head object

# Snake Food
food = Turtle()
food.shape("circle")
food.color("black", "red")  # pencolor , fillcolor
food.speed(0)  # 'fastest'
food.up()  # Pull The Pun up
x = randint(-225, 225)  # Random Integer
y = randint(-225, 225)
food.goto(x, y)

# Score
Scorepos = Turtle()
Scorepos.color("black")
Scorepos.up()
Scorepos.speed(0)  # 'fastest'
Scorepos.hideturtle()  # alis ==> ht
Scorepos.goto(0, 275)
Scorepos.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Times New Roman", 22, "bold"))

# Directions
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)    # set the turtle coordinates without changing the other value
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


listen()  # Listening for keyboard input
onkeypress(goup, "Up")   # bind arrow keys to movement functions
onkeypress(godown, "Down")
onkeypress(goleft, "Left")
onkeypress(goright, "Right")


# onkeypress(up, "w")
# onkeypress(down, "s")
# onkeypress(left, "a")
# onkeypress(right, "d")

def setIncreaseBodySound():
    PlaySound("./sound.wav", SND_FILENAME | SND_ASYNC)


# Gameplay Runtime
while True:
    win.update()
    # check if the snake hits the border
    if head.xcor() > 225 or head.xcor() < -225 or head.ycor() > 225 or head.ycor() < -225:
        sleep(1)  # Delay Execution
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        Scorepos.clear()  # Delete the turtle's drawings from the screen.
        Scorepos.write("Score: {}   High Score: {}".format(score, high_score), align="center",
                       font=("Times New Roman", 22, "bold"))
    if head.distance(food) < 20:      # ... (Code to detect if the snake eats the food)
        x = randint(-225, 225)
        y = randint(-225, 225)
        food.goto(x, y)

        # Adding Segments
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black", "#80c445")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        setIncreaseBodySound()
        if score > high_score:
            high_score = score
        Scorepos.clear()
        Scorepos.write("Score: {}   High Score: {}".format(score, high_score), align="center",
                       font=("Times New Roman", 22, "bold"))

    # Checking For Head Collisions With Body Segments        # ... (Code to detect if the snake collides with itself)
    for index in range(len(segments) - 1, 0, -1): # 3 --> 0 # 3 2 1
        x = segments[index - 1].xcor() # x = segments[2].xcor
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            Scorepos.clear()
            Scorepos.write("Score: {}   High Score: {}".format(score, high_score), align="center",
                           font=("Times New Roman", 22, "bold"))

    sleep(delay)
