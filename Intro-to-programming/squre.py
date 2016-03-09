import turtle

def draw_shapes(n):
    # get a window
    window = turtle.Screen()
    window.bgcolor("orange")

    gucio = turtle.Turtle()
    gucio.shape("turtle")
    gucio.speed(0)
    gucio.color("green")

    for i in range(n):
        for i in range(4):
            gucio.forward(99)
            gucio.right(90)
        gucio.right(360.0 / n)

    # close the window
    window.exitonclick()

draw_shapes(50)
