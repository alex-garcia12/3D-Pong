from visual import *

width = 24
thickness = 0.5
side = 10
center = vector(0, 0, 0)

wall_l = box(pos = vector(center.x - 30, center.y, center.z), length=thickness, height=side, width=side, color=color.white, opacity = 0.3)
wall_r = box(pos = vector(center.x + 30, center.y, center.z), length=thickness, height=side, width=side, color=color.white, opacity = 0.3)

ball = sphere(pos=(0,1,0), color=color.red, radius = 1.0)
ball.velocity = vector(-30,0,0)
wall_l.velocity = vector(0,5,0)

ihat = vector(1, 0, 0)
jhat = vector(0, 1, 0)
khat = vector(0, 0, 1)

moving_up = False
moving_down = False

def keyInput(evt):
    s = evt.key
    print('keyhit', evt.key)
    if s == 'w':
        wall_l.velocity.y -= 10
    elif s == 's':
        wall_l.velocity.y += 10

def over_wall_l(ball, wall_l):
    wpos = wall_l.pos
    bpos = ball.pos
    wleft = wpos.x - width/2
    wright = wpos.x + width/2
    wfront = wpos.z + width/2
    wback = wpos.z - width/2
    return ball.pos.x

def over_wall_r(ball, wall_r):
    wpos = wall_r.pos
    bpos = ball.pos
    wleft = wpos.x - width/2
    wright = wpos.x + width/2
    wfront = wpos.z + width/2
    wback = wpos.z - width/2
    return ball.pos.x

scene.bind('keydown', keyInput)
dt = 0.01
counter = 0
while 1:
    rate(100)
    ball.pos += ball.velocity*dt
    wall_l.pos += wall_l.velocity*dt
    
    if over_wall_l(ball, wall_l) and (ball.x - ball.radius <= wall_l.x) or over_wall_r(ball, wall_r) and (ball.x - ball.radius >= wall_r.x):
        ball.velocity.x *= -1
#    else:
#        ball.velocity.y += -9.8*dt
    if (counter % 10) == 9:
        sphere(pos = ball.pos, color = color.yellow, radius = ball.radius/5)
#        arrow(pos = ball.pos, color = color.green, axis = ball.velocity.x * ihat, shaftwidth = 0.1)
#        arrow(pos = ball.pos, color = color.red, axis = ball.velocity.y * jhat, shaftwidth = 0.1)
#        arrow(pos = ball.pos, color = color.white, axis = ball.velocity.z * khat, shaftwidth = 0.1)
    counter += 1
    if scene.mouse.clicked > 0:
        scene.mouse.getclick()
        scene.mouse.getclick()
