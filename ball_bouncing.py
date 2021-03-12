from vpython import *

ball = sphere(pos=vector(0,10,0), color = color.red, velocity=vector(0,0,0))

surface = box(pos=vector(0,0,0), color=color.green, size=vector(10, 0.5, 10))

# box.color = color.yellow # changing the color after assignment
# box.pos gives the position of the box
# box.pos.x can change the specific coordinate x
g = -9.8
time_step = 0.01

n = 0 # n is the number of steps/ total time passed 
change = -0.1
while n < 1000:
    rate(100)
    n += 1

    # change and update velocity
    ball.velocity.y = ball.velocity.y + g*time_step

    # change and update position
    ball.pos.y = ball.pos.y + ball.velocity.y*time_step

    # ball.pos.y = ball.pos.y + change
    if ball.pos.y < 1 and ball.velocity.y < 0:
        ball.velocity.y = -ball.velocity.y

 