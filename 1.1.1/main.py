import turtle as trtl

painter = trtl.Turtle()

painter.speed(10)
painter.color('purple')
painter.fillcolor('orange')
painter.forward(40)
painter.right(120)
painter.forward(40)
painter.right(120)
painter.forward(80)
painter.circle(80)

wn = trtl.Screen()
wn.mainloop()