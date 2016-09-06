import turtle

def draw_square(turt):
    for h in range(0,4):
        turt.forward(100)
        turt.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")

    bob = turtle.Turtle()
    bob.hideturtle()
    bob.color("yellow")
    bob.speed(8)

    for a in range(1,37):
        draw_square(bob)
        bob.right(10)

    print("done")
    window.exitonclick()


draw_shapes()
  
