# Birthday Game in Python 3 for Beginners
# By @SmurfsUp

import turtle
import random
from pygame import *
import sys
import time

mixer.init()
mixer.music.load("gabe_the_dog_tetris.mp3")
mixer.music.play(-1)

# Set up the screen
wn = turtle.Screen()
wn.title("Birthday Game by @SmurfsUp")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


score = 0


wn.register_shape("cake.gif")
wn.register_shape("candle.gif")


# Cake
cake = turtle.Turtle()
cake.speed(0)
cake.shape("cake.gif")
cake.color("white")
cake.penup()
cake.goto(0, -210)
cake.direction = "stop"


# Good things
candles = []

for _ in range(20):
    candle = turtle.Turtle()
    candle.speed(0)
    candle.shape("candle.gif")
    candle.color("green")
    candle.penup()
    candle.goto(-100, 250)
    candle.speed = random.randint(1, 2)

    candles.append(candle)

def go_left():
    cake.direction = "left"

def go_right():
    cake.direction = "right"

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Age: 0", align="center", font=("Courier", 24, "normal"))


running = True
while running:
    wn.update()

    # Move the player
    if cake.direction == "left":
        x = cake.xcor()
        x -= 0.5
        cake.setx(x)

    if cake.direction == "right":
        x = cake.xcor()
        x += 0.5
        cake.setx(x)

    if cake.xcor() < -390:
        cake.setx(-390)

    elif cake.xcor() > 390:
        cake.setx(390)

    for candle in candles:
        # Move the good things
        candle.sety(candle.ycor() - candle.speed)

        # Check if good things are off the screen
        if candle.ycor() < -300:
            candle.goto(random.randint(-300, 300), random.randint(400, 800))

        # Check for collisions
        if cake.distance(candle) < 40:
            # Score increases
            score += 1

            if score == 41:      # This Is Where You Change The Age
                wn.clear()
                pen.clear()
                wn.bgcolor("black")

                done = True
                while done:

                    penr = turtle.Turtle()
                    penr.hideturtle()
                    penr.penup()
                    penr.color("white")

                    mixer.music.pause()
                    mixer.music.load("centuryfox.mp3")
                    mixer.music.play()
                    from turtle import *

                    pensize(2)
                    colors = ["red", "yellow", "blue", "green", "red"]

                    penr.goto(0, 260)
                    penr.write("YOU MADE IT ALL THE WAY TO {}!".format(score), align="center", font=("Courier", 24, "normal"))

                    def shape():
                        for i in range(6):
                            forward(100)
                            for j in range(3):
                                forward(30)
                                right(120)
                            right(60)


                    for i in range(28):
                        colorchoice = random.choice(colors)
                        speed(0)
                        color(colorchoice)
                        shape()
                        right(11)


                    penr.goto(0, 0)
                    penr.write("HAPPY BIRTHDAY MOM!".format(score), align="center", font=("Comic Sans MS", 30, "normal"))

                    wn.update()


                    time.sleep(5)
                    sys.exit()



            # Show the score
            pen.clear()
            pen.write("Age: {}".format(score), align="center", font=("Courier", 24, "normal"))

            # Move the good thing back to the top
            candle.goto(random.randint(-300, 300), random.randint(400, 800))



wn.mainloop()