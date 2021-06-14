from turtle import *
from math import *
from numpy.random import randint
# keith.speed(1)
# def carre(longueur):  
#     window = turtle.Screen()
#     keith = turtle.Turtle()
#     for i in range(4):
#         keith.forward(longueur)
#         keith.left(90)
#     window.exitonclick()

def carre(longueur: float): 
    begin_fill()
    for i in range(4):
        forward(longueur)
        left(90)
    end_fill()
    
def cercle(rayon: float):  
    begin_fill()
    circle(rayon)
    end_fill()
    
def demi_cercle(rayon: float):
    begin_fill()
    circle(rayon, 180)
    end_fill()
        
def polygone(rayon: float, steps: int):
    begin_fill()
    circle(rayon, steps = steps)
    end_fill()
         
def rectangle(longueur: float, largeur: float):
    begin_fill()
    for i in range(2):
        forward(longueur)
        right(90)
        forward(largeur)
        right(90)
    end_fill()
    
def elipse(rayon: float):
    begin_fill()
    for i in range(2):
        circle(rayon, 90)
        circle(rayon//2, 90)
    end_fill()
    
def al_kashi(cote_1, cote_2, cote_3):
    angle = acos((cote_2**2 + cote_1**2 - cote_3**2)/(2*cote_2*cote_1))
    angle2 = acos((cote_3**2 + cote_2**2 - cote_1**2)/(2*cote_3*cote_2))
    angle, angle2 = degrees(angle), degrees(angle2)
    return angle, angle2
    
def triangle(cote_1: float, cote_2: float, cote_3: float, up: bool = True):
    angle, angle2 = al_kashi(cote_1, cote_2, cote_3)
    begin_fill()
    if up:
        forward(cote_1); left(180 - angle); forward(cote_2); left(180 - angle2); forward(cote_3)
    else:
        forward(cote_1); right(180 - angle); forward(cote_2); right(180 - angle2); forward(cote_3)
    end_fill()

def losange(cote: float, diag = randint(10, 50)):
    angle, angle2 = al_kashi(diag, cote, cote)
    begin_fill()
    anglep = 180 - angle
    anglep2 = 180 - angle2
    penup(); forward(diag); pendown(); left(anglep); forward(cote); left(anglep2); forward(cote)
    right(angle); stamp(); left(anglep); forward(cote); left(anglep2); forward(cote)
    end_fill()
    
def trapeze(cote_1: float, cote_2: float, cote_3: float = randint(20, 40), angle: float = 90):
    position = pos()
    begin_fill()
    forward(cote_1); left(180 - angle); forward(cote_2); left(angle); forward(cote_3); goto(position) 
    end_fill()
    
def set_move(x, y: float = None):
    penup()
    if(type(x) is tuple or type(x) is list and len(x) == 2):
        goto(x)
    else:
        goto(x, y)
    pendown()
window = Screen()
# keith = turtle.Turtle()
# turtle.home()
# turtle.circle(50)
# turtle.circle(100, 180)
# carre(100)
#-------------------------------
# turtle.home()
# turtle.dot()
# turtle.fd(50); turtle.dot(20, "orange"); turtle.fd(50)
#-------------------------------
# turtle.home()
# turtle.color("blue")
# stampid = turtle.stamp()
# turtle.fd(50)
# turtle.stamp()
# turtle.fillcolor("orange")
# turtle.color("red")
# turtle.left(90)
# turtle.forward(50)
# turtle.clearstamp(stampid)
# print(turtle.position())
#------------------------------
# for i in range(8):
#     turtle.stamp(); turtle.fd(30)

# turtle.clearstamps(2)
# turtle.clearstamps(-2)
# turtle.clearstamps()
#------------------------------
# turtle.home()
# turtle.goto(10, 10)
# print(turtle.towards(0, 0))
#-----------------------------
# print(turtle.pensize())
# turtle.pensize(10)
# turtle.forward(100)
#-------------------------------
# turtle.pen(fillcolor="black", pencolor="red", pensize=20)
# print(sorted(turtle.pen().items()))
# penstate = turtle.pen()
# turtle.color("yellow", "")
# turtle.penup()
# turtle.forward(10)
# print(sorted(turtle.pen().items())[:3])
# turtle.pen(penstate, fillcolor="green")
# print(sorted(turtle.pen().items())[:3])
# turtle.speed("slowest")
# turtle.pendown()
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(10)
# turtle.circle(40, 180)
# turtle.pen(pencolor="orange")
# turtle.right(90)
# turtle.forward(100)
# print(turtle.isdown())
#-------------------------------------
# turtle.fillcolor("violet")
# print(turtle.fillcolor())
# print(turtle.pencolor())
# # turtle.fillcolor(50, 193, 143)
# # print(turtle.fillcolor())
# turtle.fillcolor('#000000')
# print(turtle.fillcolor())
# turtle.pensize(20)
# # turtle.pencolor("white")
# turtle.color("red", "green")
# turtle.forward(100)
#-----------------------------------
# turtle.begin_fill()
# if turtle.filling():
#     turtle.pensize(5)
# else:
#     turtle.pensize(3)
# turtle.forward(40)
#------------------------------------

