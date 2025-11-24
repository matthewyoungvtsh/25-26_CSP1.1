import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

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

#eyes
painter.teleport(-15, 50)
e = 0
for e in range(2):
    painter.setheading(340)
    painter.circle(40, 45)
    painter.setheading(160)
    painter.circle(40,45)
    painter.teleport(45,50)

if e >= c:
    painter.teleport(0, 48)
    f = 0
    for f in range(2):
        painter.setheading(0)
        painter.circle(3, 360)
        painter.penup()
        painter.forward(60)
        painter.pendown()

#lips
painter.setheading(350)
painter.teleport(3, 12)

l = 0
for l in range(2):
    painter.circle(170, 20)
    painter.setheading(170)
    l += 1
painter.setheading(0)
painter.forward(60)

#nose
painter.teleport(32, 27)
painter.circle(4)

#whiskers
painter.teleport(-10, 35)
painter.setheading(170)
painter.forward(60)
painter.setheading(200)
painter.forward(60)

wn = trtl.Screen()
wn.mainloop()