import turtle

def draw_rectangle(width, height):
    """
    指定された幅と高さで長方形を描画します。
    """
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def write_text(text):
    """
    指定されたテキストをより上の位置に描画します。
    """
    turtle.penup()
    turtle.goto(-50, 50)  
    turtle.pendown()
    turtle.write(text, font=("Arial", 16, "normal"))
    turtle.penup()

def main():
    turtle.speed(1)  

    
    write_text("rectangle")

    
    turtle.goto(-100, -50)
    turtle.pendown()

    
    draw_rectangle(200, 100)

    turtle.done()

if __name__ == "__main__":
    main()