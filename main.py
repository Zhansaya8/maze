import turtle
from tkinter import PhotoImage
import math
from turtle import Turtle, Screen, Shape

# https://www.youtube.com/watch?v=sVUNibx2gxc

wn = turtle.Screen()
wn.bgcolor("purple")
wn.title("Try To Get Out")
wn.setup(900, 600)
wn.tracer(0)

turtle.register_shape("quokka.gif")
turtle.register_shape("nut.gif")
turtle.register_shape("grass.gif")
# substitute 'subsample' for 'zoom' if you want to go smaller:
screen = Screen()
quokka = PhotoImage(file="quokka.gif").subsample(20, 20)
screen.addshape("quokka", Shape("image", quokka))

nut = PhotoImage(file="nut.gif").subsample(20, 20)
screen.addshape("nut", Shape("image", nut))

grass = PhotoImage(file="grass.gif").subsample(20, 20)
screen.addshape("grass", Shape("image", grass))

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("quokka")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.score = 0

    def up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24

        if (move_x, move_y) not in walls:
            self.goto(move_x, move_y)

    def down(self):
        move_x = player.xcor()
        move_y = player.ycor() - 24

        if (move_x, move_y) not in walls:
            self.goto(move_x, move_y)

    def left(self):
        move_x = player.xcor() - 24
        move_y = player.ycor()

        if (move_x, move_y) not in walls:
            self.goto(move_x, move_y)

    def right(self):
        move_x = player.xcor() + 24
        move_y = player.ycor()

        if (move_x, move_y) not in walls:
            self.goto(move_x, move_y)

    def is_win(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        d = math.sqrt((a**2) + (b ** 2))

        if d < 10:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("nut")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.score = 100
        self.goto(x, y)

    def delete(self):
        self.goto(2000, 2000)
        self.hideturtle()

levels=[""]

level_1=[
    "XXXXXXXXXXXXXXXXXXXPXXXXX   ",
    "X                 X X    X X",
    "X XXXX   XXXXXXXX X XX X XXX",
    "X X               X    X X X",
    "X XXXXXXXXXXXXXXX          X",
    "X XXXXXXXX     XXXXXXXXXXX X",
    "X XXXXXXXX XXX XXXXXXXXXXX X",
    "XXXXXX     XXX             X",
    "  XXXX XXXXXXXXXXX XXXXXXXXX",
    "XXXXXX XXXXXXXXXXX XXXXXXXX ",
    "X XXXX       XXXXX XXXXXXX X",
    "X XXXXXXXXXX XX    XXXXXXX X",
    "X X          XX XXXXXXXXXX X",
    "X    XXXXXXX XX X        X X",
    "XX           XX XXXXXXXXXX X",
    "  XXXXXXXXXX  X            X",
    "  XXXXXXXXXXXTXXXXXXXXXXXXXX"
]

level_2=[
    "XXXXXXXXXXXX XXXXXXXXX      ",
    "X          XP     X X    X X",
    "X XXXX   XXX  XXX X XX X XXX",
    "X X          X    X    X X X",
    "X XX    XXXX XXXX          X",
    "X XX XXXXX     XXXXXXXXXXX X",
    "X XX XXXXX XXX XXXXXXXXXXX X",
    "XXX  X     XXX             X",
    "  X XX XXXXXXXXXXX XXXXXXXXX",
    "XXX XX XXXXXXXXXXX XXXXXXXX ",
    "X X XX       XXXXX XXXXXXX X",
    "X X XXXXXXXX XX    XXXXXXX X",
    "XT  X        XX XXXXXXXXXX X",
    "X    XXXXXXX XX X        X X",
    "X               XXXXXXXXXX X",
    "X                          X",
    "  XXXXXXXXXX  X            X"

]

level_3=[
    "XXXXXXXXXXXXXXXXXXXPXXXXX   ",
    "X                 X X    X X",
    "X XXXX   XXXXXXXX X XX X XXX",
    "X X               X    X X X",
    "X XXXXXXXXXXXXXXX          X",
    "X XXXXXXXX     XXXXXXXXXXX X",
    "X XXXXXXXX XXX XXXXXXXXXXX X",
    "XXXXXX     XXX             X",
    "  XXXX XXXXXXXXXXX XXXXXXXXX",
    "XXXXXX XXXXXXXXXXX XXXXXXXX ",
    "X XXXX       XXXXX XXXXXXX X",
    "X XXXXXXXXXX XX    XXXXXXX X",
    "X X          XX XXXXXXXXXX X",
    "X XXXXXXXXXX XX X        X X",
    "XXT          XX XXXXXXXXXX X",
    "  XXXXXXXXXX  X            X",
    "  XXXXXXXXXXX XXXXXXXXXXXXXX"
]

level_4=[
    "XXXXXXXXXXXXXXXXXXXPXXXXX   ",
    "X                 X X    X X",
    "X XXXX   XXXXXXXX X XX X XXX",
    "X X               X    X X X",
    "X XXXXXXXXXXXXXXX          X",
    "X XXXXXXXX     XXXXXXXXXXX X",
    "X XXXXXXXX XXX XXXXXXXXXXX X",
    "XXXXXX     XXX             X",
    "  XXXX XXXXXXXXXXX XXXXXXXXX",
    "XXXXXX XXXXXXXXXXX XXXXXXXX ",
    "X XXXX       XXXXX XXXXXXX X",
    "X XXXXXXXXXX XX    XXXXXXX X",
    "X X          XX XXXXXXXXXX X",
    "X XXXXXXXXXX XX X        XTX",
    "XX           XX XXXXXXXXXX X",
    "  XXXXXXXXXX  X            X",
    "  XXXXXXXXXXX XXXXXXXXXXXXXX"
]
treasures = []
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("grass")
                pen.stamp()

                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

pen = Pen()
player = Player()

walls = []


setup_maze(level_1)
pen.write("Score: {}".format(player.score))


turtle.listen()
turtle.onkey(player.left, "Left")
turtle.onkey(player.right, "Right")
turtle.onkey(player.up, "Up")
turtle.onkey(player.down, "Down")

wn.tracer(0)

while True:
    for treasure in treasures:
        if player.is_win(treasure):
            player.score += treasure.score
            print("Player Score: {}".format(player.score))

            treasure.delete()

            treasures.remove(treasure)
            if player.score == 100:
                levels.remove(level_1)


                pen.clear()
                pen.write("Score: {}".format(player.score))
                setup_maze(level_2)
            elif player.score == 200:

                pen.clear()
                pen.write("Score: {}".format(player.score))
                setup_maze(level_3)
            elif player.score == 300:

                pen.clear()
                pen.write("Score: {}".format(player.score))
                setup_maze(level_4)
            elif player.score == 400:
                pen.clear()
                pen.write("Total score: {}".format(player.score))

    wn.update()