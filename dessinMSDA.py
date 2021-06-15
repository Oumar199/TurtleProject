# Importation des bibliotheques qui nous serviront dans ce module

# Importons les fonctions de la librairie turtle pour les figures
from turtle import *

# Importons les fonctions mathematiques
from math import *

# Importons la fonction random.randint de numpy 
from numpy.random import randint as rdt

# Nous allons créer pour chaque type de figure simple (triangle, rectangle, carre, cercle, ...) 
# une fonction (ou procédure) qui comportera les manipulation permettant de tracer la figure

# Mais d'abord creons quelques fonctions tres utiles au programme
def set_move(x, y: float = None):
    """Cette fonction permet au turtle de quitter un endroit pour aller dans un autre sans être 
    Visible
    Method:
        Utilisation de la fonction penup() et pendown() pour lever le crayon et ne rien tracer
        et utiliser la fonction goto() pour aller vers un endroit selon les coordonnées x et y
    Args:
        x(float ou tuple ou list): si c'est une liste ou un tuple goto la prendra seule comme para-
        -mètre sinon goto prendra avec elle un deuxième paramètre de type float
        y(float): le deuxième paramètre de goto si x n'est pas un tuple ou une liste
    Returns: 
        None
    """
    penup()
    if (type(x) is tuple or
        type(x) is list and
        len(x) == 2):
        
        goto(x)
    
    else:
        goto(x, y)
    
    pendown()

def al_kashi(
    cote_1: float,
    cote_2: float,
    cote_3: float):
    """Cette fonction permet de calculer deux angles du triangle à partir de la longueur des cotés
    Cette méthode provient du théorème géométrique d'Al-Kashi pour calculer les côtés du triangle
    quelconque
    Method:
        Utilisation de la formule: angle = arccos((coté_gauche^2 + coté_droit^2 - coté_oppose^2)/
        (2*coté_droit*coté_gauche)
        et conversion des angles obtenus en degrés
    Args:
        cote_1(float): La base du triangle
        cote_2(float): le coté droit du triangle
        cote_3(float): le coté gauche du triangle
    Returns:
        angle(float): l'angle droit du triangle en radians
        angle2(float): l'angle opposé à la base du triangle en radians
    """
    angle = acos((cote_2**2 + cote_1**2 - cote_3**2)/(2*cote_2*cote_1))
    angle2 = acos((cote_3**2 + cote_2**2 - cote_1**2)/(2*cote_3*cote_2))
    return degrees(angle), degrees(angle2)

# On implemente les fonctions permettant de créer les figures simples
def carre(cote: float):
    """Cette fonction nous permet de tracer une carre
    Method:
        On utilise la boucle for pour répéter les fonctions forward et left(90 degrés). Ce qui nous
        permet de tracer les quatre côtés du carre d'égales longueurs
    Args:
        cote(float): La longueur de chaque cote du carre. Cette longueur ne doit être inferieure ou
        égale a 0
    Returns:
        None
    """
    if cote > 0:
        for i in range(4):
            forward(cote)
            left(90)
    else:
        raise ValueError("La longueur du coté ne peut être inférieure ou égale à zero")
        

def rectangle(
    longueur: float,
    largeur: float):
    """Cette fonction permet de tracer un rectangle 
    Method:
        On utilise la boucle for permettant de répéter deux fois les instructions forward à longueur, right(90 degrés),
        forward à largeur, right (90 degrés). Cela nous permet de tracer deux fois la longueur et la largeur du rectangle
        pour le créer (calcul du périmètre)
    Args:
        longueur(float): la longueur du rectangle qui ne doit pas être inferieure ou égale a 0
        largeur(float): la largeur du rectangle qui ne doit pas non plus être inferieure ou égale a 0
    Returns:
        None
    """
    if (longueur > 0  and
            largeur > 0):
        for i in range(2):
            forward(longueur)
            right(90)
            forward(largeur)
            right(90)
    else:
        raise ValueError("La longueur et la largeur ne doivent pas être inferieures ou egales a 0")


def cercle(rayon: float):
    """Cette fonction permet de tracer un cercle
    Method:
        On utilise la fonction circle de turtle. On indique uniquement le rayon
    Args:
        rayon(float): le rayon du cercle qui doit être supérieur à 0
    Returns:
        None
    """
    if rayon > 0:
        circle(rayon)        
    else:
        raise ValueError("La longueur du rayon ne peut être inférieure ou égale à 0")

