import turtle

def draw_triangle(turt,length,counter):
    if(counter<3):
        for h in range(0,3):
            turt.forward(length)
            turt.right(120)
            draw_triangle(turt,length/2,counter+1)
            
        

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")

    bob = turtle.Turtle()
   # bob.hideturtle()
    bob.color("yellow")
    bob.speed(5)
    bob.right(60)

    length = 300

    draw_triangle(bob,length,0,)

    print("done")
    window.exitonclick()


draw_shapes()
