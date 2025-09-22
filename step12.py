# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What is the color of the circle? ")

# ask user for the radius of a circle
circle_radius = int(input("What is the circle radius? "))

# draw a circle with the radius and line color entered by the user
painter.pencolor(color)
painter.circle(circle_radius)
painter.penup()
painter.up(30)
painter.forward(40)
painter.circle(

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()