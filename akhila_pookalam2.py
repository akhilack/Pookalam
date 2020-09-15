import turtle
import math

design = turtle.Turtle()
design.hideturtle()
design.speed(0)

# set bg color
design.getscreen().bgcolor("white")
#circle
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
circle("black",290)
circle("red",280)
circle("orange",270)
circle("yellow",260)
circle("white",250)

# base design
design.color("purple")
for i in range(12) :
    design.begin_fill()
    design.circle(120)
    design.circle(-120)
    design.left(30)
    design.end_fill()

def square(n,color,size,angle):
    design.color(color)
    design.begin_fill()
    for j in range(n):
      for i in range(4):
        design.forward(size)
        design.left(90)
      design.left(angle)
    design.end_fill()
square(13,"red",180,30)

for j in range(13) :
  # design three --petals
  def draw_petal(turtle, radius):
      heading=turtle.heading()
      turtle.circle(radius,60)
      turtle.left(120)
      turtle.circle(radius,60)
      turtle.setheading(heading)
  def petal(my_petals,my_radius,c):
      for i in range(my_petals):
          design.color(c)
          design.fillcolor(c)
          design.begin_fill()
          draw_petal(design,my_radius)
          design.left(360/my_petals)
          design.end_fill()
design.speed(0)
petal(60,200,"yellow")

circle("white",170)
circle("purple",160)
circle("white",150)
square(6,"black",130,60)
square(10,"white",120,60)
square(10,"red",110,60)
square(10,"green",100,60)
square(10,"yellow",90,60)
circle("white",90)
petal(12,90,"black")
petal(12,70,"red")
petal(12,50,"yellow")
petal(12,20,"white")

turtle.done() 
