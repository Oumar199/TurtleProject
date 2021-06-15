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
    """Cette fonction permettant au turtle de quitter un endroit pour dans un autre sans etre 
    visible
    Method:
        Utilisation de la fonction penup() et pendown() pour lever le crayon et ne rien tracer
        et utiliser la fonction goto pour aller directement vers un endroit selon les coordonnées
    Args:
        x(float ou tuple ou list): si c'est une liste ou un tuple goto la prendra seule comme para-
        -metre sinon goto prendra avec elle un deuxieme parametre de type float
        y(float): le deuxieme parametre de goto si x n'est pas un tuple ou une liste
    Returns: 
        None
    """
    penup()
    if(type(x) is tuple or type(x) is list and len(x) == 2):
        goto(x)
    else:
        goto(x, y)
    pendown()