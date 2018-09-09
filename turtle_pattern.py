    from turtle import *
    from random import randint
     
     
    bgcolor('black')
    x = 1
    tracer(0, 0)
    while x < 500:
     
     a = randint(0,255)
     b = randint(0,255) 
     c = randint(0,255)
     
     colormode(255) 
     pencolor(a,b,c)
     fd(45 + x)
     rt(92)
     x = x+1
     exitonclick()
