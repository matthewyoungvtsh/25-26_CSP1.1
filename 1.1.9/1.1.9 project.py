import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

'''#cat's tail
painter.left(180)
painter.circle(250, 35)
painter.left(110)
painter.circle(10, 50)
painter.penup()
painter.setposition(0, -10)
painter.pendown()
painter.left(165)
painter.circle(262, 31)
painter.penup()

#cat's body
painter.setposition(45, 130)
painter.setheading(210)
painter.pendown()
for x in range(2):
    painter.circle(110, 45)'''


#cat's head
painter.setheading(320)
painter.circle(50, 80)
painter.teleport(33,86)
painter.setheading(180)

b = 1
x = 1
for x in range(2):
    painter.circle(100, 25*b)
    painter.circle(100, 20*b)
    painter.circle(30, 15*b)
    painter.circle(20, 30*b)
    painter.circle(15, 30*b)
    painter.circle(70, 20*b)
    painter.circle(70, 26*b)
    painter.teleport(31, 86)
    painter.setheading(180)
    x +=1
    b = -1

#ears
painter.teleport(-5, 75)
a = 1
c = 0
for a in range(2):
    painter.setheading(130 +c)
    painter.forward(50)
    painter.setheading(280 +c)
    painter.forward(55)
    painter.teleport(95, 60)
    c = -60

wn = trtl.Screen()
wn.mainloop()