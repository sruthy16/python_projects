Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.showturtle()
>>> turtle.forward(200)
>>> turtle.right(90)
>>> turtle.forward(200)
>>> turtle.setheading(120)
>>> turtle.heading()
120.0
>>> turtle.penup()
>>> turtle.forward(45)
>>> turtle.drawcircle(120)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    turtle.drawcircle(120)
AttributeError: module 'turtle' has no attribute 'drawcircle'
>>> turtle.circle(120)
>>> turtle.pendown()
>>> turtle.circle(123)
>>> turtle.penup()
>>> turtle.forward(200)
>>> turtle.dot()
>>> turtle.pensize(20)
>>> turtle.pendown()
>>> turtle.forward(34)
>>> turtle.pencolor('blue')
>>> turtle.forward(300)
>>> turtle.bgcolor('yellow')
>>> turtle.clear()
>>> turtle.setup(500,500)
>>> turtle.goto(50,40)
>>> turtle.setup(500,500)
>>> turtle.pos
<function pos at 0x000001157E97F550>
>>> turtturtle.forward(200)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    turtturtle.forward(200)
NameError: name 'turtturtle' is not defined
>>> turtle.pos()
(50.00,40.00)
>>> turtle.write('Hello There!')
>>> turtle.begin_fill('green')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    turtle.begin_fill('green')
TypeError: begin_fill() takes 0 positional arguments but 1 was given
>>> turtle.begin_fill()
>>> turtle.circle(50)
>>> turtle.end_fill()
>>> 