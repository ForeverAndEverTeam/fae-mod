#Sayori sitting transfroms
transform ss1: #Defualt position
    on show:
        tinstant(620, 1)
    on replace:
        tcommon(620, 1)
transform ss2: #Left position
    on show:
        tinstant(480, 1)
    on replace:
        tcommon(480, 1) 

transform ss1i: #Defualt position (instant)
    tinstant(620, 1)

transform chibi(x = 640):
    yanchor 1.0
    pos (x, 1.25)
    easein 0.5 ypos 0.795
transform chibi_hide(x = 64):
    yanchor 1.0
    pos (x, 0.795)
    easeout 0.5 ypos 1.25