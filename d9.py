import turtle

rohan = turtle.Turtle()
def A(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + 200)
    t.goto(x + 80, y + 200)
    t.goto(x + 80, y + 150)
    t.goto(x, y + 150)
    t.goto(x + 80, y + 150)
    t.goto(x + 80, y)
def P(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + 200)
    t.goto(x + 80, y + 200)
    t.goto(x + 80, y + 150)
    t.goto(x, y + 150)

def ex(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(3)
    t.penup()
    t.goto(x, y + 15)
    t.pendown()
    t.goto(x, y + 200)
ex(rohan, 0, 0)
turtle.done()
