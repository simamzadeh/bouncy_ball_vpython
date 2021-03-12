from vpython import *

ball = sphere(pos=vector(0,10,0), color = color.red)

surface = box(pos=vector(0,0,0), color=color.green, size=vector(10, 0.5, 10))

# box.color = color.yellow # changing the color after assignment
# box.pos gives the position of the box
# box.pos.x can change the specific coordinate x

n = 0
change = -0.1
while n < 200:
    rate(100)
    n += 1
    ball.pos.y = ball.pos.y + change
    if ball.pos.y < 0:
        change = -change