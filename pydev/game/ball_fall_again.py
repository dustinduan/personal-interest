import pgzrun as pg
r=10
y=10
def draw():
    screen.fill('red')
    screen.draw.filled_circle((150,y),r,'green')
    screen.draw.filled_circle((400,y),r,'yellow')
    screen.draw.filled_circle((650,y),r,'purple')
def update():
    global y
    y=y+1
    if(y>600):
        y=0
    
pg.go()
