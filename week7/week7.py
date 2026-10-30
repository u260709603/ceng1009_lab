# Example 1

# def sumTo(n):
#     total = n * (n + 1) / 2
#     return total
#
# print(sumTo(10))
#


# Example 2

# import turtle
#
# def drawStar(t,n ,size):
#     angle = (180 - 180 / n)
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 11, 100)
#
# wn.exitonclick()



# Example 3

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         return(total)
#
# print(sumTo(10))



# Example 4
#
# import math
#
# def mySqrt(x):
#     guess = x / 2
#     for i in range(20):
#         guess = ( 1 / 2 ) * (guess + (x / guess))
#     return guess
#
# n = int(input("Enter a positive integer: "))
# print(mySqrt(n))
# print(math.sqrt(n))



# Example 5

# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
#
#
# def Sprite(t, size):
#     for i in range(12):
#         t.forward(size)
#         t.left(180)
#         t.forward(size)
#         t.right(30)
#
# def fancySquare(t,sideofsquare,size):
#     for i in range(4):
#         t.forward(sideofsquare)
#         t.left(90)
#         Sprite(t,size)
#
#
# fancySquare(tess,100,20)
#
#
# wn.exitonclick()



# Example 5(part 2)

# import turtle
#
# wn = turtle.Screen()
# t = turtle.Turtle()
#
#
# def drawTip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size / 2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size / 2)
#     t.right(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         drawTip(someturtle, 10)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancySquare(t,legs, size,legsize):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#         drawSpriteWithTips(t,legs, legsize)
#
#
# fancySquare(t, 8, 100, 20)
# wn.exitonclick()



# Example 6

# def checkSign(n):
#     if n > 0:
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else:
#         return "zero"
#
# num_list = [-7, 5, 0]
#
# for number in num_list:
#     print(checkSign(number))
#
# n = int(input("Enter a number: "))
# print(checkSign(n))
#
#
#
# Example 7
import turtle

def drawBar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height + gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)

    border = 10
    gap = (maxheight - border) / 25

    wn =  turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40* num_bars + border
    top = maxheight + 4 + border
    wn.setworldcoordinates(-border, -border, right, top)

    t= turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t, height, gap)

    wn.exitonclick()


data= [48,117,200,240,160,220]

barChart(data)