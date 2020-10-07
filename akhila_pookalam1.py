import turtle
import math

design = turtle.Turtle()
design.speed(0)

# set bg color
design.getscreen().bgcolor("white")

#Circle
def circle(color,radius):
    design.color(color)
    design.begin_fill()
    design.penup()
    design.right(90)
    design.forward(radius)
    design.left(90)
    design.pendown()
    design.circle(radius)
    design.penup()
    design.left(90)
    design.forward(radius)
    design.right(90)
    design.pendown()
    design.end_fill()
circle("red",290)
circle("green",280)
circle("red",270)
circle("orange",260)
circle("yellow",250)
circle("white",240)
circle("black",220)

#2nd design
def star(color,n,size,angle):
    design.color(color)
    design.begin_fill()
    for j in range(n):
      for i in range(4):
        design.forward(size)
        design.left(90)
      design.left(angle)
    design.end_fill()

star("black",12,175,30)
star("green",12,165,30)
star("red",12,155,30)
star("orange",12,145,30)
star("yellow",12,135,30)
star("white",12,125,30)

circle("black",145)
circle("yellow",135)
circle("white",125)

star("green",11,85,30)
star("red",10,85,60)

circle("yellow",85)
circle("black",75)
circle("white",65)

star("brown",10,45,35)
star("red",10,41,35)
star("orange",10,37,35)
star("gold",10,33,35)
star("yellow",10,29,35)
star("white",10,25,35)

circle("gold",25)
circle("yellow",20)
circle("white",10)
turtle.done()
