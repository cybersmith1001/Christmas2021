from turtle import *
import turtle

number_of_shapes = 4

pendown()

for shape in range(1, number_of_shapes + 1):
        for sides in range(1, 4):      
                forward(10 + shape * 20)
                left(120)                              
                
        penup()
        left(90)
        back(15 + shape * 10)
        right(90)
        back(10)
        pendown()

penup()
goto (0,0)
forward(10)
right(90)
forward(100)
right(90)
forward(10)
pendown()

for sides in range(1, 5):
        back(30)
        right(90)

penup()
left(90)
forward(30)
left(90)
pendown()
forward(100)
left(180)
forward(180)

penup()
goto (0,0)
back(15)
right(90)
forward(30)
pendown()

for sides in range(1, 13):
        forward(10)
        penup()
        back(10)
        right(30)
        pendown()

penup()
right(180)
forward(200)
right(90)
forward(100)

pendown()
turtle.write('MERRY CHRISTMAS & HAPPY NEW YEAR')


penup()
right(90)
back(100)

pendown()

number_of_squares = 2

for shape in range (1, number_of_squares + 1):
    for sides in range(1, 5):
        forward(60)
        right(90)

    penup()       
    goto(50, -270)
    pendown()    

penup()
right(90)
forward(30)
left(90)
pendown()
forward(60)
penup()
back(30)
left(90)
pendown()
forward(30)
left(180)
penup()
forward(30)
pendown()
forward(30)
penup()
back(30)
left(90)
forward(30)

pendown()
for shape in range(1):
        for sides in range(1, 4):
                forward(10)
                left(120)

for shape in range(1):
        for sides in range(1, 4):
                forward(10)
                right(120)

penup()
left(90)
forward(135)
right(90)

pendown()
for shape in range(1):
        for sides in range(1, 4):
                forward(10)
                left(120)

for shape in range(1):
        for sides in range(1, 4):
                forward(10)
                right(120)

back(60)
penup()
forward(30)
right(90)
pendown()
forward(30)
penup()
back(30)
pendown()
back(30)

penup()
goto(110, 50)

pendown()

number_of_spikes = 8

for shape in range(1, number_of_spikes + 1):
    for side in range(1, 4):
        forward(20)
        goto(110, 50)
        left(66)

hideturtle()
