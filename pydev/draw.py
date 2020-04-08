import turtle

def draw_rectangle(x,y,width=1,height,color1='red',color2='green'):
    """绘制矩形"""
    turtle.goto(x, y)
    turtle.pencolor(color1)
    turtle.fillcolor(color2)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
