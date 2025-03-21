import turtle
import math


t = turtle.Turtle()
t.speed(3)  


def A(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x, y+200)
    t.goto(x+80, y+200)
    t.goto(x+80, y+120)
    t.goto(x, y+120)
    t.goto(x+80, y+120)
    t.goto(x+80, y)

def B(t, x, y):
    t.penup()
    t.goto(x+12.5, y+13)
    t.pendown()
    t.goto(x+67.5, y+13)
    t.goto(x+67.5, y+187.5)
    t.goto(x+12.5, y+187.5)
    t.goto(x+22.5, y+187.5)
    t.goto(x+22.5, y+13)
    t.goto(x+22.5, y+105)
    t.goto(x+67.5, y+105)
    
    t.goto(x+55, y+120)
    t.goto(x+35, y+120)
    t.goto(x+22.5, y+105)
    t.goto(x+22.5, y+187.5)
    t.goto(x+35, y+172.5)
    t.goto(x+55, y+172.5)
    t.goto(x+67.5, y+187.5)
    t.goto(x+22.5, y+187.5)
    t.goto(x+10, y+175)
    t.goto(x, y+175)
    t.goto(x+12.5, y+187.5)
    t.goto(x, y+200)
    t.penup()
    t.goto(x+22.5, y+105)
    t.pendown()
    t.goto(x+35, y+90)
    t.goto(x+55, y+90)
    t.goto(x+67.5, y+105)
    t.goto(x+67.5, y+13)
    t.goto(x+55, y+27.5)
    t.goto(x+35, y+27.5)
    t.goto(x+22.5, y+13)
    t.goto(x+10, y+25)
    t.goto(x, y+25)
    t.goto(x+12.5, y+13)
    t.goto(x, y)

def C(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+200)
    t.goto(x+80,y+200)
    t.goto(x+80,y+150)
    t.goto(x+80,y+200)
    t.goto(x,y+200)
    t.goto(x,y)
    t.goto(x+80,y)
    t.goto(x+80,y+50)

def D(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+200)
    t.goto(x+60, y+200)
    t.goto(x+80, y+175)
    t.goto(x+80, y+25)
    t.goto(x+60, y)
    t.goto(x,y)

def E(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+80,y)
    t.goto(x,y)
    t.goto(x,y+200)
    t.goto(x+80,y+200)
    t.goto(x,y+200)
    t.goto(x,y+100)
    t.goto(x+80,y+100)
    t.goto(x,y + 100)

def F(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+200)
    t.goto(x+80,y+200)
    t.penup()
    t.goto(x,y+100)
    t.pendown()
    t.goto(x+80,y+100)

def G(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+200)
    t.goto(x+80,y+200)
    t.goto(x+80,y+180)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+80,y)
    t.goto(x+80,y+100)
    t.goto(x+40,y+100)

def H(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x, y+200)
    t.goto(x, y+100)
    t.goto(x+80, y+100)
    t.goto(x+80, y+200)
    t.goto(x+80, y+1)

def I(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+80, y)
    t.goto(x+40, y)
    t.goto(x+40, y+200)
    t.goto(x+80, y+200)
    t.goto(x, y+200)


def letter_positions_on_circle(radius, num_letters, center_x, center_y):
    positions = []
    angle_step = 360 / num_letters  
    for i in range(num_letters):
        angle = math.radians(i * angle_step)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        positions.append((x, y))
    return positions

def draw_circle_with_letters():
    radius = 200
    num_letters = 8
    center_x = -150  
    center_y = -100  
    positions = letter_positions_on_circle(radius, num_letters, center_x, center_y)
    letter_functions = [A, B, C, D, E, F, G, H]
    for i, pos in enumerate(positions):
        x, y = pos
        letter_functions[i](t, x, y)
draw_circle_with_letters()

turtle.done()
