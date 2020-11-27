import pgzrun as pg
r=10
x=100
y=100
speed_x=3
speed_y=5
def draw():
    screen.fill('red')
    screen.draw.filled_circle((x,y),r,'green')
def update():
    global x,y,speed_x,speed_y
    x=x+speed_x
    y=y+speed_y
    if(x>800 or x<=0):
        speed_x=-speed_x
    if(y>600 or y<=0):
        speed_y=-speed_y    
pg.go()
