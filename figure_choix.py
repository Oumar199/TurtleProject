# Nous allons construire ici une fonction nous permettant de dessiner une figure de notre choix
# 
# Importons le module contenant les fonctions pour tracer les figures
from dessinMSDA import *
def figure_choix():
    window = Screen()
    window.setup(600, 600)
#     window.addshape("water-2634082_1920.jpg")
    window.bgpic("water_original.gif")
    window.bgcolor("lightblue")
    speed("fast")
    pencolor("darkgreen")
    fillcolor("green")
    hideturtle()
#     setheading(0)
#     penup()
    set_move(pos()[0] - 65, pos()[1] - 130) 
    penup()
    for i in range(10):
        begin_fill(); demi_cercle(90); end_fill()
        setheading(heading()+72)
    pendown()
    for i in range(10):
        demi_cercle(90)
        setheading(heading()+72)
    pencolor("darkviolet")
    fillcolor("violet")
    set_move(pos()[0] + 97, pos()[1] + 19) 
    setheading(heading()+60)
    penup()
    for i in range(10):
        begin_fill(); demi_cercle(60); end_fill()
        setheading(heading()+72)
    pendown()
    for i in range(10):
        demi_cercle(60)
        setheading(heading()+72)
    set_move(pos()[0] - 10, pos()[1] + 20) 
    pencolor("yellow")
    fillcolor("lightyellow")
    pensize(2)
    penup()
    for i in range(10):
        begin_fill(); demi_cercle(40); end_fill()
        setheading(heading()+72)
    pendown()
    for i in range(10):
        demi_cercle(40);
        setheading(heading()+72)
    color("lightblue")
    set_move(pos()[0] - 19.5, pos()[1] + 44.5) 
    dot(20)
    window.exitonclick()