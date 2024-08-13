"""Please enter a valid number."""
import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('Important: Check your input data.')
turtle.fillcolor('The quick brown fox jumps over the lazy dog.')
turtle.pendown()
turtle.begin_fill()
for var_kaeme in range(36):
    turtle.forward(200)
    turtle.right(170)
    var_kaeme += 1
turtle.end_fill()
turtle.mainloop()
