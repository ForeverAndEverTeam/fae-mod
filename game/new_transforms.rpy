#Sayori sitting transfroms
transform ss1: #Defualt position
    align (0.5, 1)
transform ss2: #Left position
    align (0.5, 1)
    linear 0.5 xanchor 0.3

transform ss1i: #Defualt position (instant)
    align (0.5, 1)

transform chibi(x = 640):
    yanchor 1.0
    pos (x, 1.25)
    easein 0.5 ypos 0.795
transform chibi_hide(x = 64):
    yanchor 1.0
    pos (x, 0.795)
    easeout 0.5 ypos 1.25