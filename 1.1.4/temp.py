import turtle as trtl
painter = trtl.Turtle()

x = input("What is the value of x? ")
while (x != 0):
    painter.forward(100)
    painter.right(90)

wn = trtl.Screen()
wn.mainloop()