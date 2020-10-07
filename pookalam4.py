import turtle
import math

design = turtle.Turtle()
design.speed(0)

# set bg color
design.getscreen().bgcolor("white")

# outer circle
design.color("black")
design.begin_fill()
design.penup()
design.right(90)
design.forward(280)
design.left(90)
design.pendown()
design.circle(290)
design.penup()
design.left(90)
design.forward(290)
design.right(90)
design.pendown()
design.end_fill()

#2nd circle
design.color("red")
design.begin_fill()
design.penup()
design.right(90)
design.forward(280)
design.left(90)
design.pendown()
design.circle(280)
design.penup()
design.left(90)
design.forward(280)
design.right(90)
design.pendown()
design.end_fill()

design.color("orange")
design.begin_fill()
design.penup()
design.right(90)
design.forward(270)
design.left(90)
design.pendown()
design.circle(270)
design.penup()
design.left(90)
design.forward(270)
design.right(90)
design.pendown()
design.end_fill()

design.color("yellow")
design.begin_fill()
design.penup()
design.right(90)
design.forward(260)
design.left(90)
design.pendown()
design.circle(260)
design.penup()
design.left(90)
design.forward(260)
design.right(90)
design.pendown()
design.end_fill()

design.color("black")
design.begin_fill()
design.penup()
design.right(90)
design.forward(250)
design.left(90)
design.pendown()
design.circle(250)
design.penup()
design.left(90)
design.forward(250)
design.right(90)
design.pendown()
design.end_fill()
# design 2
def shape(size,side):
    for i in range(side):
        design.forward(size)
        design.left(360/side)

# base design
design.color("blue")
for i in range(10) :
    design.begin_fill()
    design.circle(120)
    design.circle(-120)
    design.left(45)
    design.end_fill()



#for square
for j in range(13) :
  design.color("white")
  design.begin_fill()
  shape(178,4)
  design.left(30)
  design.end_fill() 

design.color("blue")
design.begin_fill()
design.penup()
design.right(90)
design.forward(200)
design.left(90)
design.pendown()
design.circle(200)
design.penup()
design.left(90)
design.forward(200)
design.right(90)
design.pendown()
design.end_fill()

design.color("yellow")
design.begin_fill()
design.penup()
design.right(90)
design.forward(190)
design.left(90)
design.pendown()
design.circle(190)
design.penup()
design.left(90)
design.forward(190)
design.right(90)
design.pendown()
design.end_fill()

# second set of squares
for j in range(36):
  design.color("white")
  design.begin_fill()
  shape(130, 4)
  design.left(10)
  design.end_fill()


design.color("black")
design.begin_fill()
design.penup()
design.right(90)
design.forward(170)
design.left(90)
design.pendown()
design.circle(170)
design.penup()
design.left(90)
design.forward(170)
design.right(90)
design.pendown()
design.end_fill()

design.color("green")
design.begin_fill()
design.penup()
design.right(90)
design.forward(160)
design.left(90)
design.pendown()
design.circle(160)
design.penup()
design.left(90)
design.forward(160)
design.right(90)
design.pendown()
design.end_fill()

design.color("red")
design.begin_fill()
design.penup()
design.right(90)
design.forward(150)
design.left(90)
design.pendown()
design.circle(150)
design.penup()
design.left(90)
design.forward(150)
design.right(90)
design.pendown()
design.end_fill()



#third set of shapes
  #hexagon
design.color("yellow")
design.begin_fill()
for j in range(10):

  shape(70, 6)
  design.left(35)
design.end_fill()
#pentagon
design.color("red")
design.begin_fill()
for j in range(9) :

  shape(60, 5)
  design.left(45)
design.end_fill()

#pentagon
design.color("white")
design.begin_fill()
for j in range(9) :

  shape(48, 5)
  design.left(45)
design.end_fill()

  #squares
design.color("pink")
design.begin_fill()
for j in range(10):

  shape(45, 4)
  design.left(35)
design.end_fill()
design.color("white")
design.begin_fill()
for j in range(10):

      shape(41, 4)
      design.left(35)
design.end_fill()
design.color("orange")
design.begin_fill()
for j in range(10):

  shape(38, 4)
  design.left(35)
design.end_fill()

design.color("gold")
design.begin_fill()
for j in range(10):

  shape(34, 4)
  design.left(35)
design.end_fill()
design.color("yellow")
design.begin_fill()
for j in range(10):

  shape(30, 4)
  design.left(35)
design.end_fill()

design.color("green yellow")
design.begin_fill()
for j in range(10):

  shape(26, 4)
  design.left(35)
design.end_fill()

design.color("lime")
design.begin_fill()
for j in range(10):
  shape(21, 4)
  design.left(35)
design.end_fill()

design.color("lime green")
design.begin_fill()
for j in range(10):
  shape(17, 4)
  design.left(35)
design.end_fill()

design.color("forest green")
design.begin_fill()
for j in range(10):
  shape(13, 4)
  design.left(35)
design.end_fill()

design.color("green")
design.begin_fill()
for j in range(10):

  shape(9, 4)
  design.left(35)
design.end_fill()


turtle.done() 
