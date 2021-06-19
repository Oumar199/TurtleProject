from dessinMSDA import *
def avion():
    """Cette fonction permet de tracer un avion
    """
    #Configuration de la fenetre
    window=Screen()
    window.setup(700, 700)
    window.bgpic("ciel.gif")
    hideturtle()

    #Corps Avion
    begin_fill()
    fillcolor("grey")
    setheading(45)
    set_move(pos()[0] + 70, pos()[1] + 70)
    demi_cercle(25)
    forward(104)
    positionA1 = position()
    forward(60)
    positionA1fin = position()
    forward(110)
    positionqueue1 = position()
    lt(90)
    forward(25)
    positionqueuemoitié1 = position()
    forward(25)
    positionqueue2 = position()
    lt(90)
    fd(110)
    positionA2fin = position()
    fd(60)
    positionA2 = position()
    fd(104)
    end_fill()

    #Ails

    #AilGauche
    begin_fill()
    set_move(positionA1)
    lt(120)
    fd(150)
    lt(50)
    fd(20)
    setpos(positionA1fin)
    end_fill()

    #AilDroite
    begin_fill()
    set_move(positionA2)
    rt(180)
    rt(120)
    fd(150)
    rt(50)
    fd(20)
    setpos(positionA2fin)
    end_fill()

    #QueueGuauche
    begin_fill()
    set_move(positionqueue1)
    rt(180 - 120)
    fd(50)
    left(5)
    fd(20)
    lt(50)
    fd(20)
    lt(110)
    fd(94)
    setpos(positionqueuemoitié1)
    end_fill()

    #QueueDroite
    begin_fill()
    set_move(positionqueue2)
    rt(103)
    lt(180 - 120)
    fd(50)
    rt(5)
    fd(20)
    rt(50)
    fd(20)
    rt(110)
    fd(94)
    end_fill()

    exitonclick()
