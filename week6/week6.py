# -- setup --

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

# -- functions --

def drawPoly (someturtle, somesides, somesizes):
    angle = 360 / somesides
    for i in range (somesides):
        someturtle.forward(somesizes)
        someturtle.left(angle)

def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size = size + 2

def drawEquitriangle(someturtle, somesizes):
    drawPoly(someturtle, 3, somesizes)

def drawStar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawSprite(someturtle, legs, length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)

# -- exercises --

# Exercise 1
# tess.color("hotpink")
# drawPoly(tess, 8, 50)

# Exercise 2
# tess.color("blue")
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)

# Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)
#

# Exercise 4
# drawEquitriangle(tess,100)

# Exercise 5
# tess.pencolor("hotpink")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# for i in range(5):
#     drawStar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#

# Exercise 6
# drawSprite(tess, 15, 200)

# -- finish --

wn.exitonclick()
