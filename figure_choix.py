# Nous allons construire ici une fonction nous permettant de dessiner une figure de notre choix
# 
# Importons le module contenant les fonctions pour tracer les figures
from dessinMSDA import *
def figure_choix():
    """Cette fonction permet de tracer notre figure de choix 
    Tracer une fleur avec une image de arriere plan derriere
    """
    #Configuration de la fenetre
    window = Screen()
    window.setup(600, 600)
    #Mise en place de l'image de l'arriere plan
    window.bgpic("water_original.gif")
    window.bgcolor("lightblue")
    #Vitesse d'execution rapide
    speed("fast")
    
    #Tracer de telles fleurs demande un certain d'ajustements et 
    #de calculs geometriques faits au prealable
    #On commence d'abord avec la fleur verte derriere
    #On trace avec l'aide des demi-cercles
    pencolor("darkgreen")
    fillcolor("green")
    hideturtle()
    set_move(pos()[0] - 65, pos()[1] - 130) 
    penup()
    for i in range(10):
        begin_fill(); demi_cercle(90); end_fill()
        setheading(heading()+72)
    pendown()
    for i in range(10):
        demi_cercle(90)
        setheading(heading()+72)
        
    #Puis on passe a la fleur violete juste devant la fleur verte
    #Meme methode qu'avec la fleur verte
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
    
    #En fin on passe a la fleur blanche blanche au contours jaunes qui va former le bouquet
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
    #On place un point bleu clair au milieu de la fleur blanche au contours jaunes
    color("lightblue")
    set_move(pos()[0] - 19.5, pos()[1] + 44.5) 
    dot(20)
    
    #Quitter la fenetre au clic
    window.exitonclick()
