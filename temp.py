#multiply 8 x 4,through addition
import turtle as trtl
painter = trtl.Turtle()

painter.shape('circle')
painter.turtlesize(2)

# multiply 800 x 10000
for t in range(18):
    painter.stamp()
    painter.right(20)
    painter.forward(20)

wn = trtl.Screen()
wn.mainloop()