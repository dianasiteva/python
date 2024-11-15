import turtle

my_turtle = turtle.Turtle()

my_turtle.shape("turtle")
n = 10
for i in range(0, 36):
    my_turtle.left(10)
    my_turtle.forward(200)
    my_turtle.left(170)
    my_turtle.forward(200)
    # my_turtle.left(10)
    # my_turtle.forward(200)
    # my_turtle.left(170)
    # my_turtle.forward(200)
    my_turtle.left(10)
    my_turtle.forward(5)

turtle.done()