def ellipse(rayon: float):
    """Cette fonction permet de tracer une ellipse
    Method:
        On utilise la boucle for pour répéter deux fois les commandes tracer un quart de cercle de rayon donné en para-
        -mètre et un quart de cercle de rayon de longueur faisant la partie entière de la longueur du rayon en paramètre 
        divisée par deux. Ces tracées de quart de cercle se feront à l'aide de la fonction circle de turtle
    Args:
        rayon(float): la longueur du rayon utilisé deux fois pour tracer le quart du cercle. La longueur du rayon doit être
        supérieure a 2 pour éviter que la partie entière de la longueur du rayon divisée par deux soit égale 0
    Returns:
        None
    """
    if rayon > 2:
        for i in range(2):
            circle(rayon, 90)
            circle(rayon//2, 90)
    else:
        raise ValueError("La longueur du rayon ne doit pas être inférieure ou égale à deux pour éviter que la partie entière de la division par deux du rayon soit égale à 0")
    
def demi_cercle(rayon: float):
    """Cette fonction permet de tracer un demi-cercle
    Method:
        On utilise la fonction circle de turtle. On indique le rayon donné en paramètre et un angle de 180 degrés
        correspondant à l'étendu du cercle
    Args:
        rayon(float): le rayon du cercle qui doit être supérieur à 0
    Returns:
        None
    """
    if rayon > 0:
        circle(rayon, 180)        
    else:
        raise ValueError("La longueur du rayon ne peut être inférieure ou égale à 0")

def triangle(
    cote_1: float, cote_2: float,
    cote_3: float, up: bool = True):
    """Cette fonction permet de tracer un triangle quelconque
    Method:
        On récupère l'angle droit et l'angle a l'opposé de la base à l'aide de la fonction d'Al-Kachi. On vérifie ensuite si le
        paramètre "up" indique True ou False pour savoir si l'on doit utiliser la fonction left oubien la fonction right pour 
        tourner la tortue. 
        Dans les deux cas on va suivre ce procédé :
        Tracer le premier coté du triangle avec forward(cote_1), puis tourner a (180 - angle) (angle droit du triangle);
        On trace le deuxième coté avec forward(cote_2), puis tourner a 180 - angle2 (angle a l'oppose de la base) et enfin
        On trace le troisième côté avec forward(cote_3).
    Args:
        cote_1(float): la longueur de la base du triangle qui doit être supérieure a 0 et inferieure a la somme des deux autres côtés
        du triangle
        cote_2(float): la longueur du cote droit du triangle qui doit être supérieure a 0 et inferieure a la somme des deux autres côtés
        cote_3(float): la longueur du cote gauche du triangle qui doit être supérieure a 0 et inferieure a la somme des deux autres
        côtés
        up(bool): la valeur booléenne qui doit indiquer si le sommet du triangle pointe vers le côté supérieur de la base ou vers 
        son côté inferieur. Si elle n'est pas indiquée alors elle prendra par defaut la valeur True
    Returns: 
        None
    """
    if (cote_1 > 0 and
       cote_2 > 0 and
       cote_3 > 0 and
       cote_1 < (cote_2 + cote_3) and
       cote_2 < (cote_1 + cote_3) and
       cote_3 < (cote_1 + cote_2)):
        
        angle, angle2 = al_kashi(cote_1, cote_2, cote_3)
        forward(cote_1)
        if up:
            left(180 - angle); forward(cote_2); left(180 - angle2)
        else:
            right(180 - angle); forward(cote_2); right(180 - angle2)
        forward(cote_3)
    elif (cote_1 >= (cote_2 + cote_3) or
         cote_2 >= (cote_1 + cote_3) or
         cote_3 >= (cote_1 + cote_2)):
        
        raise ValueError("Aucun des cotés du triangle ne doit avoir une longueur plus importante que la somme des longueurs des deux autres")
    
    else:
        raise ValueError("Aucun des cotés du triangle ne doit avoir une longueur inférieure ou égale à 0")

def losange(cote: float, diag = rdt(10, 50)):
    """Cette fonction permet de tracer un losange
    Method:
        On a décider de tracer deux triangles de base commune (la diagonale indiquée en paramètre
        Utiliser la fonction d'Al-Kachi pour trouver les angles de chaque triangle
        Pour concevoir les deux triangles on va tourner a 180 - angle degrés (angle droit de chaque triangle), avancer avec
        forward(cote), tourner a 180 - angle2 degrés (angle à l'opposé du diagonale du losange) et avancer avec forward(cote)
        Les différences résident aux points suivant pour chaque triangle :
        - triangle 1: on lève le crayon avec penpup(), on avance avec forward(diag) et on remet le crayon en place (pendown())
        - triangle 2: on tourne a "angle" degrés à droite
    Args:
        cote(float): la longueur de chaque côté du losange qui doit être positive
        diag(flaot ou int): la longueur de la diagonale du losange qui doit être positive. Si elle n'est pas donnée alors elle
        prend une valeur entière comprise entre 10 et 50
    Returns:
        None
    """
    if (cote > 0 and
        diag > 0 and
        diag < cote*2):
        
        angle, angle2 = al_kashi(diag, cote, cote)
        anglep = 180 - angle
        anglep2 = 180 - angle2
        penup(); forward(diag); pendown(); left(anglep); forward(cote); left(anglep2); forward(cote)
        right(angle); left(anglep); forward(cote); left(anglep2); forward(cote)
    
    elif (diag >= cote * 2):
        raise ValueError("La longueur de la diagonale ne doit pas être supérieure ou égale à la somme des longueurs de deux cotés")
        
    else:
        raise ValueError("Les longueurs du coté et de la diagonale ne doivent pas être inférieures ou égales à 0")
        
def trapeze(cote_1: float, cote_2: float, cote_3 = rdt(20, 40), angle: float = 90, up: bool = True):
    """Cette fonction permet de tracer un trapèze
    Method:
        On stocke dans une variable la position du curseur ou de la tortue ((x, y): tuple)
        Si "up" est à True, on utilise la fonction left(angle en degrés) pour tourner la tortue
        sinon on utilise right(angle en degrés) pour la tourner
        On avance avec forward(longueur base du trapèze), on tourne a 180 - angle (angle droit du trapèze) degrés, on avance 
        avec forward(longueur côté droit du trapèze), on tourne à angle (angle droit du trapèze) degrés pour ensuite avancer avec                   forward(longueur côté parallèle a la base) pour enfin avancer le crayon jusqu'à la position initiale avec goto(position ini-
        -tiale)
    Args:
        cote_1(float): la longueur de la base du trapèze qui doit être supérieure a la longueur du côté qui lui est opposé et
        supérieure a 0
        cote_2(float): la longueur du côté du trapèze qui doit être supérieure a 0
        cote_3(float): la longueur du côté opposé à la base qui doit être supérieure a 0 et a la longueur de la base. Si cette longueur
        n'est pas précisée alors sa valeur entière sera comprise entre 20 et 40
        angle(float): angle au bas-droit du trapèze. Sa valeur doit être comprise entre 20 et 160 degrés
        up(bool): la valeur booléenne qui doit indiquer si le côté opposé de la base du trapèze sera conçu vers le côté supérieur de la             base du trapèze ou vers son côté inferieur. S'il n'est pas indiquée alors elle prendra par défaut la valeur True 
    Returns:
        None
    """
    if (cote_1 > cote_3 and
        cote_1 > 0 and
        cote_2 > 0 and
        cote_3 > 0 and
        angle > 20 and
        angle < 160):
        
        position = pos()
        forward(cote_1)
        if up:
            left(180 - angle); forward(cote_2); left(angle);
        else:
            right(180 - angle); forward(cote_2); right(angle);
        forward(cote_3); goto(position)
    
    elif (cote_1 <= cote_3):
        raise ValueError("La longueur de la base doit être supérieure à la longueur du côté qui lui est opposé")
        
    elif (angle <= 20 or
          angle >= 160):
        
        raise ValueError("La valeur de l'angle au bas-droit du trapèze doit être comprise entre 20 degrés et 160 degrés (20 et 160 non comprises)")
        
    else:
        raise ValueError("La longueur de chaque coté du trapèze ne doit pas être inférieure ou égale à 0")
        

   
