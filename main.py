from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red", "green")
my_turtle.fd(100)
my_turtle.lt(90)
my_turtle.fd(100)
my_turtle.lt(90)
my_turtle.fd(100)
my_turtle.lt(90)
my_turtle.fd(100)
my_turtle.lt(90)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
print(my_screen.exitonclick())