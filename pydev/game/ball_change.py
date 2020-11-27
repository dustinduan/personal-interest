import pgzrun as pg
r=10
def draw():
    screen.fill('red')
    screen.draw.filled_circle((150,300),r,'green')
    screen.draw.filled_circle((400,300),r,'yellow')
    screen.draw.filled_circle((650,300),r,'purple')
def update():
    global r
    r=r+1
pg.go()
