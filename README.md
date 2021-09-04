# TurtleProject
## Description du projet :
<p align="justify">Ce projet consiste à créer 5 modules pour la création d'un programme permettant de tracer des figures grâce à la librairie Turtle de Python. Pep8 nous a permis de styliser le code. 
Le travail est réparti comme suit : 
- Oumar Kane a créé le module dessinMSDA et le module fusee; 
- Samsidine Diatta a créé le module avion et le module figure_choix;
- Oumar et Samsidine ont collaboré pour créer le module maison;
Les concepts ont été élaborés grâce aux talents de dessinateur de Oumar Kane et à certaines idées ingénieuses apportées par Samsidine. De bonnes connaissances en algorithmique et en python ont été également nécessaires.</p>

## Voici les différentes images obtenues des figures (dessins originaux avec turtle) :
### Voici l’image obtenue de la figure fusee :
![fusee](https://user-images.githubusercontent.com/83582338/122277317-496a6f00-ced5-11eb-835a-082b90f0f2bd.png)
### Voici l'image obtenue de la figure fleur : (figure de choix)
![fleur](https://user-images.githubusercontent.com/83582338/122446496-42556680-cf92-11eb-80b5-fd6828f5150e.png)
### Voici l'image obtenue de la figure maison : 
![maison](https://user-images.githubusercontent.com/83582338/122623052-39e05700-d08a-11eb-9800-0df4ffe25792.png)
### Voici l'image obtenue de la figure avion :
![avion](https://user-images.githubusercontent.com/83582338/122657727-c277f980-d155-11eb-9bab-539683022dc3.png)


## Les tableaux de flux de données de chaque figure : 
On ne précise pas toutes les fonctions utilisées mais seulement celles qui ont été les plus utiles.

### Figure fusée :
|Fusee           |Recoit                 |Fournit                                             |
|----------------|-----------------------|------------------------------------------------------|
|Triangle        |Rien                   |ltri1; lcote2_t2, lcote1_t2, lcote3_t2; lcote2_rc1, lcote3_rc1, lcote1_rc1; lcote1_fire, lcote3_fire, lcote2_fire; lcote2_rc3, lcote3_rc3, lcote1_rc3.|
|Carre           |Rien                   |lcar1; lcar2; lcote2_rc1; lcar3; lcar4                |
|Rectangle       |Rien                   |lrec1, Lrec1; lcote2_rc1; lrec2, lcote2_rc1; lrec3, Lrec3| 
|Cercle          |Rien                   |ray1, ray2                                            |
|origin_al_kachi |lcote3_rc1             |lcote1_rc1, lcote2_rc1, 90                            |

### figure de choix (fleur) :
|Figure_choix    |Recoit                 |Fournit                                             |
|----------------|-----------------------|-----------------------------------------------------|
|Demi_cercle     |Rien                   |rayon de 90 pixels, rayon de 60 pixels, rayon de 40 pixels|


### Figure avion :
|Avion           |Recoit                 |Fournit                                            |
|----------------|-----------------------|-----------------------------------------------------|
|Demi_cercle     |Rien                   |rayon de 25 pixels                                   |

### Figure Maison :
|Maison          |Recoit                 |Fournit                                             |
|----------------|-----------------------|-----------------------------------------------------|
|Rectangle       |Rien                   |largeur_fenetre, longeur_fenetre / 2; longueur_chemine, largeur_chemine; longueur_porte, largeur_porte; longueur_bas_cadre, largeur_bas_cadre; longueur_marche, largeur_marche|
|Cercle          |Rien                   |rayon de 30 pixels                |
|Triangle        |Rien                   |longueurs des côtés du toit       |
|Carre           |Rien                   |longueur cadre                    |
|Carres          |positionpc1            |longueur pc (petit carré)         |


## Conclusion :
Turtle est une librairie trés dynamique et plaît beaucoup aux enfants. C'est normal :), elle permet de déssiner des figures trés impressionnantes. Déssiner une figure demande cependant beaucoup d'imagination et on en a usé tout au long du projet avec une certaine joie. On espère que ces codes serviront à l'avenir.

## Recommandation :
Pour tester les fonctions du programme, rendez vous au fichier jupyter programme_principal.ipynb, enlevez les tags de commentaires sur les fonctions et executez-en !

