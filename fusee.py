#Nous allons créer ici une fonction permettant de tracer notre fusée :))
from dessinMSDA import *
def fusee():
    """Cette fonction permet de construire une fusee
    """
    #Configuration de la fenetre et de la vitesse d'execution
    window = Screen()
    hideturtle()
    window.setup(600, 600)
    window.bgcolor("black")
    pencolor("white")
    speed("normal")
    
    #On va utiliser un dictionnaires pour stocker les positions (simple precaution)
    positions = {}
    #Tracons le premier triangle et stockons sa position pour pouvoir l'utiliser plus tard
    #Les longueurs des figures seront stockees dans des variables 
    ltri1 = 66
    set_move(pos()[0] - 33, pos()[1] + 200)
    positions["tri1"] = pos()
    fillcolor("red"); begin_fill(); triangle(ltri1, ltri1, ltri1); end_fill()
    setheading(0)
    
    #On reprend la position de depart pour tracer un carre rouge au milieu du triangle et on stocke sa position (position du 
    #curseur plus precisement)
    set_move(positions["tri1"][0] + 18, positions["tri1"][1])
    lcar1 = (ltri1 - 6) / 2
    fillcolor("red"); begin_fill(); carre(lcar1); end_fill()
    positions["carre1"] = pos()
    
    #Tracons un carre juste en dessous du premier carre apres avoir defini une position du curseur suivant la position
    #retenue du carre precedent
    lcar2 = ltri1 - 8*2
    set_move(positions["tri1"][0] + 8, positions["tri1"][1] - lcar2) 
    setheading(0)
    #On utilisera la methode du fillcolor(remplir couleur);begin_fill(commencer le remplissage)
    #fonction(la fonction nous permettant de tracer une figure); end_fill(finir le remplissage)
    #pour tracer toutes les figures de cette fonction
    fillcolor("lightgreen"); begin_fill(); carre(lcar2); end_fill()
    #On stocke egalement cette position
    positions["carre2"] = pos()
    # Le triangle suivant comporte un côté de longueur egale a car2, un autre de longueur egale a car2/2 et un autre de longueur inconnue
    # calculons cette longueur avec le theoreme de al-kachi (Ce theoreme nous servira tout au long du programme)
    lcote1_t2 = lcar2
    lcote2_t2 = lcar2/2
    lcote3_t2 = origin_al_kachi(lcote1_t2, lcote2_t2, 90) #car l'angle gauche fait 90 degrés
    #On trace a present un triangle de chaque cote du carre bleu clair
    set_move(pos()[0] + lcar2, pos()[1])
    fillcolor("green"); begin_fill(); triangle(lcote2_t2, lcote3_t2, lcote1_t2); end_fill() 
    set_move(positions["carre2"][0] - lcote2_t2, positions["carre2"][1])
    setheading(0)
    fillcolor("green"); begin_fill(); triangle(lcote2_t2, lcote1_t2, lcote3_t2); end_fill() 
    
    #On passe maintenant au premier rectangle
    #specifications de la longueur et de la largeur du rectangle
    lrec1 = lcar2 * 2
    Lrec1 = 20
    # A preciser qu'a chaque fois qu'on souhaite avoir un angle bien precis 
    # on va utiliser la fonction setheading(angle). 
    setheading(0)
    #Tracons le rectangle et recuperons sa position plus tard
    fillcolor("lightblue"); begin_fill(); rectangle(lrec1, Lrec1); end_fill() 
    positions["rec1"] = pos()
    lcote1_rc1 = Lrec1 
    lcote2_rc1 = Lrec1/2
    lcote3_rc1 = origin_al_kachi(lcote1_rc1, lcote2_rc1, 90) #car l'angle gauche fait 90 degrés
    #Apres cela on utilise les methodes qui nous ont permis de tracer les triangles du deuxieme carre pour tracer ceux du premier 
    # rectangle (ceux de ses cotes du moins)
    set_move(pos()[0] + lrec1, pos()[1] - Lrec1)
    setheading(0)
    lcote2_rc1 += 14
    lcote3_rc1 += 9
    fillcolor("grey"); begin_fill(); triangle(lcote2_rc1, lcote3_rc1, lcote1_rc1); end_fill() 
    positions["tri2"] = pos()
    set_move(positions["rec1"][0] - lcote2_rc1, positions["rec1"][1] - Lrec1)
    setheading(0)
    fillcolor("grey"); begin_fill(); triangle(lcote2_rc1, lcote1_rc1, lcote3_rc1); end_fill()
    
    #Apres avoir tracer les triangles on souhaite tracer un carre en dessous de chaque triangle. Ils seront de couleur gris
    set_move(pos()[0], pos()[1] - lcote2_rc1)
    setheading(0)
    fillcolor("grey"); begin_fill(); carre(lcote2_rc1); end_fill()
    set_move(positions["tri2"][0], positions["tri2"][1] - lcote2_rc1)
    setheading(0)
    fillcolor("grey"); begin_fill(); carre(lcote2_rc1); end_fill()
    positions["carre3"] = pos() # recuperation de la position du dernier carre
    
    #On trace un rectangle, a cote des carres, de couleur bleu foncé (on souhaite que avoir l'impression
    # d'avoir des ombres sur la fusee
    set_move(positions["rec1"][0], positions["rec1"][1] - Lrec1)
    setheading(0)
    fillcolor("darkblue"); begin_fill(); rectangle(lrec1, lcote2_rc1); end_fill() 
    positions["rec2"] = pos()
    
    #La fonction set_move() sera utilisé a plusieurs reprises et semble d'ailleur etre l'une des fonctions les plus utiles
    #de ce projet
    set_move(pos()[0] - lcote2_rc1, pos()[1] - lcote2_rc1)
    #On trace deux rectangles de couleur orange pour indiquer les flammes sortant de la fusee
    lcote1_fire = lcote2_rc1
    lcote2_fire = 40
    lcote3_fire = 43
    setheading(0)
    fillcolor("orange"); begin_fill(); triangle(lcote1_fire, lcote2_fire, lcote3_fire, False); end_fill()
    set_move(positions["carre3"][0], positions["carre3"][1])
    setheading(0)
    fillcolor("orange"); begin_fill(); triangle(lcote1_fire, lcote3_fire, lcote2_fire, False); end_fill()
    
    #On place a present un carre au milieu du deuxieme rectangle
    lcar3 = lrec1/3
    set_move(positions["rec2"][0] + lcar3, positions["rec2"][1] - lcote2_rc1 - lcar3)
    setheading(0)
    fillcolor("brown"); begin_fill(); carre(lcar3); end_fill()
    positions["carre4"] = pos()
    
    #On place un cercle de chaque cote du carre, de couleur jaune
    ray1 = 12
    set_move(pos()[0] - lcar3/2 - 6, pos()[1] + 4)
    setheading(0)
    fillcolor("yellow"); begin_fill(); cercle(ray1); end_fill()
    set_move(positions["carre4"][0] + lcar3 * 1.5 + 6, positions["carre4"][1] + 4)
    setheading(0)
    fillcolor("yellow"); begin_fill(); cercle(ray1); end_fill()
    
    #On place un rectangle en dessous carre, de couleur violet sombre
    lrec2 = lcar3 * 2
    set_move(positions["carre4"][0] - lcar3/2, positions["carre4"][1])
    setheading(0)
    fillcolor("violet"); begin_fill(); rectangle(lrec2, lcote2_rc1); end_fill() 
    lcar4 = lrec2/5
    set_move(pos()[0] + lcar4*2, pos()[1] - lcote2_rc1 - lcar4)
    setheading(0)
    fillcolor("darkviolet"); begin_fill(); carre(lcar4); end_fill()
    positions["carre5"] = pos()
    
    #On dessine de petites cercles de part et d'autre du dernier carre, de 
    #couleur violet sombre
    ray2 = 3
    set_move(pos()[0] - lcar4, pos()[1])
    fillcolor("darkviolet"); begin_fill(); cercle(ray2); end_fill()
    set_move(positions["carre5"][0] + lcar4*2, positions["carre5"][1]) 
    fillcolor("darkviolet"); begin_fill(); cercle(ray2); end_fill()
    
    #Et enfin on termine avec un rectangle en dessous du dernier carre avec des triangles
    # tracés avec la fameuse methode d'al-kachi
    lrec3 = lcar4
    Lrec3 = 40
    set_move(positions["carre5"][0], positions["carre5"][1])
    setheading(0)
    fillcolor("darkviolet"); begin_fill(); rectangle(lrec3, Lrec3); end_fill() 
    positions["rec3"] = pos()
    lcote1_rc3 = Lrec3 
    lcote2_rc3 = Lrec3/2
    lcote3_rc3 = origin_al_kachi(lcote1_rc3, lcote2_rc3, 90) #car l'angle gauche fait 90 degrés
    set_move(pos()[0] + lrec3, pos()[1] - Lrec3)
    fillcolor("violet"); begin_fill(); triangle(lcote2_rc3, lcote3_rc3, lcote1_rc3); end_fill() 
    set_move(positions["rec3"][0] - lcote2_rc3, positions["rec3"][1] - Lrec3)
    setheading(0)
    fillcolor("violet"); begin_fill(); triangle(lcote2_rc3, lcote1_rc3, lcote3_rc3); end_fill() 
    
    #Quitter la fenetre au clic
    window.exitonclick()



def origin_al_kachi(lcote1: float, lcote2: float, degres: float):
    """Cette fonction nous permet de calculer la longueur inconnue d'un cote du triangle en connaissant 
    la mesure de l'angle qui lui est opposé
    """
    return sqrt(lcote2**2 + lcote1**2 - 2*lcote2*lcote1*cos(radians(degres))) 
