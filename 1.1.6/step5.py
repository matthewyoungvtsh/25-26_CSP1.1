#   a116_buggy_image.py
import turtle as trtl
# painter is the turtle
painter = trtl.Turtle()

#creating the spiders body
painter.pensize(40)
painter.circle(20)

#creating the spiders legs
#legs is the number of legs on the spider
legs = 8
#length is the length of the longest legs
length = 70
#distance between legs, in degrees of the circle
d = 360 / legs

#creating the spiders legs
painter.pensize(5)
#i is the incrementing counter in the following while loop
i = 0
#the loop that makes the legs
while (i < legs):
  painter.goto(0,20)
  painter.setheading(d*i)
  painter.forward(length)
  i = i + 1
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
