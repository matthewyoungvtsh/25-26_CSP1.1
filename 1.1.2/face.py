# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

# head
painter.pencolor('black')
painter.circle(150)

#mouth
painter.penup()
painter.left(90)
painter.forward(30)
painter.left(90)
painter.forward(50)
painter.left(180)
painter.pendown()
painter.circle(180, 45)

#nose
painter.penup()
painter.left(50)
painter.forward(20)
painter.left(90)
painter.forward(90)
painter.pendown()
painter.forward(30)
painter.right(180)
painter.circle(25,  90)
painter.forward(10)
painter.penup()

#left eye
painter.forward(30)
painter.right(90)
painter.forward(30)
painter.pendown()
painter.circle(180, 30)
painter.penup()

#right eye
painter.left(150)
painter.forward(220)
painter.left(90)
painter.forward(25)
painter.left(90)
painter.pendown()
painter.circle(120, 25)

#right eyebrow
painter.penup()
painter.forward(15)
painter.left(150)
painter.pendown()
painter.circle(140, 30)

#left eyebrow
painter.up()
painter.left(140)
painter.forward(120)
painter.left(90)
painter.forward(30)
painter.right(90)
painter.forward(50)
painter.left(180)
painter.pendown()
painter.circle(150, 40)

wn = trtl.Screen()
wn.mainloop()