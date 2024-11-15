import turtle

my_turtle = turtle.Turtle()

my_turtle.shape("turtle")
n = 10
for i in range(0, 20):
    my_turtle.forward(n)
    my_turtle.left(60)
    n += 10

turtle.done()
