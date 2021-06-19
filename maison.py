from dessinMSDA import *
def maison():
    """Cette fonction a pour but de construire avec le paysage l'avoisinant
    """
    #Initialisation de la fenetre 
    window = Screen()
    #Initialisation de taille de la fenetre
    window.setup(700, 700)
    #On fait disparaitre le curseur
    hideturtle()
    
    #Initialisation des longueurs des cotes du toit dans une liste et sa couleur
    longueurstoit = [250, 150, 150]
    couleurtoit = "chocolate"
    
    #Initialisation de la longueur et de la largeur de la cheminé
    longueurcheminé = [longueurstoit[0] / 10, 40]
    
    #Initialisation de la longueur du cadre de la maison et sa couleur
    longueurcadre = longueurstoit[0] * 6 / 8
    couleurcadre = "orange"
    
    #Inilisation de la longueur et de la largeur de la porte de la maison dans une liste
    # et de sa couleur
    longueursporte = [longueurcadre / 4, longueurcadre / 3]
    couleurporte = "peru"
    
    #Initialisation de la longueur d'une case de la fenetre et la couleur du crayon
    longueurpc = longueurcadre / 10
    couleurpc = "black"
    
    #Initialisation de la longueur et de la largeur du bas de la maison et de sa couleur de 
    # remplissage
    longueurbascadre = [longueurcadre, longueurcadre / 18]
    couleurbascadre = "black"
    
    #Initialisation de la longueur de la largeur de la marche pres de la porte de la maison
    # et de sa couleur de contour
    longueurmarche = [longueursporte[0] + 19, longueurbascadre[1]]
    couleurmarche = "black"
    
    #Conception du gazon (espace en vert)
    set_move(- window_width()/2, pos()[1])
    penup()
    fillcolor("green")
    begin_fill(); rectangle(window_width(), window_height()/2 + 60); end_fill()
    pendown()
    
    #Conception du ciel (espace en bleu ciel)
    set_move(- window_width()/2, window_height()/2)
    penup()
    fillcolor("skyblue")
    begin_fill(); rectangle(window_width(), window_height()/2); end_fill()
    pendown()
    
    #Conception du soleil (cercle jaune)
    set_move(- (window_width() * 4)/12, (window_height() * 4)/12)
    penup()
    fillcolor("yellow")
    begin_fill(); cercle(30); end_fill()
    pendown
    
    #Conception du toit et stockage de la position du curseur apres tracage
    set_move( - longueurstoit[0] / 2, window_height() / 4)
    pencolor("black")
    fillcolor(couleurtoit)
    begin_fill(); triangle(longueurstoit[0], longueurstoit[1], longueurstoit[2]); end_fill()
    positiontoit = position()
    
    #Conception de la cheminé
    set_move(pos()[0] + (longueurstoit[0] * 4)/6, pos()[1] + 70)
    setheading(0)
    begin_fill(); rectangle(longueurcheminé[0], longueurcheminé[1]); end_fill()
    
    #Conception du cadre de la maison et stockage de la position du curseur apres tracage
    set_move(positiontoit[0] + longueurstoit[0]/8, positiontoit[1] - longueurcadre)
    pencolor("darkorange")
    fillcolor(couleurcadre)
    setheading(0)
    begin_fill(); carre(longueurcadre); end_fill()
    positioncadre = position()
    #On retrace avec le crayon noir le bas du toit
    set_move(positiontoit[0], positiontoit[1]); pencolor("black"); forward(longueurstoit[0])
    
    #Conception de la porte et stockage de la position du curseur apres tracage
    set_move(positioncadre[0] + longueurcadre/8, positioncadre[1] + longueursporte[1])
    pencolor("saddlebrown")
    fillcolor(couleurporte)
    setheading(0)
    begin_fill(); rectangle(longueursporte[0], longueursporte[1]); end_fill()
    positionporte = pos()
    
    #Conception de la fenetre au bas-droite et stockage de la position du curseur apres tracage
    set_move(positioncadre[0] + (longueurcadre * 5)/8, positioncadre[1] + longueursporte[1] - longueurpc)
    pencolor(couleurpc)
    setheading(0)
    positionpc1 = carres(longueurpc)
    
    #Conception de la fenetre a gauche 
    set_move(positionporte[0] + longueursporte[0]/6, positionporte[1] + (longueurcadre * 3)/8)
    setheading(0)
    carres(longueurpc)
    
    #Conception de la fenetre en haut a droite
    set_move(positionpc1[0], positionporte[1] + (longueurcadre * 3)/8)
    setheading(0)
    carres(longueurpc)
    
    #Faisons un point pour indiquer le poignet de la porte
    set_move(positionporte[0] + longueursporte[0]/8, positionporte[1] - longueursporte[1]/1.75)
    fillcolor("brown")
    dot(5)
    
    #A present on s'occupe du bas de la maison
    #Conception du bas de la maison en noir
    set_move(positioncadre[0], positioncadre[1])
    fillcolor(couleurbascadre)
    begin_fill(); rectangle(longueurbascadre[0], longueurbascadre[1]); end_fill()
    
    #Conception de la marche pres de la porte
    set_move(positionporte[0] - 9, positionporte[1] - longueursporte[1])
    fillcolor("lightcyan")
    pencolor(couleurmarche)
    begin_fill(); rectangle(longueurmarche[0], longueurmarche[1]); end_fill()
    positionmarche = (pos()[0], pos()[1] - longueurmarche[1])
    
    #La maison est terminée mais on va continuer enfin de rendre plus jolie le paysage
    #qui l'entoure
    #On fait d'abord un passage orange par lequel on entre dans la maison
    fillcolor("orange")
    set_move(positionmarche[0] + longueurmarche[0]/2, positionmarche[1])
    positionalle = position()
    begin_fill()
    setheading(270)
    setpos(pos()[0], pos()[1] - 90)
    right(90); forward(80);
    positionrightall = position()
    setpos(positionmarche)
    setpos(positionmarche[0] + longueurmarche[0]/2, pos()[1])
    setpos(positionalle)
    end_fill()
    begin_fill()
    setheading(270)
    set_move(pos()[0], pos()[1] - 90)
    left(90); forward(80);
    positionleftall = position()
    setpos(positionmarche[0] + longueurmarche[0], positionmarche[1])
    setpos(positionmarche[0] + longueurmarche[0]/2, pos()[1])
    setpos(positionalle)
    end_fill()
    
    #Puis on trace les bords de la route en marron
    pensize(6)
    pencolor("brown")
    set_move(positionrightall)
    setheading(180)
    setpos(- window_width()/2, pos()[1])
    #Stockage de la position du coin gauche du bord d'en haut
    positiontopright = position()
    set_move(positionleftall)
    setheading(0)
    setpos(window_width()/2, pos()[1])
    #Maintenant on stocke le cote droit
    positiontopleft = position()
    
    #Avant de remplir la couleur de fond
    #On augmente la taille du crayon qui etait de 6 pxl (question de perception)
    #Puis on trace le bord du bas
    pensize(8)
    set_move(positiontopright[0], positiontopright[1] - 70)
    
    #Enfin on passe a la conception de la route elle meme en utilisant les positions 
    #prealablement stockées
    fillcolor("steelblue")
    begin_fill()
    setpos(positiontopleft[0], positiontopleft[1] - 70)
    set_move(positiontopleft)
    set_move(positiontopright)
    set_move(positiontopright[0], positiontopright[1] - 70)
    end_fill()
    set_move(positiontopright[0], positiontopleft[1] - 26)
    pencolor("white")
    pensize(3)
    setheading(0)
    #On trace par ici les traits blancs au milieu de la route en eloignant un peu par rapport au
    #milieu (question de perception)
    for i in range(35):
        forward(10)
        penup()
        forward(10)
        pendown()
        
    #Quitter la fenetre au clic
    window.exitonclick()

def carres(longueurpc):
    """Cette fonction permet de concevoir les fenetres de la maison
    """
    #Boucle qui trace successivement chaque case de la fenetre avec des couleurs de fond differents
    #pour les cotes du haut et du bas de chaque fenetre
    for i in range(2):
        if (i == 0):
            fillcolor("lightblue")
            positionpc1 = pos()
        if (i == 1):
            fillcolor("powderblue")
            set_move(positionpc1[0], positionpc1[1] - longueurpc)
            setheading(0)
        begin_fill()
        carre(longueurpc)
        end_fill()
        set_move(pos()[0] + longueurpc, pos()[1])
        begin_fill()
        carre(longueurpc)
        end_fill()
    #On retourne la position retenue de la premiere case avant de la tracer
    return positionpc1
        
    
    
            
            
