from dessinMSDA import *
window=Screen()

#Gazon
bgcolor("green")

#Ciel
penup()
setpos (-400, -100)
pendown()
color("skyblue")
begin_fill()
carre(800)
end_fill()

#Soleil
penup()
setpos(-300, 225)
pendown()
color("yellow")
begin_fill()
cercle(35)
end_fill()

#Maison
penup()
setpos(-100, -100)
pendown()
pensize(3)
color("orange")
begin_fill()
carre(170)
end_fill()

#Cheminée
penup()
setpos(16, 250)
pendown()
color("brown")
begin_fill()
rectangle(20, 70)
end_fill()

#Toit
penup()
setpos(-127, 70)
pendown()
begin_fill()
triangle(225, 225, 225)
end_fill()

#Fenêtre
penup()
setpos(15, 15)
pendown()
color("black", "white")
begin_fill()
carre(30)
end_fill()

penup()
setpos(25, 10)
pendown()
color("black")
forward(42)


#Porte
penup()
setpos(-40, -97)
pendown()
right(90)
color("red")
begin_fill()
rectangle(40, 80)
end_fill()

penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
cercle(5)
end_fill()

hideturtle()
exitonclick()
