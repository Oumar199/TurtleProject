from dessinMSDA import *
def avion():
    """Cette fonction permet de tracer un avion
    """
    #Configuration de la fenetre
    window=Screen()
    window.setup(700, 700)
    window.bgpic("ciel.gif")
    hideturtle()

    #Position Avion
    setheading(57)
    set_move(pos()[0] + 70, pos()[1] + 100)
    
    #Tete Avion
    pencolor("deepskyblue")
    fillcolor("hotpink")
    begin_fill()
    demi_cercle(20)
    end_fill()
    
    #Corps Avion
    begin_fill()
    forward(110)
    positionA1 = position()
    forward(60)
    positionA1fin = position()
    forward(65)
    positionqueue1 = position()
    lt(90)
    forward(20)
    positionqueuemoitié1 = position()
    forward(20)
    positionqueue2 = position()
    lt(90)
    fd(65)
    positionA2fin = position()
    fd(60)
    positionA2 = position()
    fd(110)
    end_fill()
   
    #Ails
    pencolor("hotpink")
    fillcolor("deepskyblue")
    #AilGauche
    begin_fill()
    set_move(positionA1)
    lt(110)
    fd(160)
    lt(50)
    fd(24)
    setpos(positionA1fin)
    setpos(positionA1)
    end_fill()

    #AilDroite
    begin_fill()
    set_move(positionA2)
    rt(168)
    rt(110)
    fd(160)
    rt(50)
    fd(24)
    setpos(positionA2fin)
    setpos(positionA2)
    end_fill()

    pencolor("hotpink")
    fillcolor("deepskyblue")
    #QueueGuauche
    begin_fill()
    set_move(positionqueue1)
    rt(180 - 120)
    fd(46)
    left(5)
    fd(13)
    lt(40)
    fd(19)
    lt(110)
    fd(66)
    setpos(positionqueuemoitié1)
    setpos(positionqueue1)
    end_fill()

    #QueueDroite
    begin_fill()
    set_move(positionqueue2)
    rt(120)
    lt(180 - 120)
    fd(46)
    rt(5)
    fd(13)
    rt(40)
    fd(19)
    rt(110)
    fd(66)
    setpos(positionqueuemoitié1)
    setpos(positionqueue2)
    end_fill()

    exitonclick()
