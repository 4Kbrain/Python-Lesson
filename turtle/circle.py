import turtle

def write_text(text):
    """
    指定されたテキストを描画します。
    """
    turtle.penup()
    turtle.goto(0, 0)  
    turtle.pendown()
    turtle.write(text, align="center", font=("Arial", 16, "normal"))
    turtle.penup()

def draw_circle(radius):
    
    """
    指定された半径で円を描画します。
    """
    turtle.goto(0, -radius)  
    turtle.pendown()
    
    turtle.circle(radius)
    turtle.penup()

turtle.speed(1)  

# "text circle"と書く
write_text("circle")


draw_circle(100)  

turtle.done()