#  # import random
#  #
#  # for i in range(10):
#  #     print(random.random())
#
#
#
#
#
#
#
#  # import random
#  #
#  # for i in range(10):
#  #     print(random.randint(25,35))
#
#
#
#
#
#
#
#
#  # import math
#  #
#  # a = int(input("enter a: "))
#  # b = int(input("enter b: "))
#  #
#  # c = math.sqrt(a**2 + b**2)
#  #
#  #
#  # print(c)
#  #






#  # import math
#  #
#  # a = int(input("enter a: "))
#  # b = int(input("enter b: "))
#  #
#  # c = math.hypot(a,b)
#  #
#  # print(c)






# # # import math
# # #
# # # def areaofCircle(r):
# # #     area = (math.pi * r**2)
# # #     return area
# # #
# # # print(areaofCircle(10))
#
#
#
#
#
#
# #
# # # import turtle
# # #
# # # def drawstar(t, side):
# # #     for i in range(5):
# # #         t.forward(side)
# # #         t.right(144)
# # #
# # # tess = turtle.Turtle()
# # # screen = turtle.Screen()
# # #
# # # drawstar(tess, 100)
# # # screen.exitonclick()
# #
#
#
#
#
#
#
# #
# import turtle
# t= turtle.Turtle()
# screen = turtle.Screen()
# color = input("What is your favorite color? ")
# t.fillcolor(color)
# side = int(input("Enter the number of the sides "))
# length = int(input("Enter the length of each side: "))
# t.begin_fill()
# for i in range(side):
#
#     t.forward(length)
#     t.left(360 / side)
#
# # Boyama işlemini bitir
# t.end_fill()
# screen.exitonclick()
# #
# #
#
#
#
#
# import turtle
# def  drawSquare(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(5):
#     drawSquare(tess,20)
#     tess.penup()
#     tess.forward(30)
#     tess.pendown()
#
# screen.exitonclick()
#
#
#
#
#
#
#
#
#
# import turtle
#
# def  drawSquare(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
# screen.bgcolor("lightgreen")
# tess.color("blue")
# tess.pensize(3)
#
# for i in range(20,120,20):
#     drawSquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
#
#
# screen.exitonclick()