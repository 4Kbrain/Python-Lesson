import turtle


t = turtle.Turtle()

for _ in range(6):
    t.forward(100)
    t.left(60)


t.penup()
t.goto(0, 0)
t.pendown()
t.write("hexagon", align="center", font=("Arial", 16, "normal"))


t.hideturtle()


turtle.done()