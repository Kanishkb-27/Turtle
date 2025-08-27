import turtle
#creating canvas
turtle.Screen().bgcolor("orange")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Turtle Window")
x=turtle.Turtle()
for i in range(4):
    x.forward(100)
    x.left(90)
    i=i+1
turtle.done()