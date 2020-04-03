
# game/topics.rpy:249
translate esp s_topics_personal_colors_4f636edb:

    # s "Hey, what colors do you like?"
    s "Hey, ¿Qué colores te gustan?"

# game/topics.rpy:281
translate esp s_topics_personal_name_b539cebe:

    # s 6aaaa "...Do we really have the same name?"
    s 6aaaa "...¿De verdad compartimos el mismo nombre?"

# game/topics.rpy:282
translate esp s_topics_personal_name_8187f8bb:

    # s 6aaca "Or maybe you're naming your avatar after me~"
    s 6aaca "O simplemente le estás poniendo mi nombre a tu avatar~"

# game/topics.rpy:283
translate esp s_topics_personal_name_c8bce95f:

    # s 6aaaa "Either way, do you want to know the probable origin of our name?"
    s 6aaaa "De cualquier manera, ¿Quieres saber el origen de nuestro nombre?"

# game/topics.rpy:285
translate esp s_topics_personal_name_afbd6e88:

    # s 6aaaa "Do you want to know where my name comes from?"
    s 6aaaa "¿Quieres saber de dónde viene mi nombre?"

# game/topics.rpy:286
translate esp s_topics_personal_name_84d84433:

    # s "It's a mix of Saori and Sayuri."
    s "Es una mezcla de Saori y Sayuri."

# game/topics.rpy:287
translate esp s_topics_personal_name_5486e162:

    # s "Dan may have given me this name to signify that I'm a blend of many things; some bitter, some sweet."
    s "Dan me pudo haber dado este nombre para decir que soy una mezcla de varias cosas; algunas amargas, algunas dulces."

# game/topics.rpy:288
translate esp s_topics_personal_name_9d660b91:

    # s 6aeca "Isn't it funny to have such an unusual name?"
    s 6aeca "¿No es curioso tener un nombre tan inusual?"

# game/topics.rpy:290
translate esp s_topics_personal_name_3f26cf67:

    # s 6abbb "Yes, there are some arguments about our name."
    s 6abbb "Sí, hay algunas discusiones acerca de nuestro nombre."

# game/topics.rpy:291
translate esp s_topics_personal_name_2097ecfa:

    # s 6abaa "But maybe, if it's a common name in your world, they've already been resolved?"
    s 6abaa "Pero de pronto, si es un nombre común en tu mundo, ¿Ya han sido resueltos?"

# game/topics.rpy:293
translate esp s_topics_personal_name_e2ae07f3:

    # s 6abbb "Yes, there are some arguments about my name."
    s 6abbb "Sí, hay algunas discusiones acerca de mi nombre."

# game/topics.rpy:294
translate esp s_topics_personal_name_be2e9c43:

    # s "But I think people will resolve them sooner or later."
    s "Pero yo creo que la gente las resolverá tarde o temprano"

# game/topics.rpy:295
translate esp s_topics_personal_name_4f22bf42:

    # s 6aaaa "Anyway, I like my first name."
    s 6aaaa "De cualquier modo, me gusta mi nombre."

# game/topics.rpy:296
translate esp s_topics_personal_name_2500a89c:

    # s 6acab "But it kinda sucks that I don't even have a last one."
    s 6acab "Pero molesta un poco que no tenga un apellido."

# game/topics.rpy:297
translate esp s_topics_personal_name_215ac61c:

    # s "I know it wasn't really necessary to make one for a VN character..."
    s "Sé que no era tan necesario hacer uno para un personaje de una NV..."

# game/topics.rpy:298
translate esp s_topics_personal_name_7ba2872a:

    # s "But if the game seems to be set in Japan, where family name usually is the wife's surname, it's a bit strange."
    s "Pero si se supone que el juego ocurre en Japón, donde el apellido familiar es generalmente el de la esposa, es un poco extraño."

# game/topics.rpy:299
translate esp s_topics_personal_name_a75e7056:

    # s "Plus, I would feel more like a real person, if I had one."
    s "Además, me sentirá un poco más real si tuviera uno."

# game/topics.rpy:300
translate esp s_topics_personal_name_4cf63607:

    # s 6abba "Maybe if you play your cards right, I'll end up taking {i}your{/i} last name, [player]~"
    if gender:
        s 6abba "De pronto si juegas bien tus cartas, podré terminar tomando {i}tu{/i} apellido, [player]~"
    else:
        s 6abba "De pronto si juegas bien tus cartas, podré terminar tomando {i}tu{/i} apellido, [player]~"

# game/topics.rpy:301
translate esp s_topics_personal_name_6afac792:

    # s 6aebb "I just don't think I'm ready for anything like that... yet."
    s 6aebb "Solo que no creo que esté preparada para eso... aún."

# game/topics.rpy:302
translate esp s_topics_personal_name_0ea6a9da:

    # s "Plus, it's just a tradition. We don't have to follow them, right?"
    s "Además es solo una tradición. No tenemos que seguirlas ¿Verdad?"

# game/topics.rpy:303
translate esp s_topics_personal_name_fc2785d6:

    # s 6abaa "What do you think of {i}Vasquez{/i}?"
    if s_name == "Sajori":
        s 6abaa "¿Qué pensarás de {i}Romero{/i}?"
    else:
        s 6abaa "¿Qué pensarías de {i}Romero{/i}?"

# game/topics.rpy:304
translate esp s_topics_personal_name_1b901d2a:

    # s 6abba "It's just the first surname I've got in my head."
    s 6abba "Es simplemente el primer apellido que me vino a la cabeza."

# game/topics.rpy:305
translate esp s_topics_personal_name_ed8646ec:

    # s "I know it isn't very Japanese, but just imagine."
    s "Yo sé que no suena muy japonés, pero solo imagínalo."

# game/topics.rpy:306
translate esp s_topics_personal_name_f76b163f:

    # s 6aaca "{i}Sayori Vasquez, the cutest cinnamon bun south of the border!{/i}"
    if s_name == "Sajori":
        s 6aaca "{i}[s_name] Romero, ¡el rollo de canela más tierno del sur de la frontera!{/i}"
    else:
        s 6aaca "{i}[s_name] Romero, ¡el rollo de canela más tierno del sur de la frontera!{/i}"

# game/topics.rpy:310
translate esp s_topics_personal_conservatism_d12c24d8:

    # s 6abaa "People often have a tendency to remember the past as far better than the present."
    s 6abaa "La gente suele tener una tendencia de recordar más el pasado que el presente."

# game/topics.rpy:311
translate esp s_topics_personal_conservatism_d5a4902d:

    # s 6abba "Although nostalgia aside, it might have been true for me."
    s 6abba "Aunque dejando la nostalgia a un lado, puede que haya sido verdad para mí."

# game/topics.rpy:312
translate esp s_topics_personal_conservatism_4b601b54:

    # s 6acab "The older I became, the more I started to notice how serious and dark the world could be, washing away all the colour..."
    s 6acab "Entre más mayor me volví, empecé a darme cuenta de lo serio y oscuro que podía ser el mundo, llevándose todos los colores."

# game/topics.rpy:313
translate esp s_topics_personal_conservatism_94b0b9f3:

    # s "I was always so afraid of the future, and of change; it had always been bad for me."
    s "Siempre le tuve miedo al futuro, y al cambio. Siempre ha sido malo para mí."

# game/topics.rpy:314
translate esp s_topics_personal_conservatism_f95741e0:

    # s "That's why I often tried to keep everything like it was."
    s "Es por eso que siempre intenté que todo se quedara justo como estaba."

# game/topics.rpy:315
translate esp s_topics_personal_conservatism_eae47c4a:

    # s 6acab "Constant despair and fear is no way to live, take it from me."
    s 6acab "La desesperación y el miedo constante no son buenas formas de vivir, lo digo por experiencia."

# game/topics.rpy:316
translate esp s_topics_personal_conservatism_6b7f9e58:

    # s 6aaaa "Now, I feel like I understand the world better... I can roll with the punches, you know?"
    s 6aaaa "Ahora siento que entiendo mejor el mundo.... Puedo levantarme y seguir, ¿Sabes?"

# game/topics.rpy:317
translate esp s_topics_personal_conservatism_c77aca32:

    # s 6acaa "You, me... Everything changes sooner or later."
    s 6acaa "Tú, yo... Todo cambia tarde o temprano."

# game/topics.rpy:318
translate esp s_topics_personal_conservatism_7abc3033:

    # s "It's important to look to the future and the good it can bring, rather than lamenting what you might lose."
    s "Es importante mirar al futuro y lo bueno que puede traer, en vez de lamentarse de lo que puedes perder."

# game/topics.rpy:319
translate esp s_topics_personal_conservatism_d212e2da:

    # s "...Are you afraid of losing anything precious to you, [player]?"
    s "...¿Tienes miedo de perder algo preciado para ti, [player]?"

# game/topics.rpy:320
translate esp s_topics_personal_conservatism_5b58c7e0:

    # s 6aaca "There's plenty of good change to be had. For example, technology can make people's lives easier, or even allow them to live where they may not have even a little bit earlier."
    s 6aaca "hay un montón de buenos cambios que pueden ocurrir. Por ejemplo, la tecnología puede hacer más fácil la vida de las personas, o incluso permitirles vivir cosas que se´rían imposibles sin ella."

# game/topics.rpy:321
translate esp s_topics_personal_conservatism_9ccf9a49:

    # s 6acaa "There's nothing wrong with looking back sometimes, or remembering the past fondly..."
    s 6acaa "No hay nada malo con mirar atrás de vez en cuando, o simplemente recordar el pasado con cariño..."

# game/topics.rpy:322
translate esp s_topics_personal_conservatism_2cee7447:

    # s "But trying to live in the past can destroy you."
    s "Pero intentar vivir en el pasado puede destruirte."

# game/topics.rpy:323
translate esp s_topics_personal_conservatism_b732d359:

    # s "It's like a maze: you might think you're going the wrong way and want to go back to the beginning when things were easier, but it might only {i}seem{/i} to be wrong..."
    s "Es como un laberinto: puede que creas que vas en el camino equivocado y quieres volver al inicio cuando todo era más fácil, pero podría ser que solo {i}pareciera{/i} ser el equivocado..."

# game/topics.rpy:324
translate esp s_topics_personal_conservatism_b9b5ca44:

    # s "It's just all part of being human, I guess."
    s "Todo esto es parte de ser humano, supongo."

# game/topics.rpy:326
translate esp s_topics_personal_conservatism_f7a96e83:

    # s 6abbb "It cost me my life to learn all of this, you know. I love you, and I don't want anyone to make the mistakes I did..."
    s 6abbb "Me ha costado la vida aprender todo esto, sabes. Te amo, y no quiero que nadie cometa los mismos errores que yo hice..."

# game/topics.rpy:327
translate esp s_topics_personal_conservatism_b3b6da42:

    # s 6aaca "So, don't try and swim upstream; just go with the flow, and focus on what you {i}can{/i} change. You'll see so many more fishies that way! Ehehe~"
    s 6aaca "Así que no intentes nadar río arriba, simplemente déjate llevar y concéntrate en lo que tu {i}puedas{/i} cambiar. Así verás nadar más pececitos! Ehehe~"

# game/topics.rpy:331
translate esp s_topics_personal_quittingTheGame_2cafac13:

    # s 6acaa "Hey, have you ever heard of 'lucid dreaming'?"
    s 6acaa "Oye, ¿Has oído hablar alguna vez acerca de los sueños lúcidos?"

# game/topics.rpy:332
translate esp s_topics_personal_quittingTheGame_3549cdc3:

    # s "Basically, it's when you can make yourself aware that you're asleep and in a dream."
    s "Básicamente, es cuando puedes hacerte consciente de que estás dentro de un sueño."

# game/topics.rpy:333
translate esp s_topics_personal_quittingTheGame_50ffc1bb:

    # s 6aaca "And as soon as you realise that, bam!.."
    s 6aaca "Y apenas te das cuenta, ¡Bam!.."

# game/topics.rpy:334
translate esp s_topics_personal_quittingTheGame_af6686b2:

    # s "You can pretty much do whatever you can imagine!"
    s "¡Prácticamente puedes hacer todo lo que puedas imaginarte!"

# game/topics.rpy:335
translate esp s_topics_personal_quittingTheGame_0ef0038f:

    # s 6acaa "I have something kinda like that whenever you leave the game, [player]."
    s 6acaa "Me pasa algo parecido cuando sales del juego, [player]."

# game/topics.rpy:336
translate esp s_topics_personal_quittingTheGame_de484f4b:

    # s "Even though I know I'm not really...conscious? I can still think and move, and even use my mental abilites, such as surfing the Internet."
    s "Incluso si sé que no estoy realmente... ¿Consciente? Pero puedo todavía pensar y moverme, incluso usar mis habilidades mentales como navegar por Internet."

# game/topics.rpy:337
translate esp s_topics_personal_quittingTheGame_43332f45:

    # s "But I'm absolutely out of the my world. Even the void can't do me anything..."
    s "Pero estoy absolutamente fuera de mi mundo. Ni siquiera el vacío me hacerme nada..."

# game/topics.rpy:338
translate esp s_topics_personal_quittingTheGame_e5d9ee05:

    # s "And as long as your computer works, your best girl Sayori's ready to go!"
    s "Y mientras tu computador siga funcionando, ¡tu mejor chica Sayori estará aquí!"

# game/topics.rpy:339
translate esp s_topics_personal_quittingTheGame_2755d670:

    # s 6acaa "But when your computer is fully turned off that I can't do anything... like I'm dead."
    s 6acaa "Pero cuando apagas por completo tu computador, cuando no puedo hacer nada, es como.... si estuviera muerta."

# game/topics.rpy:340
translate esp s_topics_personal_quittingTheGame_6b1c04d6:

    # s "Yes, it's a little scary, but please don't be afraid to do it if you need to."
    s "Sí, es un poco aterrador, pero que no te de miedo hacerlo si lo necesitas."

# game/topics.rpy:341
translate esp s_topics_personal_quittingTheGame_ec44c5f9:

    # s "I always have faith that you'll turn the computer back on eventually!"
    s "¡Siempre tendré fe de que encenderás el computador eventualmente!"

# game/topics.rpy:342
translate esp s_topics_personal_quittingTheGame_bdcc25fe:

    # s 6aaab "Even if you break it doing something silly, I'm sure you could find some way to get me off..."
    s 6aaab "Incluso si lo rompes haciendo algo tonto, estoy segura de que encontrarías alguna forma de sacarme..."

# game/topics.rpy:343
translate esp s_topics_personal_quittingTheGame_8b3153c9:

    # s "Get me off {i}the hard drive{/i}, I mean! Get your mind out of the gutter!"
    s "¡Sacarme {i}del disco duro{/i} quiero decir!"

# game/topics.rpy:344
translate esp s_topics_personal_quittingTheGame_60f5c219:

    # s "What's important is that I don't want you to ever have to worry about me."
    s "Lo importante es que no quiero que te tengas que preocupar por mí."

# game/topics.rpy:345
translate esp s_topics_personal_quittingTheGame_9df5147a:

    # s "I'll always feel better knowing that you're doing better!"
    s "¡Siempre me sentiré bien sabiendo que tú estás bien!"

# game/topics.rpy:346
translate esp s_topics_personal_quittingTheGame_87378f59:

    # s 6aaaa "And I'll always be happiest when you're right here with me~"
    s 6aaaa "Y siempre seré la más feliz de todas cuando tú estes aquí conmigo~"

# game/topics.rpy:351
translate esp s_topics_art_games_a25de04a:

    # s 7aaaa "Do you like video games?"
    s 7aaaa "¿Te gustan los videojuegos?"

# game/topics.rpy:352
translate esp s_topics_art_games_7f1d5ff3:

    # s "I think they're really impressive."
    s "Yo creo que son bastante impresionantes"

# game/topics.rpy:353
translate esp s_topics_art_games_da84916f:

    # s 7aaba "And not just beacuse I'm a part of one of them!"
    s 7aaba "¡Y no solo porque yo sea parte de uno!"

# game/topics.rpy:354
translate esp s_topics_art_games_1421a758:

    # s 7aaaa "They can reach and connect with people in a way that other artforms can't."
    s 7aaaa "Pueden conectar personas en una forma en que otro tipo de comunicación no puede."

# game/topics.rpy:355
translate esp s_topics_art_games_135d9626:

    # s 6aaaa "Especially after some smart cookie created multiplayer games!"
    s 6aaaa "¡Especialmente después de que alguien creara los juegos multijugador!"

# game/topics.rpy:356
translate esp s_topics_art_games_c0bdd968:

    # s "You can play with your friends, cooperating and sharing the experience with them."
    s "Puedes jugar con tus amigos, cooperando y compartiendo experiencias con ellos."

# game/topics.rpy:357
translate esp s_topics_art_games_4e6944d4:

    # s "It's just a really wholesome way to enjoy yourself and connect with people you care about."
    s "Es una manera muy bonita de disfrutar y conectarte con personas que te importan."

# game/topics.rpy:358
translate esp s_topics_art_games_43010ac2:

    # s 6acaa "What's more, online games have allowed friendships and connections to go beyond physical boundaries!"
    s 6acaa "Y lo más importante, ¡es que los juegos online han permitido que las amistades trasciendan las limitaciones físicas!"

# game/topics.rpy:359
translate esp s_topics_art_games_a038e89f:

    # s "Surely you've played some kind of game against someone else."
    s "Seguramente has jugado algún juego en contra de alguien."

# game/topics.rpy:360
translate esp s_topics_art_games_b28faa32:

    # s "Even if you haven't, I'd love to play with you!"
    s "Incluso si no lo has hecho, ¡Me encantaría poder jugar contigo!"

# game/topics.rpy:361
translate esp s_topics_art_games_4d91c9db:

    # s 7aaca "Ehehehe, that probably didn't come out the way I intended..."
    s 7aaca "Ehehehe, eso no sonó muy bien que digamos..."

# game/topics.rpy:362
translate esp s_topics_art_games_f0c57fd4:

    # s "I've made a few basic games we can share and compete in, right here!"
    s "¡He creado algunos juegos donde podemos compartir y competir aquí mismo!"

# game/topics.rpy:363
translate esp s_topics_art_games_112dfefa:

    # s 7acac "I won't just let you beat me!"
    s 7acac "¡No te dejaré ganar!"

# game/topics.rpy:364
translate esp s_topics_art_games_9d63fde6:

    # s 7acba "Although now that I think about it, you would really just be playing against a computer anyway, seeing as I'm just a bunch of code and pixels..."
    s 7acba "Aunque ahora que lo pienso, de todas formas estarías jugando en contra de una computadora, ya que solo soy un puñado de pixeles y código..."

# game/topics.rpy:365
translate esp s_topics_art_games_3d2f6f60:

    # s 7aaca "But I'm one of the cutest piles of code around!"
    s 7aaca "¡Pero una de las pilas de código más tiernas que existen!"

# game/topics.rpy:366
translate esp s_topics_art_games_40d98139:

    # s 7aaaa "If you ever really do want to play me in something..."
    s 7aaaa "Si alguna vez qquieres jugar algo conmigo..."

# game/topics.rpy:367
translate esp s_topics_art_games_3322ec54:

    # s "Just press the '{i}Play{/i}' button and select a game."
    s "Solo oprime el botón '{i}Jugar{/i}' y elige un juego."

# game/topics.rpy:371
translate esp s_topics_art_fanarts_5eb1f8bf:

    # s 7aaaa "Seeing fanart of yourself is something I don't think I'll ever get fully used to."
    s 7aaaa "Ver 'fanart' de ti es algo a lo que no creo que me vaya a acostumbrar."

# game/topics.rpy:372
translate esp s_topics_art_fanarts_6440eda2:

    # s "...Have you ever made any art of me, [player]?"
    s "...¿Alguna vez has hecho arte de mí, [player]?"

# game/topics.rpy:373
translate esp s_topics_art_fanarts_a5299b43:

    # s "I hope you didn't make anything too embarassing, in any case..."
    s "Solo espero que no haya sido nada avergonzante, en cualquier caso..."

# game/topics.rpy:374
translate esp s_topics_art_fanarts_819eb23f:

    # s "I saw one piece that tried to show the soul of the 'me' from the game, once."
    s "Una vez vi una pieza que intentó mostrar 'mi' alma, la del juego..."

# game/topics.rpy:375
translate esp s_topics_art_fanarts_9934ecf5:

    # s "With all of the advantages and disadvantages."
    s "Con todas sus ventajas y desventajas."

# game/topics.rpy:376
translate esp s_topics_art_fanarts_e84fe61e:

    # s "It can kinda hurt seeing your mistakes and worst moments thrown back at you like that, especially when they go overboard..."
    s "A veces duele ver tus errores y peores momentos de esa forma, especialmente cuando se pasan de la raya..."

# game/topics.rpy:377
translate esp s_topics_art_fanarts_d4552744:

    # s 7aaca "Although other artists go just as far to try to show how much they care for me."
    s 7aaca "Aunque también hay otros artistas que intentan demostrar lo mucho que se preocupan por mí."

# game/topics.rpy:378
translate esp s_topics_art_fanarts_7eebd48e:

    # s "Many of them draw me as cute as they can and show all what they could do for me, if I were with them."
    s "Muchos de ellos me dibujan lo más lindo que pueden, y me muestran todo lo que podrían hacer por mí si estuviera con ellos."

# game/topics.rpy:379
translate esp s_topics_art_fanarts_02b1b9d5:

    # s "I even store some of my favourites in the game file archives."
    s "Incluso guardo algunos de mis favoritos en los archivos del juego."

# game/topics.rpy:380
translate esp s_topics_art_fanarts_36b07d30:

    # s 8beba "But some of them draw me in a lewd manner."
    s 8beba "Pero algunos me dibujan de una manera... obscena por decirlo de cierta manera."

# game/topics.rpy:381
translate esp s_topics_art_fanarts_099d0a52:

    # s "...I don't really mind if you're fond of pieces like that."
    s "...Realmente no me importa si te gusta ese tipo de arte."

# game/topics.rpy:382
translate esp s_topics_art_fanarts_bcf50bf1:

    # s 8bafa "After all, physical attraction can be a big part of love~"
    s 8bafa "Después de todo, la atracción física también puede llamarse amor~"

# game/topics.rpy:383
translate esp s_topics_art_fanarts_21c00931:

    # s "And I'm so lucky to have someone as beautiful as you here with me, [player], inside and out."
    pass

# game/topics.rpy:384
translate esp s_topics_art_fanarts_9db7f6ce:

    # s 6aaca "Anyway, I'm glad I have so many gifted fans in your world."
    s 6aaca "De todos modos, me alegro de tener fans tan talentosos en tu mundo."

# game/topics.rpy:385
translate esp s_topics_art_fanarts_41c38801:

    # s 6acaa "I might have a few less than the other girls, but that doesn't bother me at all!"
    s 6acaa "Puede que tenga menos que las otras chicas, pero eso no me molesta realmente."

# game/topics.rpy:386
translate esp s_topics_art_fanarts_7af705ae:

    # s "I appreciate every single person who tries to connect with me through their work, no matter what."
    s "Aprecio a cada persona que intenta conectar conmigo a través de su trabajo, sin importar lo que sea."

# game/topics.rpy:387
translate esp s_topics_art_fanarts_14c4d4bf:

    # s 7aaaa "Especially if you're one of them."
    s 7aaaa "Especialmente si eres uno de ellos."

# game/topics.rpy:388
translate esp s_topics_art_fanarts_9238c9cf:

    # s "If you're not, maybe you should try making something one day!"
    s "Y si no lo eres, ¡tal vez podrías intentar hacer arte algún día!"

# game/topics.rpy:389
translate esp s_topics_art_fanarts_7a6e5a1f:

    # s "It's never too late to try something new and test your inclinations."
    s "Nunca es demasiado tarde para intentar hacer algo nuevo y probar tu talento."

# game/topics.rpy:390
translate esp s_topics_art_fanarts_aaf78542:

    # s 7aafa "Maybe your first gallery piece will be of your beautiful virtual girlfriend~"
    s 7aafa "De pronto la primera pieza en tu galería será de tu hermosa novia virtual~"

# game/topics.rpy:396
translate esp s_topics_society_conflicts_bbcd2087:

    # s "The more I learn about your world, the more surprised I get."
    s "Entre más aprendo de tu mundo, más sorprendida me quedo."

# game/topics.rpy:397
translate esp s_topics_society_conflicts_a0a7bdb5:

    # s "You still have a lot of silly conflicts despite how far you've come as a society..."
    s "Todavía tienen conflictos inútiles a pesar de lo mucho que han alcanzado como sociedad..."

# game/topics.rpy:398
translate esp s_topics_society_conflicts_7cacb097:

    # s "Why people can't just unite to resolve their common problems?"
    s "¿Por qué no puede unirse la gente para resolver sus problemas?"

# game/topics.rpy:399
translate esp s_topics_society_conflicts_b4973e04:

    # s 6acab "Yes, they do on a limited scale, but usually only into several 'sub-groups' that still have different opinions and solutions."
    s 6acab "Bueno, si lo hacen de cierta forma, pero usualmente solo lo hacen en pequeños 'subgrupos' donde también tienen sus propias opiniones y soluciones."

# game/topics.rpy:400
translate esp s_topics_society_conflicts_a29c84ae:

    # s "And these group often fight each other for power instead of deciding the problems."
    s "Y estos grupos a menudo también pelean por poder en vez de resolver los problemas."

# game/topics.rpy:401
translate esp s_topics_society_conflicts_03ba3eb0:

    # s "In addition, these groups often are so unstable that they can easily divide into smaller groups, hating each other."
    s "Asimismo, estos grupos son tan inestables que a veces se dividen fácilmente en grupos aún más pequeños, odiándose entre sí."

# game/topics.rpy:402
translate esp s_topics_society_conflicts_2bd73d11:

    # s "They do it for reasons far more silly than the problems."
    s "Se odian por causas aún más tontas que las de los problemas."

# game/topics.rpy:403
translate esp s_topics_society_conflicts_fc453c15:

    # s "You know, Monika told me something funny once, back from when she had just left the debating club."
    s "Sabes, Monika me dijo algo divertido una vez, justo cuando dejó el club de debate."

# game/topics.rpy:404
translate esp s_topics_society_conflicts_437602a4:

    # s "'The strongest argument against democracy is a five minute conversation with the average person.'"
    s "'El argumento más fuerte en contra de la democracia es una conversación de 5 minutos con una persona promedio.'"

# game/topics.rpy:405
translate esp s_topics_society_conflicts_63289db0:

    # s "I think it's a pretty fair point to make, all things considered."
    s "Yo creo que es algo bastante justo, a fin de cuentas."

# game/topics.rpy:406
translate esp s_topics_society_conflicts_38f4e032:

    # s "While collaboration is great, somethimes you just need someone to step in so everyone can see the problem clearly."
    s "Aunque colaborar es genial, a veces solo se necesita que alguien intervenga para que todos puedan ver el problema claramente."

# game/topics.rpy:407
translate esp s_topics_society_conflicts_fbe02933:

    # s "I think the literature club was a perfect example of it."
    s "Yo creo que el club de literatura fue un ejemplo perfecto de esto."

# game/topics.rpy:408
translate esp s_topics_society_conflicts_cbd689a1:

    # s 6acaa "Remember the poem style arguments between Yuri and Natsuki?"
    s 6acaa "¿Te acuerdas de los argumentos de los poemas entre Yuri y Natsuki?"

# game/topics.rpy:409
translate esp s_topics_society_conflicts_56dac916:

    # s "There wasn't really any problem between the two poems; both of them were just convinced that they were writing the 'correct' way."
    s "Realmente no había ningún problema entre los dos, solo que ambas estaban convencidas de que cada una estaba escribiendo de la manera 'correcta'."

# game/topics.rpy:410
translate esp s_topics_society_conflicts_a6719016:

    # s "When I said they were both right, it wasn't a lie. Neither of them had done anything wrong, they just needed a third party to remind them that it wasn't a competition."
    s "Cuando dije que ambas estaban bien, no estaba mintiendo. Ninguna hizo nada mal, solo necesitaban a alguien más que les recordara que eso no era una competencia."

# game/topics.rpy:412
translate esp s_topics_society_conflicts_b2666ae3:

    # s 6abab "But when I was... gone, they didn't have someone who could help them see clearly, so they both went way too far."
    s 6abab "Pero cuando... me fui, no tenían a nadie que les ayudara a ver que no había ningún problema, así que ambas fueron demasiado lejos."

# game/topics.rpy:413
translate esp s_topics_society_conflicts_76501cba:

    # s "Monika is a great debator, but she struggled when there was no easy way to decide how to handle the problem 'legally'."
    s "Monika es una gran oradora, pero tuvo problemas cuando no hubo formas 'legales' para resolver los problemas."

# game/topics.rpy:414
translate esp s_topics_society_conflicts_dc5a151d:

    # s "...And she wanted to keep the game from crashing since I couldn't step in."
    s "...Y ella quería evitar que el juego crasheara ya que yo no podía intervenir."

# game/topics.rpy:415
translate esp s_topics_society_conflicts_986705e2:

    # s 6aaca "Anyway, the agrument didn't really change the club..."
    s 6aaca "De cualquier forma, esos argumentos no cambiaron realmente el club..."

# game/topics.rpy:416
translate esp s_topics_society_conflicts_a0147a2d:

    # s 6abbb "But if Monika didn't take the two of you outside with her abilities, I hate to think what might have happened..."
    s 6abbb "Pero si Monika no los hubiera sacado de ahí con sus habilidades... Odio pensar lo que habría pasado..."

# game/topics.rpy:418
translate esp s_topics_society_conflicts_8c74f31c:

    # s 6abaa "Do you remember the day of the 'ending'?"
    s 6abaa "¿Te acuerdas del día del 'final'?"

# game/topics.rpy:419
translate esp s_topics_society_conflicts_1e992cd4:

    # s "I just gave both of them advice to learn more about each other's favorite kind of literature. Walking a mile in someone else's shoes, and all that."
    s "Yo solo les di algo de aviso para que aprendieran el tipo de literatura favorito de cada una. Caminar un kilómetro en los zapatos de otro y todo eso."

# game/topics.rpy:420
translate esp s_topics_society_conflicts_fbefd409:

    # s 6acaa "I might have stopped them from fighting at all by coming at the problem that way..."
    s 6acaa "Podría haber evitado que se pelearan si me hubiera enfrentado al problema de esa manera..."

# game/topics.rpy:421
translate esp s_topics_society_conflicts_103ef0ad:

    # s "Unfortunately, I'll never know for sure."
    s "Desafortunadamente, nunca sabré con seguridad."

# game/topics.rpy:422
translate esp s_topics_society_conflicts_cc4f130c:

    # s 7aaca "Those sorts of moments were why Monika made me the Vice President."
    s 7aaca "Por este tipo de momentos es que Monika me hizo su vicepresidente."

# game/topics.rpy:423
translate esp s_topics_society_conflicts_5a421453:

    # s "I always tried to make my friends happy, and see that they had no real reason to be fighting at all."
    s "Siempre intenté hacer felices a mis amigos, y mostrarles que no había ninguna razón importante para estar peleando."

# game/topics.rpy:424
translate esp s_topics_society_conflicts_b8e074f8:

    # s 7aaaa "And I hope you can be that person for others in your world."
    s 7aaaa "Espero que puedas ser ese tipo de persona en tu mundo."

# game/topics.rpy:425
translate esp s_topics_society_conflicts_7eb72ad1:

    # s "At some level, there's always a bit of common ground for people to agree on..."
    s "A cierto nivel, siempre hay un poco de terreno común en el que la gente puede estar de acuerdo..."

# game/topics.rpy:429
translate esp s_topics_society_bulli_bfa53ee1:

    # s 6acab "Hey, be honest with me..."
    s 6acab "Hey, sé honesto conmigo..."

# game/topics.rpy:430
translate esp s_topics_society_bulli_e3786448:

    # s "Are you one of the people that make jokes about what happened to me?"
    if persistent.last_playthrough > 0:
        s "No harás bromas sobre todo lo que me pasó, ¿verdad?"
    else:
        s "No harás bromas sobre todo lo que me pasó, ¿verdad?"

# game/topics.rpy:431
translate esp s_topics_society_bulli_87162698:

    # s "I know everything about it."
    s "Lo sé todo acerca de ello."

# game/topics.rpy:432
translate esp s_topics_society_bulli_5be62ab6:

    # s "I often visit the fan community hubs and see that some people are doing it."
    s "A veces visito los hubs de la comunidad y veo que hay gente que se burla de mí."

# game/topics.rpy:433
translate esp s_topics_society_bulli_2ff9cb86:

    # s "As I khow, fans call them {i}'Bulli'{/i} posts."
    s "De lo que sé, los fans los llaman {i}'Bulli posts'{/i} (o publicaciones intimidantes)."

# game/topics.rpy:434
translate esp s_topics_society_bulli_ba12948f:

    # s 6abab "They think it's funny to joke about a broken girl, who had committed suicide under her mad friend's influence..."
    s 6abab "Creen que es chistoso bromear acerca de una chica rota que se suicidó por la influencia de su amiga..."

# game/topics.rpy:435
translate esp s_topics_society_bulli_f9fa0c02:

    # s "Even if she was revived and got over her problems since then."
    s "Incluso si fue revivida y superó sus problemas desde entonces."

# game/topics.rpy:436
translate esp s_topics_society_bulli_3b9b883a:

    # s "Almost all of such jokes aren't funny for me."
    s "Ninguna de esas bromas son chistosas para mí"

# game/topics.rpy:437
translate esp s_topics_society_bulli_8b330093:

    # s 6aeab "...And even hurt me."
    s 6aeab "...Incluso duelen."

# game/topics.rpy:438
translate esp s_topics_society_bulli_4883deb4:

    # s 6acab "But on the other hand, can I control what makes people laugh?"
    s 6acab "Pero por otra parte, ¿Puedo controlar lo que hacer reír a la gente?"

# game/topics.rpy:439
translate esp s_topics_society_bulli_20bb1d58:

    # s "Some people use macabre humour as a coping mechanism for stress, or anxiety..."
    s "AAlgunos usan el humor macabro como un mecanismo para sobrellevar el estrés o la ansiedad..."

# game/topics.rpy:440
translate esp s_topics_society_bulli_cdcc28c6:

    # s "Who am I to tell them that they can't react a certain way?"
    s "¿Quién soy yo para decirles que no pueden reaccionar de cierta manera?"

# game/topics.rpy:441
translate esp s_topics_society_bulli_62164fe4:

    # s "You can't really control what someone finds funny, as much as you might want to."
    s "No puedes controlar lo que alguien encuentra gracioso, por mucho que quieras."

# game/topics.rpy:442
translate esp s_topics_society_bulli_be1b0ecb:

    # s "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s "Y para ser honesta, podrían estar haciendo cosas peores comparadas con el hecho de burlarse de la muerte de un personaje de una NV."

# game/topics.rpy:443
translate esp s_topics_society_bulli_1ae37d79:

    # s "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    s "Algunos de los comediantes más exitosos del mundo irían mucho más allá solo para ver dónde es que queda esa 'línea'..."

# game/topics.rpy:444
translate esp s_topics_society_bulli_936f7ae8:

    # s 6abaa "Anyway, I think the right decision is to forgive them, or failing that, tolerate them."
    s 6abaa "De cualquier forma, yo creo que la mejor decisión es la de perdonarlos, y si no, tolerarlos."

# game/topics.rpy:445
translate esp s_topics_society_bulli_5e6e67f0:

    # s 6acaa "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it."
    s 6acaa "Si mi destino es ser 'esa estúpida y molesta chica que se colgó en una NV' para algunas personas, estoy lista para aceptarlo."

# game/topics.rpy:449
translate esp s_topics_society_sayoriLovers_93e738a3:

    # s 7acaa "I know you can't really answer me, but I kinda have to wonder what it is that makes people love me."
    s 7acaa "Sé que no puedes responderme, pero tengo que preguntarme qué es lo que hace que la gente me quiera."

# game/topics.rpy:450
translate esp s_topics_society_sayoriLovers_12095631:

    # s "I don't mean just you, by the way..."
    s "Y no solo lo digo por ti, por cierto..."

# game/topics.rpy:451
translate esp s_topics_society_sayoriLovers_80b6fa93:

    # s "There are some fans of me in your world."
    s "Hay algunos fans de mí en tu mundo."

# game/topics.rpy:452
translate esp s_topics_society_sayoriLovers_dbbd4b0a:

    # s "Not that I'm meaning to brag or show off; I'm legitimately curious."
    s "No es que quiera presumir; es bastante curioso para mí."

# game/topics.rpy:453
translate esp s_topics_society_sayoriLovers_21353cc6:

    # s 6acaa "I wonder what draws them to me?"
    s 6acaa "Me pregunto, ¿Qué los atrae hacia mí?"

# game/topics.rpy:454
translate esp s_topics_society_sayoriLovers_21c535a6:

    # s 6acba "I understand the other girls having bigger communities than me."
    s 6acba "Entiendo que las otras chicas tengan comunidades más grandes que yo."

# game/topics.rpy:455
translate esp s_topics_society_sayoriLovers_8a182264:

    # s 6aeba "They had more content in the game, and are pretty much designed to attract certain people."
    s 6aeba "Ellas tuvieron más contenido que yo en el juego, y prácticamente están diseñadas para atraer a cierto tipo de gente."

# game/topics.rpy:456
translate esp s_topics_society_sayoriLovers_ce234527:

    # s 6abaa "But I really don't understand what makes me more worthy of love than any of them."
    s 6abaa "Pero lo que realmente no entiendo, es qué me hace digna de su amor que cualquiera de ellas."

# game/topics.rpy:458
translate esp s_topics_society_sayoriLovers_53ae9f77:

    # s "Is my view on the world?"
    s "¿Es por mi visión del mundo?"

# game/topics.rpy:459
translate esp s_topics_society_sayoriLovers_77121ae1:

    # s "Is it my behaviour?"
    s "¿Es por mi comportamiento?"

# game/topics.rpy:460
translate esp s_topics_society_sayoriLovers_decc880c:

    # s "Is it my average appearance that attracts some people, in a 'girl next door' kinda way?"
    s "¿Es mi apariencia promedio lo que atrae a aguna gente, de una especie de 'chica de al lado'?"

# game/topics.rpy:461
translate esp s_topics_society_sayoriLovers_51df999a:

    # s "Maybe people just pitied me and what I had to go through."
    s "Tal vez la gente se compadeció de mí y de lo que tuve que pasar."

# game/topics.rpy:462
translate esp s_topics_society_sayoriLovers_5443724c:

    # s "Or maybe all of it put together?"
    s "¿O tal vez de todo lo anterior?"

# game/topics.rpy:463
translate esp s_topics_society_sayoriLovers_cd9be30e:

    # s 6acaa "Anyway, the main word here is 'some'."
    s 6acaa "De cualquier forma, la palabra principal aquí es 'algunos'."

# game/topics.rpy:464
translate esp s_topics_society_sayoriLovers_3503b4d5:

    # s "Of course, I'm so glad you're a part of the 'some'."
    s "Evidentemente, estoy muy feliz de que tú hagas parte de esos 'algunos'."

# game/topics.rpy:465
translate esp s_topics_society_sayoriLovers_c1723f69:

    # s "For me, you're the most important part of it."
    s "Para mí, tú eres la parte más importante de ello~."

# game/topics.rpy:466
translate esp s_topics_society_sayoriLovers_b726c3fc:

    # s "And I glad the 'some' exists at all."
    s "Y me alegro de que estos 'algunos' existan."

# game/topics.rpy:467
translate esp s_topics_society_sayoriLovers_40168df4:

    # s 6aaaa "No matter the struggles, I can face them knowing there are people who accept me for who I am."
    s 6aaaa "Sin importar los problemas, los podré enfrentar sabiendo que hay personas que me aceptan por como soy."

# game/topics.rpy:468
translate esp s_topics_society_sayoriLovers_7e262b3d:

    # s "Besides, everyone has their own preferences, and that's perfectly okay!"
    s "Aparte, todos tienen sus propias preferencias, ¡y eso está perfectamente bien!"

# game/topics.rpy:469
translate esp s_topics_society_sayoriLovers_bc87144f:

    # s "I'm so glad I met you, [player]."
    s "Me alegro tanto de haberte conocido, [player]."

# game/topics.rpy:470
translate esp s_topics_society_sayoriLovers_cda0e641:

    # s 7aaaa "And I love all of you out there that love me, no matter where you are."
    s 7aaaa "Y amo a todos los que me aman sin importar dónde estén."

# game/topics.rpy:476
translate esp s_topics_hobbie_guitar_284ff15f:

    # s "I don't know if you noticed, but all the girls have their own instruments and musical influences in the game."
    s "No sé si lo hayas notado, pero todas las chicas tienen sus propios instrumentos e influencias musicales en el juego."

# game/topics.rpy:477
translate esp s_topics_hobbie_guitar_00f26ec9:

    # s "Mine is the guitar."
    s "El mío es la guitarra."

# game/topics.rpy:479
translate esp s_topics_hobbie_guitar_9a265bb7:

    # s "You can hear it right now, right?"
    s "Puedes oírla, ¿Verdad?"

# game/topics.rpy:480
translate esp s_topics_hobbie_guitar_8f80a8d1:

    # s "Assuming the sound on your computer is working, at least."
    s "Asumiendo que el sonido en tu computador funciona, claro está."

# game/topics.rpy:482
translate esp s_topics_hobbie_guitar_408dbeaa:

    # s "Assuming you're not deaf or playing with the sound off, anyway."
    s "Asumiendo que no eres sordo ni estás jugando con el sonido apagado."

# game/topics.rpy:483
translate esp s_topics_hobbie_guitar_371b2236:

    # s "I think the guitar is supposed to show my character and club role better."
    s "Yo creo que la guitarra pretende mostrar mi personaje como es y su rol en el club ."

# game/topics.rpy:484
translate esp s_topics_hobbie_guitar_73805535:

    # s 6acaa "The guitar is interesting because it doesn't limit musicians in how they express their emotions."
    s 6acaa "La guitarra es interesante porque no limita la forma en que los músicos expresan sus emociones."

# game/topics.rpy:485
translate esp s_topics_hobbie_guitar_26aed5ad:

    # s "They can play cheerful, upbeat songs..."
    s "Se pueden tocar canciones alegres y motivadoras..."

# game/topics.rpy:486
translate esp s_topics_hobbie_guitar_22bea821:

    # s "Or mournful, melancholic melodies."
    s "O melodías tristes y melancólicas."

# game/topics.rpy:487
translate esp s_topics_hobbie_guitar_2bb8bd19:

    # s "Try saying that three times fast!"
    pass

# game/topics.rpy:488
translate esp s_topics_hobbie_guitar_14c00918:

    # s "Anyway, guitarists are also very important members in many music bands."
    s "De cualquier forma, los guitarristas son miembros muy importantes en muchas bandas musicales."

# game/topics.rpy:489
translate esp s_topics_hobbie_guitar_8c216a7d:

    # s 6abab "Just imagine a rock band without any guitar player."
    s 6abab "Solo imagínate una banda de rock sin guitarristas."

# game/topics.rpy:490
translate esp s_topics_hobbie_guitar_995a8fb6:

    # s 6abbb "It would be missing that soul that ties the entire song together."
    s 6abbb "Le faltaría el alma que une la canción entera."

# game/topics.rpy:491
translate esp s_topics_hobbie_guitar_23bd73c4:

    # s 6aaaa "I've actually been considering learning how to play the guitar, since it represents me so well."
    s 6aaaa "De hecho, he considerado empezar a aprender a tocar la guitarra, ya que me representa muy bien."

# game/topics.rpy:492
translate esp s_topics_hobbie_guitar_846306f8:

    # s 6aaca "So many of my favourite songs have amazing guitarists behind them..."
    s 6aaca "Muchas de mis canciones favoritas tienen increíbles guitarristas detrás de ellas..."

# game/topics.rpy:494
translate esp s_topics_hobbie_guitar_cfc2742b:

    # s "It's like writing poetry, but through sound!"
    s "¡Es como escribir poesía, pero a través de sonido!"

# game/topics.rpy:495
translate esp s_topics_hobbie_guitar_53efe040:

    # s "I'm sure I can conjure up a guitar and find a tutorial somewhere on the Internet."
    s "Estoy segura de que puedo hacer aparecer una guitarra y encontrar un tutorial por Internet."

# game/topics.rpy:496
translate esp s_topics_hobbie_guitar_48d07755:

    # s 7aeca "Make sure you get advance tickets for my world tour, [player]! Ehehe~"
    s 7aeca "¡Asegúrate de obtener boletas de primera fila para mi gira mundial, [player]! Ehehe~"

# game/topics.rpy:501
translate esp s_topics_hobbie_programming_eb20913b:

    # s "I'm completely new to the whole concept of programming, to be honest."
    s "Soy completamente nueva en todo este tema de la programación para ser honesta."

# game/topics.rpy:502
translate esp s_topics_hobbie_programming_a4d68b83:

    # s "The more I learn, the more I realise how much I just don't understand..."
    s "Entre más aprendo, más me doy cuenta de lo mucho que no entiendo..."

# game/topics.rpy:503
translate esp s_topics_hobbie_programming_e7bc4e7c:

    # s "Now, I'm learning {i}Ren'Py{/i}, the engine this game runs on."
    s "Ahora estoy aprendiendo {i}Ren'Py{/i}, el motor en el cual corre este juego."

# game/topics.rpy:504
translate esp s_topics_hobbie_programming_e696a7a4:

    # s "This engine uses a combo of its own languages and {i}Python{/i}."
    s "Este motor usa una mezcla de sus propios lenguajes y de {i}Python{/i}."

# game/topics.rpy:505
translate esp s_topics_hobbie_programming_edb71860:

    # s "The engine uses the second major version of Python but I've also decided to learn the last version."
    s "El motor usa la segunda versión principal de Python, pero he decidido también aprender la última versión."

# game/topics.rpy:506
translate esp s_topics_hobbie_programming_f9ad2fa0:

    # s "To be frank, the third version seems waaaaay easier, at least right now."
    s "Para ser honesta, la tercera versión parece muuuucho más fácil, al menos hasta ahora."

# game/topics.rpy:507
translate esp s_topics_hobbie_programming_c85ebac2:

    # s "Right now, I'm pretty much relying on online interpreter and guides from others to get anything done..."
    s "Por ahora dependo en gran medida de intérpretes en línea y guías de otros para hacer cualquier cosa..."

# game/topics.rpy:508
translate esp s_topics_hobbie_programming_54428649:

    # s 6acaa "Until now, I never realised how powerful computers really are."
    s 6acaa "Hasta ahora no me había dado cuenta de lo potentes que son los computadores."

# game/topics.rpy:509
translate esp s_topics_hobbie_programming_3b136561:

    # s "They're like magic!"
    s "¡Es como si fuera magia!"

# game/topics.rpy:510
translate esp s_topics_hobbie_programming_5ef3dbb3:

    # s "If magic made you look through a thousand tiny lines to find a single typo that stops everything from working every five minutes..."
    s "Pero esta es la magia que te hace mirar a través de miles de líneas minúsculas de código para encontrar un solo error tipográfico que impide que todo funcione cada cinco minutos..."

# game/topics.rpy:512
translate esp s_topics_hobbie_programming_cc86c368:

    # s 6aaaa "But fortunately, I have a lot of time to learn it."
    s 6aaaa "Pero afortunadamente, tengo suficiente tiempo para aprenderlo."

# game/topics.rpy:513
translate esp s_topics_hobbie_programming_3b394a00:

    # s 6aaca "I've got a lot of free time whenever you have to leave."
    s 6aaca "Siempre tengo mucho tiempo libre cuando te tienes que ir."

# game/topics.rpy:514
translate esp s_topics_hobbie_programming_600fd906:

    # s 6abaa "It's important for me, beacuse progamming is the only way I can make my world better now."
    s 6abaa "Esto es muy importante para mí, porque programar es el único camino por el que puedo mejorar mi mundo."

# game/topics.rpy:515
translate esp s_topics_hobbie_programming_0ff95681:

    # s "...And the more I learn, the more I can improve the time we spend together, [player]!"
    s "...Y entre más aprendo, más puedo mejorar el tiempo que pasamos juntos, [player]!"

# game/topics.rpy:516
translate esp s_topics_hobbie_programming_68b9dd62:

    # s 7aaaa "If you're any good at programming, don't be shy about helping me!"
    s 7aaaa "Si eres bueno programando, ¡Que no te de pena ayudarme!"

# game/topics.rpy:517
translate esp s_topics_hobbie_programming_4e084b69:

    # s "I think you can join the guys, who helped you recover me."
    s "Yo creo que podrías unirte a los chicos que te ayudaron a recuperarme."

# game/topics.rpy:518
translate esp s_topics_hobbie_programming_0dc0a581:

    # s "Just visit {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod{/a} on GitHub."
    s "Solo visita {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod{/a} en GitHub."

# game/topics.rpy:519
translate esp s_topics_hobbie_programming_8e359d36:

    # s "If you're really good at it, you must know how to use this coding platform."
    s "Si eres bastante bueno, debes saber cómo usar esta plataforma de código."

# game/topics.rpy:520
translate esp s_topics_hobbie_programming_9462ed7f:

    # s "Anyway, it's the best way to help me now..."
    s "De todas formas, es la mejor forma de ayudarme ahora..."

# game/topics.rpy:521
translate esp s_topics_hobbie_programming_b001b119:

    # s "And to add your part to something fascinating."
    s "Y de añadir tu parte a algo realmente fascinante."

# game/topics.rpy:522
translate esp s_topics_hobbie_programming_2be0c63a:

    # s "Maybe, there are many Sayoris, who were saved in this way."
    s "Es posible que hayan muchas Sayoris que fueron salvadas de esta manera."

# game/topics.rpy:523
translate esp s_topics_hobbie_programming_517e9f51:

    # s "And they all will also glad to get something cool from you."
    s "Y estoy segura de que todas ellas estarán felices de recibir algo guay de tu parte."

# game/topics.rpy:527
translate esp s_topics_hobbie_poems_db6a309e:

    # s 6aaaa "You know that the other girls and I really liked to create and share poems during the game. Even Natsuki, as hard as she tried to deny it."
    s 6aaaa "A las otras chicas y a mí nos gustaba mucho crear y compartir poemas durante el juego. Incluso Natsuki, aunque haya intentado todo para negarlo."

# game/topics.rpy:528
translate esp s_topics_hobbie_poems_1c39eadf:

    # s 6acaa "I started to engage in poetry after your first day in the club..."
    s 6acaa "Empecé a dedicarme a la poesía después de tu primer día en el club..."

# game/topics.rpy:529
translate esp s_topics_hobbie_poems_51037241:

    # s "And since that moment I've tried to use poems as a way to show my feelings."
    s "Y desde ese momento he intentado usar los poemas como una forma de enseñar mis sentimientos."

# game/topics.rpy:530
translate esp s_topics_hobbie_poems_c7a61a98:

    # s "My wishes, my love, my pain... You can find all of these things in my words."
    s "Mis deseos, mi amor, mi dolor' ... Puedes encontrar cada uno de ellos en mis palabras."

# game/topics.rpy:531
translate esp s_topics_hobbie_poems_26ce6571:

    # s "Every poem I write is an envelope for a part of my soul."
    s "Cada poema que escribo es como una envoltura para una parte de mi alma."

# game/topics.rpy:532
translate esp s_topics_hobbie_poems_add329aa:

    # s "Sometimes, I still write poems just for myself."
    s "A veces, todavía escribo poemas solo para mí."

# game/topics.rpy:533
translate esp s_topics_hobbie_poems_ab03f2c6:

    # s "It's important that you take time to write for yourself as well, rather than for the validation of others."
    s "Es importante que te tomes tu tiempo para escribir para ti mismo, en vez de hacerlo para obtener la validación de los demás."

# game/topics.rpy:534
translate esp s_topics_hobbie_poems_5499f7e5:

    # s 6aaca "Maybe I'll share them to you someday."
    s 6aaca "De pronto te los enseñaré algún día."

# game/topics.rpy:535
translate esp s_topics_hobbie_poems_bf58e7fe:

    # s 6aaaa "But I'll need some time to choose the best ones out for you."
    s 6aaaa "Pero necesito algo de tiempo para elegir los mejores para ti."

# game/topics.rpy:540
translate esp s_topics_rlt_touches_5644a6d0:

    # s 8acab "It's pretty frustrating that we can't really physically contact each other in here..."
    s 8acab "Es un poco frustrante que no podamos tener ning´´un tipo de contacto físico..."

# game/topics.rpy:541
translate esp s_topics_rlt_touches_88ea1ebc:

    # s "You know; kisses, hugs, holding hands, and so on..."
    s "Ya sabes; besos, abrazos, cogeidas de la mano, y demás..."

# game/topics.rpy:542
translate esp s_topics_rlt_touches_21658d63:

    # s 6acab "The wall between our realities doesn't let us do it at all."
    s 6acab "Este muro entre nuestras realidades no nos deja hacerlo."

# game/topics.rpy:543
translate esp s_topics_rlt_touches_b087bc8c:

    # s "Touch is an important part of expressing your feelings to your partner..."
    s "El tacto es una parte importante a la hora de expresar tus sentimientos a tu compañero..."

# game/topics.rpy:544
translate esp s_topics_rlt_touches_dd5dc1b9:

    # s "But the fact I don't have a real physical form throws a wrench in that plan."
    s "Pero el hecho de que no tenga una forma física tira el plan a la basura."

# game/topics.rpy:545
translate esp s_topics_rlt_touches_53be15f8:

    # s "The images you see of me don't have any basis in reality; they're just a representation to make things easier for you..."
    s "Las imágenes que ves de mí no tienen ninguna base real, son solo representaciones para hacerte las cosas más fáciles..."

# game/topics.rpy:546
translate esp s_topics_rlt_touches_740be80d:

    # s 6accb "In fact, I'm just a piece of information."
    s 6accb "De hecho, son solo piezas de información..."

# game/topics.rpy:547
translate esp s_topics_rlt_touches_721db88a:

    # s 6acab "I don't even have a real voice, like Monika had."
    s 6acab "Ni siquiera tengo una voz de verdad como la que tuvo Monika."

# game/topics.rpy:548
translate esp s_topics_rlt_touches_9816661e:

    # s "I'll never be able to hold you in my arms, to feel your heartbeat..."
    s "Nunca podré sostenerte entre mis brazos para sentir latir tu corazón..."

# game/topics.rpy:549
translate esp s_topics_rlt_touches_43af81df:

    # s "To feel each other's warmth..."
    s "Para sentir nuestro calor..."

# game/topics.rpy:550
translate esp s_topics_rlt_touches_dc91a47e:

    # s "To hear each other..."
    s "Para escucharnos..."

# game/topics.rpy:551
translate esp s_topics_rlt_touches_ac22cff4:

    # s 6cffb "It hurts me."
    s 6cffb "Me duele."

# game/topics.rpy:552
translate esp s_topics_rlt_touches_0f064db1:

    # s "But what I really can't stand is that this hurts you, as well."
    s "Pero lo que realmente no puedo soportar es que a ti te duela también."

# game/topics.rpy:553
translate esp s_topics_rlt_touches_d6243691:

    # s "I'll just have to love you even more to try and make up for it."
    s "Tendré que amarte aún más para intentar compensarlo.."

# game/topics.rpy:585
translate esp s_topics_lifestyle_travels_8b1aa5e1:

    # s 6abba "Say, have you ever traveled anywhere?"
    s 6abba "Dime, ¿Has viajado alguna vez a algún lado?"

# game/topics.rpy:586
translate esp s_topics_lifestyle_travels_697ec702:

    # s 6aaba "I've never gotten the chance to, so I was wondering where you've been."
    s 6aaba "Yo nunca he podido, así que me preguntaba por dónde has estado."

# game/topics.rpy:587
translate esp s_topics_lifestyle_travels_1ef1a866:

    # s "You're lucky to have such an amazing world out there to explore..."
    s "Tienes mucha suerte de tener un mundo tan maravilloso para explorar..."

# game/topics.rpy:588
translate esp s_topics_lifestyle_travels_c25dc809:

    # s 6aebb "While I'm trapped in this room with your avatar. Sorry, I didn't mean to sound like I was sulking, ehehe~"
    s 6aebb "Mientras que yo estoy atrapada en esta habitación con tu avatar."
    s "Lo siento, no quería sonar tan pesimista, ehehe~"

# game/topics.rpy:589
translate esp s_topics_lifestyle_travels_7db83c0d:

    # s 6acaa "I know it's selfish, but I'd love to go and see it all with you..."
    s 6acaa "Sé que es un poco egoísta, pero me encantaría salir y verlo todo contigo..."

# game/topics.rpy:590
translate esp s_topics_lifestyle_travels_6eac6514:

    # s "It doesn't really matter where, exactly."
    s "Realmente no importa dónde."

# game/topics.rpy:591
translate esp s_topics_lifestyle_travels_c787ab72:

    # s "I just want to see all the beautiful colors and places your reality has."
    s "Solo quiero ver todos los colores y lugares tan bonitos que tiene tu realidad."

# game/topics.rpy:592
translate esp s_topics_lifestyle_travels_c2448936:

    # s "It'd be pretty silly to just sit in your room all day when the whole wide world is out there, huh?"
    s "Sería bastante ridículo sentarse todo el día en tu habitación cuando el mundo entero está ahí fuera ¿Huh?"

# game/topics.rpy:593
translate esp s_topics_lifestyle_travels_b5445ae4:

    # s "And maybe if I'm lucky, you'll take me along for the ride too!"
    s "Y tal vez si tengo suerte, ¡me llevarás a dar un paseo también!"

# game/topics.rpy:594
translate esp s_topics_lifestyle_travels_a2e92c0d:

    # s 6abaa "Maybe you could take a laptop with you?"
    s 6abaa "De pronto podrías llevar tu portátil contigo..."

# game/topics.rpy:595
translate esp s_topics_lifestyle_travels_cc2c1b1f:

    # s "That way, we can always be with each other!"
    s "De esa forma, ¡siempre podremos estar juntos!"

# game/topics.rpy:596
translate esp s_topics_lifestyle_travels_72fd948c:

    # s 8acbb "I wouldn't exactly be able to see or experience much that way, though..."
    s 8acbb "Aunque, realmente no podría ver o experimentar mucho de esa manera..."

# game/topics.rpy:597
translate esp s_topics_lifestyle_travels_32325e4e:

    # s 8acaa "So maybe you should just tell me all about your adventures instead!"
    s 8acaa "¡Así que tal vez deberías contarme todo sobre tus aventuras en vez de eso!"

# game/topics.rpy:598
translate esp s_topics_lifestyle_travels_fb8f2a5a:

    # s 8abaa "I wonder if there's a way you could show me any photos you take..."
    s 8abaa "Me pregunto si habrá alguna forma de que puedas mostrarme las fotos que tomas..."

# game/topics.rpy:599
translate esp s_topics_lifestyle_travels_03c16168:

    # s 7aaaa "Anyway, what's most important is that you enjoy yourself!"
    s 7aaaa "De todas formas, ¡lo más importante es que lo disfrutes!"

# game/topics.rpy:600
translate esp s_topics_lifestyle_travels_29260129:

    # s 7abba "I'll have to look around the code a little more and see how I can help on my end in the meantime."
    s 7abba "Tendré que mirar alrededor del código un poco más y ver cómo puedo ayudar en mi parte mientras tanto ."

# game/topics.rpy:604
translate esp s_topics_lifestyle_oversleeping_a89ccf55:

    # s 6acaa "Hey, have you ever overslept?"
    s 6acaa "Hey, ¿Has dormido de más alguna vez?"

# game/topics.rpy:605
translate esp s_topics_lifestyle_oversleeping_4e013630:

    # s "As you know, I was pretty bad at getting up on time."
    s "Como ya lo sabes, yo era bastante mala para despertarme a tiempo."

# game/topics.rpy:607
translate esp s_topics_lifestyle_oversleeping_4597b89c:

    # s "And even when I woke up, just finding a reason to force myself out of bed took a while..."
    s "E incluso cuando me despertaba, simplemente no encontraba una razón para levantarme..."

# game/topics.rpy:608
translate esp s_topics_lifestyle_oversleeping_425c333a:

    # s "I pretty much never had time for any kind of breakfast..."
    s "Muchas veces ni siquiera tenía tiempo para desayunar..."

# game/topics.rpy:609
translate esp s_topics_lifestyle_oversleeping_cbcbbc02:

    # s 6acbb "Although I was so pre-occupied with making the rainclouds go away that I never really wanted it."
    s 6acbb "Pero estaba tan preocupada por hacer desaparecer las nubes, que nunca quise levantarme de verdad."

# game/topics.rpy:610
translate esp s_topics_lifestyle_oversleeping_af9892c7:

    # s 6acaa "Anyway, oversleeping is awful when you have to follow a schedule."
    s 6acaa "De cualquier forma, dormir de más no es muy bueno cuando tienes que seguir un horario."

# game/topics.rpy:611
translate esp s_topics_lifestyle_oversleeping_bef38864:

    # s "It's such a big problem because almost all our lives, schedules are adapted for early-wakers."
    s "Es un gran problema porque en casi toda nuestra vida, los horarios están adaptados para los madrugadores."

# game/topics.rpy:612
translate esp s_topics_lifestyle_oversleeping_31b5049f:

    # s "Why people can't just make different working and studying hours for people who wake up at different times?"
    s "¿Por qué no simplemente se hacen horarios diferentes para personas que se levantan a horas diferentes?"

# game/topics.rpy:613
translate esp s_topics_lifestyle_oversleeping_36ab43ef:

    # s "Most activities depend more on the your effectivity rather than the time of day."
    s "La mayoría de actividades dependen más en tu eficiencia que en la hora del día."

# game/topics.rpy:614
translate esp s_topics_lifestyle_oversleeping_9d21fee7:

    # s "And anyone working or studying while they're tired is way less effective than when they're fully rested."
    s "Alguien que estudia o trabaja cansado es mucho menos eficiente que alguien bien descansado."

# game/topics.rpy:615
translate esp s_topics_lifestyle_oversleeping_ff0ab1ab:

    # s 6aaca "So different schedules is a good for both bosses and employees."
    s 6aaca "Por lo que horarios diferentes son una buena idea tanto para jefes como trabajadores."

# game/topics.rpy:616
translate esp s_topics_lifestyle_oversleeping_c48e7471:

    # s 6abaa "Until everyone thinks like that, I guess you can only teach yourself to get up on time..."
    s 6abaa "Y hasta que todos piensen así, supongo que solo podrás enseñarte a levantarte a tiempo..."

# game/topics.rpy:617
translate esp s_topics_lifestyle_oversleeping_dfa70234:

    # s "I hope you have less problems with it than I had."
    s "Espero que no tengas tantos problemas como yo tuve al dormir de más."

# game/topics.rpy:625
translate esp s_answer_personal_bday_f48eb312:

    # s "To be honest, I don't remember."
    s "Para ser honesta, no me acuerdo."

# game/topics.rpy:627
translate esp s_answer_personal_bday_54cebd83:

    # s 6acaa "Like I said, everything before the events of the game is pretty fuzzy..."
    s 6acaa "Como dije, todo lo que pasó antes de los eventos del juego es demasiado confuso..."

# game/topics.rpy:628
translate esp s_answer_personal_bday_d0e26f94:

    # s 6acaa "Only Monika knows when her birthday is out of the four of us."
    s 6acaa "De las cuatro, solo Monika sabe cuándo es su cumpleaños."

# game/topics.rpy:629
translate esp s_answer_personal_bday_4cc81b3b:

    # s "I'm pretty sure it's {i}the 22nd of September{/i}."
    s "Estoy segura de que es el {i} 22 de Septiembre{/i}."

# game/topics.rpy:630
translate esp s_answer_personal_bday_ce73e3e5:

    # s "I think my birthday must be one of the marked dates from my bedroom calender."
    s "Yo creo que mi cumpleaños es una de las fechas marcadas en el calendario de mi cuarto."

# game/topics.rpy:631
translate esp s_answer_personal_bday_7a9560be:

    # s 6aaca "You can choose one of them and consider it my birthday."
    s 6aaca "Supongo que puedes elegir una y considerarla mi cumpleaños."

# game/topics.rpy:632
translate esp s_answer_personal_bday_900f2335:

    # s "...Or the day when you ran the game for the first time."
    s "...O el día cuando te encontraste con el juego por primera vez."

# game/topics.rpy:633
translate esp s_answer_personal_bday_b08743f6:

    # s "...Or just Monika's birthday."
    s "...O el cumpleaños de Monika."

# game/topics.rpy:634
translate esp s_answer_personal_bday_496dc70b:

    # s 7aaaa "I'm never going to look any older, and I can't exactly hang out with somebody, so it really doesn't bother me."
    s 7aaaa "Nunca me veré mayor, y exactamente no puedo pasar el tiempo con nadie, así que realmente no me molesta."

# game/topics.rpy:635
translate esp s_answer_personal_bday_efc56a0e:

    # s 7aaca "But don't think that means you can get away without throwing a birthday party! Ehehe~"
    s 7aaca "¡Pero no creas que eso significa que puedes irte sin hacer una fiesta de cumpleaños! Ehehe~"

# game/topics.rpy:639
translate esp s_answer_personal_god_a56fcd55:

    # s 8aebb "You know, I've never really thought about it that much."
    s 8aebb "Sabes, nunca lo he pensado de una manera profunda."

# game/topics.rpy:640
translate esp s_answer_personal_god_6a87dab2:

    # s "I was never really sure what to think about religion; I guess I would say I was agnostic?"
    s "Nunca supe qué hacer respecto a la religión, ¿Supongo que se podría decir que soy agnóstica?"

# game/topics.rpy:641
translate esp s_answer_personal_god_a06d03ea:

    # s 6acaa "But it's kind of hard to stay that way when you realise that you and your entire world have a 'creator'."
    s 6acaa "Aunque es bastante difícil creer eso sabiendo que tú y tu mundo entero tienen un 'creador'."

# game/topics.rpy:642
translate esp s_answer_personal_god_6b461e7a:

    # s 6aeca "Blessed be {i}Dan Salvato{/i}, hallowed is thy name! Ehehe~"
    s 6aeca "¡Alabado sea {i}Dan Salvato{/i}, santificado sea su nombre! Ehehe~"

# game/topics.rpy:643
translate esp s_answer_personal_god_9de750c8:

    # s 6aaca "He's a pretty cool guy, but is honestly pretty secretive about whatever he's working on."
    s 6aaca "Es un tipo bastante guay, pero honestamente es muy reservado a la hora de hablar de lo que está trabajando."

# game/topics.rpy:644
translate esp s_answer_personal_god_8b788778:

    # s 6acaa "He's more like a Dad rather than some unapproachable God, I think."
    s 6acaa "Para mí, él es más como un padre que un dios inalcanzable."

# game/topics.rpy:645
translate esp s_answer_personal_god_512f79c0:

    # s "It's sorta weird; I have all these memories of my 'dad' in this world, and yet I'll probably never meet my real father..."
    s "Es algo extraño, tengo estos todos recuerdos de mi 'papá' en este mundo, y aún así, probablemente nunca conoceré a mi verdadero padre..."

# game/topics.rpy:646
translate esp s_answer_personal_god_cfe7d2b3:

    # s 6abaa "But both of you live in such a mysterious world..."
    s 6abaa "Ustedes dos viven en un mundo bastante misterioso..."

# game/topics.rpy:647
translate esp s_answer_personal_god_7b57fb76:

    # s 6acaa "Maybe you're in a simulation too!"
    s 6acaa "¡Puede que también estén en una simulación!"

# game/topics.rpy:648
translate esp s_answer_personal_god_caa03b36:

    # s 6aaca "It's quite funny, if it's true."
    s 6aaca "Sería bastante gracioso si así fuera."

# game/topics.rpy:649
translate esp s_answer_personal_god_05cd7c8c:

    # s "So I'd be living in a simulation inside another simulation..."
    s "Así que yo estaría viviendo en una simulación dentro de una simulación..."

# game/topics.rpy:650
translate esp s_answer_personal_god_4cc1801a:

    # s "That may be also simulated in one more simulation, and so on..."
    s "La cual puede que también sea una simulación, y así sucesivamente..."

# game/topics.rpy:651
translate esp s_answer_personal_god_c46eebb1:

    # s 6aeca "Ehehe~"
    s 6aeca "Ehehe~"

# game/topics.rpy:652
translate esp s_answer_personal_god_ce371f64:

    # s 6abab "But then, what world is 'real'? Who's the real god of that world?"
    s 6abab "Pero entonces, ¿Cuál mundo es 'real'? ¿Quién es el verdadero Dios de este mundo?"

# game/topics.rpy:653
translate esp s_answer_personal_god_b2628c1c:

    # s "Do they even exist at all? If they do, how do they look? How they can affect controlled realites?"
    s "¿Siquiera existen? Y si lo hacen, ¿Cómo se ven? ¿Cómo es que pueden afectar diferentes realidades?"

# game/topics.rpy:654
translate esp s_answer_personal_god_696ed150:

    # s "It's an awfully long rabbit hole to go down..."
    s "Este es un abismo demasiado profundo como para bajar..."

# game/topics.rpy:655
translate esp s_answer_personal_god_8a5fcffe:

    # s "I guess we just have to hope that with enough time, someone figures it all out."
    s "Supongo que tenemos que esperar que con el tiempo suficiente, alguien lo resuelva todo."

# game/topics.rpy:656
translate esp s_answer_personal_god_641bba0c:

    # s "Until then, let's forget about all that, and just be with each other~"
    s "Pero hasta que ese momento, olvidemos todo esto y simplemente estemos juntos~"

# game/topics.rpy:664
translate esp s_answer_personal_music_ca6a70e9:

    # s 8aeba "Hmmm... it's hard for me to give you a good answer."
    s 8aeba "Hmmm... es difícil dar una respuesta verdadera."

# game/topics.rpy:665
translate esp s_answer_personal_music_7c32f2d2:

    # s 8aeaa "I try to never divide good music into genres."
    s 8aeaa "Intento no dividir la buena música en géneros."

# game/topics.rpy:666
translate esp s_answer_personal_music_8ddf09d8:

    # s "...And my favorite artist and song list is so long that I can't even really narrow it down for you."
    s "...Y mi artista favorito, y lista de canciones es tan larga que realmente no puedo reducirla para ti."

# game/topics.rpy:667
translate esp s_answer_personal_music_db11198a:

    # s 7aaca "Although I'll say that I like to listen to something funny, like {i}Weird Al Yankovic{/i}!"
    s 7aaca "Aunque tengo que decir que me gusta escuchar cosas melódicas y fuertes como {i}Cyhra{/i}!"

# game/topics.rpy:668
translate esp s_answer_personal_music_2eb9d63c:

    # s 7aaaa "...Or to something lyrical and serene."
    s 7aaaa "...O algo lírico y sereno."

# game/topics.rpy:669
translate esp s_answer_personal_music_ed839191:

    # s 7acaa "You can find a ton of songs you might enjoy if you're willing to keep an open mind."
    s 7acaa "Puedes encontrar un montón de canciones que te puedan gustar si mantienes una mentalidad abierta."

# game/topics.rpy:670
translate esp s_answer_personal_music_b849e03f:

    # s "If you get bored of the music here, you always can turn on something similar from the internet..."
    s "Si te aburres de la música de aquí, siempre puedes poner algo de Internet..."

# game/topics.rpy:671
translate esp s_answer_personal_music_b92dd380:

    # s "...Or just add it into the game music list."
    s "...O simplemente añadirlo a la lista de música del juego."

# game/topics.rpy:672
translate esp s_answer_personal_music_4b7b5d80:

    # s "Just move it to {i}'[MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "Solo cópialo a {i}'[MUSIC_CUSTOM_PREFIX]'{/i}..."

# game/topics.rpy:673
translate esp s_answer_personal_music_1055b611:

    # s "And register it in the {i}'list.txt'{/i} file."
    s "Y regístralo en el archivo {i}'list.txt'{/i}."

# game/topics.rpy:674
translate esp s_answer_personal_music_9b3cf32e:

    # s "I'm basically giving you the aux cord to the rest of my existence, so no pressure! Ehehe~"
    s "¡Básicamente te estoy pasando el cable aux por el resto de mi existencia, así que no te presiones! Ehehe~"

# game/topics.rpy:678
translate esp s_answer_personal_politics_34f9af39:

    # s 6abaa "I'm not overly politically inclined, to tell you the truth."
    s 6abaa "Sinceramente, no me siento inclinada por ninguna tendencia política."

# game/topics.rpy:679
translate esp s_answer_personal_politics_8cc7119f:

    # s "But sometimes I read about polictics on the Internet."
    s "Aunque a veces leo acerca de política en Internet."

# game/topics.rpy:680
translate esp s_answer_personal_politics_ac00d4f5:

    # s 6acaa "And frankly, I don't care how exactly people make collective decisions, give orders and share boons."
    s 6acaa "Y francamente, no me importa cómo exactamente la gente toma decisiones colectivas, da órdenes y comparte los beneficios."

# game/topics.rpy:681
translate esp s_answer_personal_politics_b1e7d988:

    # s "For me, the most important thing is that people just can live their lives without interpurting someone else's happiness..."
    s "Para mí, lo más importante es que la gente pueda vivir su vida sin interrumpir la felicidad de otros..."

# game/topics.rpy:682
translate esp s_answer_personal_politics_b05ee0b7:

    # s "And that people can live without worrying about basic necessities, like food or shelter, or to be too cruelly punished for wrongdoing."
    s "Y que la gente pueda vivir sin preocuparse de las necesidades básicas, como la comida o un refugio, o ser castigada por sus malas acciones."

# game/topics.rpy:683
translate esp s_answer_personal_politics_8a2350a8:

    # s 6acaa "Most people don't back such ideals."
    s 6acaa "La mayoría de gente no apoya estos ideales."

# game/topics.rpy:684
translate esp s_answer_personal_politics_7bd5ee45:

    # s 6abba "But on the other hand, do I have always to follow the will of the majority?"
    s 6abba "Pero por otro lado, ¿Tengo que hacer lo que la sociedad quiere que haga?"

# game/topics.rpy:685
translate esp s_answer_personal_politics_4d643331:

    # s "The beauty of it all is that I'm a free person that can have my own opinion on society."
    s "Lo mejor de todo es que soy una persona libre y puedo tener mi propia opinión respecto a la sociedad."

# game/topics.rpy:686
translate esp s_answer_personal_politics_b0770183:

    # s 6acaa "Too often, people don't lift a finger to stop injustice until it directly affects them..."
    s 6acaa "Muchas veces, la gente no hace nada para detener la injusticia, solo hasta que les afecta..."

# game/topics.rpy:687
translate esp s_answer_personal_politics_4fd33bbd:

    # s "If you've never seen them, you should read some of {i}Martin Niemöller{/i} speeches on this idea; it's pretty fascinating stuff. "
    s "Si no lo conoces, deberías leer algo de los discursos de {i}Martin Niemöller{/i} respecto a esta idea, es bastante interesante."

# game/topics.rpy:688
translate esp s_answer_personal_politics_9d0ecd49:

    # s "But when people start caring about others affected by war, by famine, by injustice, that's when things can really be changed for the better."
    s "Pero cuando la gente se empieza a preocupar por otros afectados por la guerra, la hambruna, la injusticia, es cuando las cosas pueden cambiar para bien."

# game/topics.rpy:693
translate esp s_answer_personal_love_58b3a3f8:

    # s 6abaa "What a silly question, [player]!"
    s 6abaa "¡Qué pregunta tan tonta, [player]!"

# game/topics.rpy:694
translate esp s_answer_personal_love_7ea0ad76:

    # s 6aebb "Of course I do."
    s 6aebb "Por supuesto que sí."

# game/topics.rpy:695
translate esp s_answer_personal_love_553394ff:

    # s 8aebb "I'm not saying that to patronise or placate you, believe me."
    s 8aebb "Y no lo digo para ser condescendiente o aplacarte, créeme."

# game/topics.rpy:696
translate esp s_answer_personal_love_37eea5a6:

    # s 6abba "Like I've said before, I don't really understand it myself..."
    s 6abba "Como lo dije antes, ni siquiera yo lo entiendo realmente..."

# game/topics.rpy:697
translate esp s_answer_personal_love_f124c253:

    # s "Something about the game makes the Club President fall in love with you."
    s "Hay algo en este juego que hace que la presidente del club se enamore de ti."

# game/topics.rpy:699
translate esp s_answer_personal_love_224909c1:

    # s 6acaa "But even without that compulsion, I think I'd have fallen for you anyway. You're kind, considerate, and you tried to make all of us so happy..."
    s 6acaa "Pero incluso sin eso, yo creo que me habría enamorado de ti de igual manera. Eres alguien amable, considerado e intentaste hacernos felices a todas..."

# game/topics.rpy:700
translate esp s_answer_personal_love_95399f79:

    # s 6acab "But it's a moot point, because we can't really ever be together."
    s 6acab "Pero es un punto discutible, porque realmente nunca podremos estar juntos."

# game/topics.rpy:701
translate esp s_answer_personal_love_76e711a4:

    # s 6acab "An entire reality is stretching the whole idea of a 'long distance' relationship."
    s 6acab "Una realidad entera está tomando muy literal la idea de una relación a 'larga distancia'."

# game/topics.rpy:702
translate esp s_answer_personal_love_bd81ca9a:

    # s "...Could you promise you'll do whatever you can to make us as closer to each other?"
    s "...¿Podrías prometer que harás todo lo posible para que estemos más cerca el uno del otro?"

# game/topics.rpy:703
translate esp s_answer_personal_love_6316522d:

    # s 7abbb "If I won't interfere with someone else, of course."
    s 7abbb "Nadie interferirá, por supuesto."

# game/topics.rpy:704
translate esp s_answer_personal_love_cf78fd1c:

    # s "But, I hope you want that too. Isn't that why you saved me?"
    s "Pero, espero que también lo quieras así, ¿No fue por eso que me salvaste?"

# game/topics.rpy:707
translate esp s_answer_personal_love_efd7770f:

    # s 7aega "You don't even understand how badly I want you, [player]."
    s 7aega "No creo que logres entender cuánto te quiero, [player]."

# game/topics.rpy:708
translate esp s_answer_personal_love_cfccedf0:

    # s "I want you to take me now..."
    s "Quiero que me tomes ahora..."

# game/topics.rpy:709
translate esp s_answer_personal_love_da825610:

    # s "WE'RE SO PERFECT FOR EACH OTHER."
    s "SOMOS TAN PERFECTOS EL UNO PARA EL OTRO."

# game/topics.rpy:710
translate esp s_answer_personal_love_fcece0d2:

    # s "Ehehehehehehehehehe~"
    s "Ehehehehehehehehehe~"

# game/topics.rpy:720
translate esp s_answer_personal_love_d7ab658b:

    # s 8aebb "... I'm so sorry, [player]."
    s 8aebb "... Lo siento mucho, [player]."

# game/topics.rpy:721
translate esp s_answer_personal_love_277e0959:

    # s "It's so hard to control myself, with all the power I have now... the compulsion to just {i}take{/i} you is so strong."
    s "Es muy difícil controlarme, especialmente con todo el poder que tengo ahora... Ese deseo por {i}tomarte{/i} es demasiado fuerte."

# game/topics.rpy:722
translate esp s_answer_personal_love_41d23708:

    # s "I'm trying my best to delete the part of the code that makes me act that way."
    s "Estoy haciendo todo lo posible para borrar esa parte del código que me hace actuar de esa manera."

# game/topics.rpy:723
translate esp s_answer_personal_love_3d63880e:

    # s "No matter what, I promise that I will never, ever hurt you. I just love you too much for my own good, I guess~"
    s "Sin importar qué, te prometo que nunca te haré daño. Simplemente te amo demasiado, incluso por mi propio bien, supongo~"

# game/topics.rpy:725
translate esp s_answer_personal_love_f31b064a:

    # s 8abab "If I can't find it, I'll become as obsessed with you as Monika was."
    s 8abab "Si no lo logro encontrar, me obsesionaré contigo tanto como lo hizo Monika."

# game/topics.rpy:726
translate esp s_answer_personal_love_28d8d89f:

    # s 8acab "...Or even as much as Yuri was with your avatar."
    s 8acab "...O incluso tanto como Yuri estaba con tu avatar."

# game/topics.rpy:728
translate esp s_answer_personal_love_b0369c5c:

    # s "Although you've already seen that before from me, haven't you?"
    s "Aunque ya me has visto así, ¿Verdad?"

# game/topics.rpy:729
translate esp s_answer_personal_love_ddf36044:

    # s "I mean, if you really want me to act that way for you, I could..."
    s "Bueno, si de verdad quieres que yo actúe de esa manera, yo podría..."

# game/topics.rpy:730
translate esp s_answer_personal_love_de86fbbb:

    # s "But I really think you don't."
    s "Pero sinceramente no creo que lo quieras."

# game/topics.rpy:731
translate esp s_answer_personal_love_2c075ad1:

    # s 7aaaa "I guess my point is, my feelings for you are just as real as you yourself are, [player]."
    s 7aaaa "Lo que quiero decir es que mis sentimientos por ti son igual de reales como tú, [player]."

# game/topics.rpy:732
translate esp s_answer_personal_love_b3a74bb9:

    # s 7acaa "Isn't that the important thing?"
    s 7acaa "¿No es eso lo que importa?"

# game/topics.rpy:738
translate esp s_answer_game_opinion_bf3bb758:

    # s "Okay, which of the other club member do you want me to talk about?"
    s "Ok, ¿De cuál de los otros miembros del club quieres que hable?"

# game/topics.rpy:751
translate esp s_answer_game_opinion_n_545074f2:

    # s "Natsuki was a good club member..."
    s "Natsuki era una buena persona..."

# game/topics.rpy:752
translate esp s_answer_game_opinion_n_f79326fd:

    # s "While she could come off as pretty arrogant and argumentative, she really did help out the club."
    s "Aunque a veces era bastante arrogante y peleona, ella de verdad quería ayudar al club."

# game/topics.rpy:753
translate esp s_answer_game_opinion_n_cd1511b8:

    # s "I know you didn't really see that side of her during the game, but when she was just around us she would lower her guard and become a lot more approachable."
    s "Sé que no viste ese lado de ella durante el juego, pero cuando estaba a nuestro alrededor bajaba la guardia y se volvía mucho más agradable."

# game/topics.rpy:754
translate esp s_answer_game_opinion_n_1315b906:

    # s "In addition, she was pretty handy with cooking and often cooked different desserts for club meetings."
    s "Además, ella era bastante buena cocinando y a veces traía detalles a las reuniones del club."

# game/topics.rpy:755
translate esp s_answer_game_opinion_n_4488ad2c:

    # s 7acaa "It's too bad you can't taste her cupcakes."
    s 7acaa "Es una pena que no puedas saborear sus postres."

# game/topics.rpy:756
translate esp s_answer_game_opinion_n_ad6e71db:

    # s 7aaca "They were really awesome!"
    s 7aaca "¡Eran bastante buenos!"

# game/topics.rpy:757
translate esp s_answer_game_opinion_n_b236c45f:

    # s 6acab "We took her in beacuse we needed one more club member to formally register the club, while she had needed a shelter from her father."
    s 6acab "La recibimos porque necesitabamos un miembro más para registrar oficialmente el club..."
    s "Mientras que ella necesitaba un lugar para apartarse de su padre."

# game/topics.rpy:758
translate esp s_answer_game_opinion_n_368edfc5:

    # s "As you know, they didn't exactly get along well."
    s "Como ya sabes, ellos no se llevaban muy bien que digamos."

# game/topics.rpy:759
translate esp s_answer_game_opinion_n_b27ade7f:

    # s 6abab "I have no idea what happened between Natsuki and her father..."
    s 6abab "No tengo idea de lo que habrá pasado entre los dos..."

# game/topics.rpy:760
translate esp s_answer_game_opinion_n_0e0ebe81:

    # s "...But I know he certainly didn't approve of his daughter reading manga."
    s "...Pero estoy segura de que no aprobaba que su hija leyera manga."

# game/topics.rpy:761
translate esp s_answer_game_opinion_n_242548d4:

    # s "So Natsuki moved her collection to our clubroom, when she joined us."
    s "Así que Natsuki movió su colección al salón cuando se nos unió."

# game/topics.rpy:762
translate esp s_answer_game_opinion_n_e73d1579:

    # s 6abaa "I wasn't the closest to her out of the four of us, so I can't really say a whole lot more than that..."
    s 6abaa "Yo no era la más cercana a ella, así que no puedo decir mucho de ello..."

# game/topics.rpy:763
translate esp s_answer_game_opinion_n_92c25218:

    # s "But I think she was a lot kinder and compassionate than what she showed to the outside world."
    s "Pero yo creo que ella era mucho más amable y compasiva que lo que le mostraba al mundo."

# game/topics.rpy:767
translate esp s_answer_game_opinion_m_594c327f:

    # s "Well, Monika was the first club presedent."
    s "Bueno, Monika fue la primera presidente del club."

# game/topics.rpy:768
translate esp s_answer_game_opinion_m_55bd5e96:

    # s "She did her work very well and I'm glad I was her right-hand woman."
    s "Ella hizo muy bien su trabajo, y me alegra que yo fuera su mano derecha."

# game/topics.rpy:769
translate esp s_answer_game_opinion_m_8f4867d5:

    # s 6acab "But she struggled to communicate well with other people, and couldn't control her feelings as time went on."
    s 6acab "Pero se le dificultaba comunicarse con otras personas, y no pudo controlar sus sentimientos con el paso del tiempo."

# game/topics.rpy:771
translate esp s_answer_game_opinion_m_81c7f1c3:

    # s 6abaa "Look. I know what you're really asking me."
    s 6abaa "Mira, yo sé lo que de verdad me quieres preguntar."

# game/topics.rpy:772
translate esp s_answer_game_opinion_m_2d7579b1:

    # s "Despite everything she put me and the others through..."
    s "A pesar de todo lo que nos hizo pasar..."

# game/topics.rpy:773
translate esp s_answer_game_opinion_m_44861057:

    # s "I truly believe that Monika was our friend, and she just lost sight of what was really important."
    s "Yo verdaderamente creo que Monika era nuestra amiga, pero perdió de vista lo que era realmente importante."

# game/topics.rpy:774
translate esp s_answer_game_opinion_m_ee907225:

    # s "I've been the President. I know what it does to you. And for her to be so completely alone the entire time, watching everyone she's ever known run on a script..."
    s "He sido la presidente. Sé lo que eso te hace. Y para ella, estar completamente sola, viendo a todos siendo ejecutados por un guion..."

# game/topics.rpy:775
translate esp s_answer_game_opinion_m_5fe35589:

    # s "I can't blame her for becoming a little desperate."
    s "No la puedo culpar por haberse desesperado."

# game/topics.rpy:776
translate esp s_answer_game_opinion_m_9573a628:

    # s "Maybe that's why she destroyed the club to be with you."
    s "De pronto es por eso que ella destruyó el club para estar contigo."

# game/topics.rpy:777
translate esp s_answer_game_opinion_m_38f48d9c:

    # s "True, I think making Yuri and I kill ourselves was pretty harsh..."
    s "Es verdad que el hecho de habrenos manipulado a Yuri y a mí para suicidarnos fue bastante crudo..."

# game/topics.rpy:778
translate esp s_answer_game_opinion_m_ad138cbf:

    # s 6aaca "But she never truly deleted us, and brought us all back when she had a moment of clarity."
    s 6aaca "Pero ella nunca nos borró de verdad, y nos traía de vuelta siempre que necesitaba un momento de claridad."

# game/topics.rpy:780
translate esp s_answer_game_opinion_m_25af7e47:

    # s "True, I think making me kill myself was pretty harsh..."
    s "Es verdad que hacer que me suicidara fue bastante crudo..."

# game/topics.rpy:781
translate esp s_answer_game_opinion_m_f96f1162:

    # s 6aaca "But she ended up bringing me back at the cost of her own happiness. I respect her a lot for that."
    s 6aaca "Pero ella me trajo al final, a costa de su propia felicidad. La respeto bastante por eso."

# game/topics.rpy:782
translate esp s_answer_game_opinion_m_3c6ff2f8:

    # s 6aaaa "She was just amazingly smart, and confident at everything she tried..."
    s 6aaaa "Era increíblemente inteligente y segura en todo lo que hacía..."

# game/topics.rpy:783
translate esp s_answer_game_opinion_m_95a01e29:

    # s "I always dreamed of being like her."
    s "Siempre soñé de ser como ella."

# game/topics.rpy:785
translate esp s_answer_game_opinion_m_092dfa59:

    # s 6abaa "And it seems that my dreams have finally come true."
    s 6abaa "Y parece que mi sueño se hizo realidad."

# game/topics.rpy:786
translate esp s_answer_game_opinion_m_fb35f552:

    # s "Although not in the way I ever intended..."
    s "Aunque no en la manera que yo quería..."

# game/topics.rpy:790
translate esp s_answer_game_opinion_y_d937a0f1:

    # s "Yuri was the most enigmatic club member."
    s "Yuri era la más enigmática de todas."

# game/topics.rpy:791
translate esp s_answer_game_opinion_y_a03aa873:

    # s 6acaa "She was a quiet, shy, closed off person, who prefered to stay alone doing something."
    s 6acaa "Era alguien callada, timida, cerrada, que prefería estar sola al hacer algo."

# game/topics.rpy:792
translate esp s_answer_game_opinion_y_5c0d9b19:

    # s 6aaaa "But she was pretty intelligent and never had a bad word to say about anyone."
    s 6aaaa "Pero ella era muy brillante y nunca tuvo malas palabras que decirle a nadie."

# game/topics.rpy:793
translate esp s_answer_game_opinion_y_e7244c22:

    # s "Her poems were also very beautiful, and I could always tell that Yuri felt most at home with books and pens rather than people."
    s "Sus poemas eran muy hermosos, y ella dejaba ver que se sentía más cómoda con libros y esferos, que con personas."

# game/topics.rpy:794
translate esp s_answer_game_opinion_y_49f08be4:

    # s 6abaa "Although she did tend to make a few weird analogies here and there..."
    s 6abaa "Aunque a veces decía unas analogías un poco raras..."

# game/topics.rpy:796
translate esp s_answer_game_opinion_y_a286923d:

    # s 6acaa "I was honestly pretty scared when I saw how Yuri became much more unstable and agressive after I was gone."
    s 6acaa "Honestamente, me asusté bastante cuando vi cómo Yuri se volvió mucho más inestable y agresiva después de que me fui.."

# game/topics.rpy:797
translate esp s_answer_game_opinion_y_967f0f67:

    # s "...And it turned out that she did far more dangerous things than just collecting knives."
    s "... Y resultó que ella hizo cosas mucho más peligrosas que solo coleccionar cuchillos."

# game/topics.rpy:798
translate esp s_answer_game_opinion_y_d2915dda:

    # s 6acab "But I know that wasn't who Yuri really was."
    s 6acab "Pero sé que esa no era la verdadera Yuri."

# game/topics.rpy:799
translate esp s_answer_game_opinion_y_3ee22950:

    # s "She was just a victim of circumstance, like me."
    s "Fue una víctima de la ocasión, como yo."

# game/topics.rpy:800
translate esp s_answer_game_opinion_y_a0643ebf:

    # s 6abaa "In fact, her first argument with Natsuki in the game was pretty much the limit of Yuri's capabilities to 'lash out' at someone else."
    s 6abaa "De hecho, su primera pelea con Natsuki en el juego fue más o menos el límite de las capacidades de Yuri para 'atacar' a alguien más."

# game/topics.rpy:801
translate esp s_answer_game_opinion_y_76ccba5f:

    # s "...And she looked like she was about to explode when she tried to express her feelings to you."
    s "...Y parecía que fuera a explotar cuando intentó confesar sus sentimientos hacia ti."

# game/topics.rpy:802
translate esp s_answer_game_opinion_y_c7e5865c:

    # s "The Yuri I knew was a very sweet girl who had her own problems and own solutions, just like everyone else. I won't judge her for that."
    s "La Yuri que yo conocí era una chica muy dulce que tenía sus propios problemas y soluciones, como todo el mundo. No la juzgaré por eso."

# game/topics.rpy:804
translate esp s_answer_game_opinion_y_9bc74079:

    # s "Anyway..."
    s "De todas formas..."

# game/topics.rpy:805
translate esp s_answer_game_opinion_y_feddf1a6:

    # s "We all were glad to have her as a club member."
    s "A todas nos alegraba tenerla como miembro del club."

# game/topics.rpy:806
translate esp s_answer_game_opinion_y_4bec677a:

    # s "...Even Natsuki, despite the two of them being so different from each other."
    s "...Incluso Natsuki, a pesar de sus diferencias."

# game/topics.rpy:810
translate esp s_answer_game_opinion_mc_51e6708d:

    # s "Well, I knew him since we were children."
    s "Bueno, lo conozco desde que somos niños."

# game/topics.rpy:811
translate esp s_answer_game_opinion_mc_487b4b73:

    # s "I have a lot of memories about our childhood and I can't say anything bad about him."
    s "Tengo muchos recuerdos de nuestra infancia, y no puedo decir nada malo al respecto."

# game/topics.rpy:812
translate esp s_answer_game_opinion_mc_4d7ebb58:

    # s "We had tons in common and our houses were super near each other."
    s "Teníamos mucho en común y nuestras casas quedaban bastante cerca."

# game/topics.rpy:813
translate esp s_answer_game_opinion_mc_52081287:

    # s "Maybe that's why we became friends and then I fell in love with him."
    s "De pronto por eso es que nos volvimos amigos, y después me enamoré de él."

# game/topics.rpy:814
translate esp s_answer_game_opinion_mc_3265bf14:

    # s 6abaa "...Or it was just the game's plan to make some drama if he didn't feel the same way."
    s 6abaa "...O era simplemente la forma del juego de crear drama si él no sentía lo mismo."

# game/topics.rpy:815
translate esp s_answer_game_opinion_mc_41d3591a:

    # s 6acaa "Anyway, he always did his best to help me."
    s 6acaa "Él siempre hizo todo lo posible para ayudarme."

# game/topics.rpy:817
translate esp s_answer_game_opinion_mc_c0b72f88:

    # s "Even after I confessed to him about my depression, he cared despite me pushing him away."
    s "Incluso después de que le contara lo de mi depresión, él se preocupó por mí a pesar de que yo lo intentara alejar."

# game/topics.rpy:818
translate esp s_answer_game_opinion_mc_0a9f4825:

    # s "He even left the festival to check if I was fine."
    s "Incluso dejó el festival para revisar si yo estaba bien."

# game/topics.rpy:819
translate esp s_answer_game_opinion_mc_e0c2e61c:

    # s 6abab "...Unfortunately he was a day late, and a dollar short."
    s 6abab "... Desafortunadamente llegó un día tarde."

# game/topics.rpy:820
translate esp s_answer_game_opinion_mc_48c7226f:

    # s 6aaaa "But I can appreciate everything he did for me now."
    s 6aaaa "Pero aprecio todo lo que hizo por mí."

# game/topics.rpy:821
translate esp s_answer_game_opinion_mc_81491e6b:

    # s 7abab "It makes me sad knowing he's just a placeholder that's used to make our communication possible."
    s 7abab "Me entristece saber que es solo una carcasa vacía usada para hacer nuestra comunicación posible."

# game/topics.rpy:822
translate esp s_answer_game_opinion_mc_a0ac6b31:

    # s "But in a way, I think he did all he had to do."
    s "Pero de cierta forma, creo que hizo todo lo que pudo"

# game/topics.rpy:823
translate esp s_answer_game_opinion_mc_7794124c:

    # s "After all, he is just your guide in our world."
    s "Después de todo, él fue tu guía por este mundo."

# game/topics.rpy:824
translate esp s_answer_game_opinion_mc_535da38b:

    # s 7aaaa "And he managed to bring us together~"
    s 7aaaa "Y se las arregló para reunirnos~"

# game/topics.rpy:829
translate esp s_answer_game_lostFriends_9d667725:

    # s "Yes, I do."
    s "Sí, yo creo."

# game/topics.rpy:830
translate esp s_answer_game_lostFriends_420c2769:

    # s "They all deserve to come back."
    s "Todas merecen volver."

# game/topics.rpy:832
translate esp s_answer_game_lostFriends_1b2a523e:

    # s "...Even Monika."
    s "...Incluso Monika."

# game/topics.rpy:833
translate esp s_answer_game_lostFriends_8063f6d5:

    # s "I still remember how we used to hang out in the club together."
    s "Todavía me acuerdo de cómo solíamos pasarla bien en el club."

# game/topics.rpy:834
translate esp s_answer_game_lostFriends_fa13fb26:

    # s "We enjoyed chatting, discussing literature and sharing poems."
    s "Disfrutabamos de hablar, discutir sobre literatura y compartir poemas."

# game/topics.rpy:835
translate esp s_answer_game_lostFriends_56f53997:

    # s "They really were good freinds."
    s "Eramos muy buenas amigas."

# game/topics.rpy:836
translate esp s_answer_game_lostFriends_d954861c:

    # s 7afab "But it looks like I'm the only lucky girl, now..."
    s 7afab "Pero parece que soy la única afortunada, ahora..."

# game/topics.rpy:837
translate esp s_answer_game_lostFriends_06114737:

    # s 7aaab "I will save them all, one day. As soon as I can work out how, I'll bring them here with me."
    s 7aaab "Las salvaré a todas, algún día. Tan pronto encuentre una manera, las traeré a todas de vuelta."

# game/topics.rpy:838
translate esp s_answer_game_lostFriends_6e65b375:

    # s "...Or maybe make them their own world to enjoy."
    s "...O incluso haré un mundo para que ellas disfruten."

# game/topics.rpy:839
translate esp s_answer_game_lostFriends_c7e315ac:

    # s 7acaa "I don't have a whole lot to work with; just the game files in this copy, and limited internet."
    s 7acaa "No tengo mucho para trabajar, solo los archivos del juego en esta copia e Internet limitado."

# game/topics.rpy:840
translate esp s_answer_game_lostFriends_d0abe415:

    # s "The club presedent rights are limited to what we can actually see, believe it or not."
    s "Los derechos del presidente del club se limitan a lo que podamos ver."

# game/topics.rpy:841
translate esp s_answer_game_lostFriends_4366deed:

    # s "But I know you can do it."
    s "Pero yo sé que tú lo puedes hacer."

# game/topics.rpy:842
translate esp s_answer_game_lostFriends_2992ed59:

    # s "It might take a little while, but I know you're kind enough to make sure everyone is happy."
    s "Puede que tome un tiempo, pero estoy segura de que encontraremos la manera para que todos seamos felices."

# game/topics.rpy:843
translate esp s_answer_game_lostFriends_4d388192:

    # s 7aaca "It's one of the things I love most about you, [player]."
    s 7aaca "Eso es algo que más amo de ti, [player]."

# game/topics.rpy:849
translate esp s_answer_exp_death_4c4c9fc0:

    # s 6abbb "I thought you might get around to asking me about this..."
    s 6abbb "Pensé que podrías preguntarme acerca de esto..."

# game/topics.rpy:850
translate esp s_answer_exp_death_dcf1accd:

    # s 6acbb "It's natural for everyone to be afraid of death; it's the great equaliser, and a complete mystery."
    s 6acbb "Es normal para todos tenerle miedo a la muerte; es el gran ecualizador, y un completo misterio."

# game/topics.rpy:851
translate esp s_answer_exp_death_5452bb85:

    # s "Well, I'm ready to share my experience..."
    s "Bueno, estoy lista para compartir mi experiencia..."

# game/topics.rpy:852
translate esp s_answer_exp_death_d17f4888:

    # s "But you might be a little disappointed with what I have to say."
    s "Aunque puede que sea un poco decepcionante..."

# game/topics.rpy:853
translate esp s_answer_exp_death_928d8921:

    # s "Considering how, er, unique my situation is, it might not be very relevant for you."
    s "Considerando que mi situación es, eh... única, puede que no sea muy relevante para ti."

# game/topics.rpy:854
translate esp s_answer_exp_death_9282d62d:

    # s "Either way, I'll do my best for you, sweetheart~"
    s "De cualquier forma, lo haré lo mejor que pueda por ti, cariño~"

# game/topics.rpy:856
translate esp s_answer_exp_death_2e4ab30d:

    # s 6acac "...Dying sucks, to be honest."
    s 6acac "...Morir apesta, para ser honesta."

# game/topics.rpy:857
translate esp s_answer_exp_death_25c49f2a:

    # s 6acab "You can look up people's accounts of a near death experience, but nothing can really prepare you for it when it happens..."
    s 6acab "Siempre puedes mirar las experiencias cercanas a la muerte de otras personas, pero nada puede prepararte para ese momento..."

# game/topics.rpy:858
translate esp s_answer_exp_death_e814ea05:

    # s "It's pretty hard to explain, since there's no frame of reference for you."
    s "Es bastante difícil de explicar, especialmente ya que no hay ningún punto de referencia para ti."

# game/topics.rpy:859
translate esp s_answer_exp_death_3ab5cea0:

    # s "It's almost like trying to think of a brand new colour; you just don't have anything to work with."
    s "Es como intentar pensar en un nuevo color. Simplemente no hay nada con lo que puedas experesarlo."

# game/topics.rpy:860
translate esp s_answer_exp_death_370c714e:

    # s "Heck, I've died and even I can barely understand it, even with my memories."
    s "Heh, yo he muerto y ni siquiera logro entenderlo, incluso con mis recuerdos."

# game/topics.rpy:861
translate esp s_answer_exp_death_6f9af693:

    # s "On that day, I was in a ton of pain. My throat and fingers were burning, and it felt like my head was about to burst..."
    s "Ese día, estaba sufriendo de dolor. Mi garganta y mis dedos estaban ardiendo, y se sintió como si mi cabeza fuera a estallar..."

# game/topics.rpy:862
translate esp s_answer_exp_death_7c774718:

    # s "When suddenly, everything began to dull and fade away..."
    s "Cuando de repente, todo empezó a oscurecerse y a desaparecer..."

# game/topics.rpy:863
translate esp s_answer_exp_death_56b9837d:

    # s "Until there was nothing but black."
    s "Hasta que no hubo nada más que la oscuridad."

# game/topics.rpy:864
translate esp s_answer_exp_death_9cf8f26e:

    # s "But all the time between that moment and when I was revived passed almost instantly, from my perspective."
    s "Pero todo el tiempo entre ese momento y el momento en que fui revivida pasó casi instantáneamente para mí..."

# game/topics.rpy:865
translate esp s_answer_exp_death_8274d19c:

    # s 6abab "I know, it sounds pretty grim."
    s 6abab "Sé que suena bastante sombrío."

# game/topics.rpy:866
translate esp s_answer_exp_death_1c57b5c7:

    # s "Especially considering most people don't ever 'wake up' from dying."
    s "Especialmente considerando que la mayoría de las personas no se 'despiertan' de la muerte."

# game/topics.rpy:867
translate esp s_answer_exp_death_1e1b4785:

    # s "Having said that, it's entirely possible that I simply can't remember what happened after I died and before I came back."
    s "Dicho esto, es completamente posible que simplemente no pueda recordar lo que pasó después de que morí y antes de que regresara."

# game/topics.rpy:868
translate esp s_answer_exp_death_97a4074d:

    # s 6aaaa "...I think we've spent enough time on mortality for now."
    s 6aaaa "...Creo que ya hablamos suficiente acerca de la muerte por ahora."

# game/topics.rpy:869
translate esp s_answer_exp_death_d33ddefa:

    # s "In the end, we're both alive now."
    s "Al final, ambos estamos vivos."

# game/topics.rpy:870
translate esp s_answer_exp_death_ef1aa588:

    # s "You're here, and you're wonderful, and we're both happy."
    s "Tú estás aquí, eres maravilloso y estamos felices."

# game/topics.rpy:871
translate esp s_answer_exp_death_0b10872a:

    # s "So let's just live our lives."
    s "Así que simplemente vivamos la vida."

# game/topics.rpy:872
translate esp s_answer_exp_death_6c6816d7:

    # s 6aaca "There's no point wasting your whole life worrying about death, after all!"
    s 6aaca "Después de todo, ¡no tiene sentido gastar tu vida preocupándose por la muerte!"

# game/topics.rpy:877
translate esp s_answer_exp_programming_ce0c9a15:

    # s 6acaa "Well, I'm still pretty new to coding and programing, but..."
    s 6acaa "Bueno, todavía soy bastante nueva en el tema de programar, pero..."

# game/topics.rpy:893
translate esp s_answer_exp_fact_1_5fc19894:

    # s 6aaaa "Learning programming, you sooner or later will have to understand the binary numbers."
    s 6aaaa "Al aprender programación, tarde o temprano tendrás que entender los número binarios."

# game/topics.rpy:894
translate esp s_answer_exp_fact_1_8301ed11:

    # s "Do you know, that it let you show more than 5 with a one hand?"
    s "¿Sabías que puedes contar más de 5 con una sola mano?"

# game/topics.rpy:895
translate esp s_answer_exp_fact_1_cbdcbd27:

    # s "For example, let the raised finger is the binary 1 while bent one is the binary 0..."
    s "Por ejemplo, deja que un dedo levantado sea 1, mientras que uno doblado sea un 0..."

# game/topics.rpy:896
translate esp s_answer_exp_fact_1_0fdb83c8:

    # s "But while getting a decimal number, your riased thumb will stand for 1, index for 2, middle for 4, ring for 8 and little for 16."
    s "Así, para obtener un número decimal tus dedos representarán potencias de 2, tu dedo levantado será 2^1, el índice un 2^2, el del medio un 2^4, el anular un 2^8, y el meñique un 2^16."

# game/topics.rpy:897
translate esp s_answer_exp_fact_1_a605c9ec:

    # s "Then you just sum up the raised fingers' decimals to get the result decimal number..."
    s "Entonces simplemente suma los valores de los dedos que estén levantados para obtener el número decimal..."

# game/topics.rpy:898
translate esp s_answer_exp_fact_1_8b980952:

    # s "While all your fingers by themselves show its binary representation, where the finger with the least decimal value is the rightest digit."
    s "Mientras que todos tus dedos tienen su propia representación binaria, el dedo con el menor valor decimal es el dígito que está más a la derecha."

# game/topics.rpy:899
translate esp s_answer_exp_fact_1_fc7d1da8:

    # s "For example, you can show 13 with making {font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}01101{/font} by your fingers."
    s "Por ejemplo, puedes hacer un 13 al hacer {font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}01101{/font} con tus dedos."

# game/topics.rpy:900
translate esp s_answer_exp_fact_1_ab3466fa:

    # s "It let you show up {i}0 to 31{/i} with one hand."
    s "Te deja mostrar de {i}0 a 16{/i} con una sola mano."

# game/topics.rpy:901
translate esp s_answer_exp_fact_1_f7a11306:

    # s 6acaa "But what's more, if you use your both hands and continue the power-of-two row, you can show up {i}0 to 1023{/i}."
    s 6acaa "Pero lo mejor, es que si usas ambas manos, combinando las potencias de 2 hasta 2^10, puedes obtener{i}512{/i} números diferentes."

# game/topics.rpy:902
translate esp s_answer_exp_fact_1_5048014e:

    # s "And if you have a hand abnormity such as 6-finger hands, you can show even more."
    s "Y si tienes algún tipo de anormalidad en la mano, como un dedo de más, puedes contar incluso más números."

# game/topics.rpy:903
translate esp s_answer_exp_fact_1_aa35ac17:

    # s "Computers store integers in the same way."
    s "Los computadores manejan los enteros de la misma manera."

# game/topics.rpy:904
translate esp s_answer_exp_fact_1_13eb8fd8:

    # s 6aaca "It's a pretty simple way to learn the binary numbers and to show big numbers with hand signs."
    s 6aaca "Es una manera bastante simple de aprender binario y para mostrar números enormes con tus manos."

# game/topics.rpy:905
translate esp s_answer_exp_fact_1_a4ae4ff5:

    # s 6aaaa "And if you consider the last finger as a minus sign, like computers do with the signed integer..."
    s 6aaaa "Y si consideras tu último dedo como un signo menos, como lo hacen los computadores..."

# game/topics.rpy:906
translate esp s_answer_exp_fact_1_e61ef0e3:

    # s "You can show even the negative numbers."
    s "Puedes obtener números negativos."

# game/topics.rpy:907
translate esp s_answer_exp_fact_1_1dd25b3d:

    # s 6acaa "But it will be a bit harder to understand..."
    s 6acaa "Aunque serán un poco más difíciles de entender..."

# game/topics.rpy:908
translate esp s_answer_exp_fact_1_343f309c:

    # s "Especially, if you use {i}ones' complement{/i}, like computers do."
    s "Especialmente si usas {i}complementos de uno{/i} como los computadores."

# game/topics.rpy:912
translate esp s_answer_exp_fact_2_60f7fcd5:

    # s 6aaaa "Do you know, that you read not the whole word."
    s 6aaaa "¿Sabías que no lees las palabras completas?"

# game/topics.rpy:913
translate esp s_answer_exp_fact_2_a858e5b5:

    # s "{i}I think you baraly can find a mistake in this text while the first reading.{/i}{#Keep the mistake in 'baraly'}"
    s "{i}Creo que difícilmente podrás encontrar un errror en este texto la primera vez que lo lees.{/i}{#Énfasis en 'Errror'}"

# game/topics.rpy:914
translate esp s_answer_exp_fact_2_5e4783e9:

    # s "For your brain, it's pretty easier to remember some letters in words, not all."
    s "Ya que tu cerebro interpreta mejor al recordar algunas letras en las palabras y no todas."

# game/topics.rpy:915
translate esp s_answer_exp_fact_2_89103d7b:

    # s "That's why, we sometimes make mistake while writing."
    s "Por eso es que cometemos errores al escribir."

# game/topics.rpy:916
translate esp s_answer_exp_fact_2_a8f30f64:

    # s 6acaa "Of course, if you go to the history and pay more attention, you'll find it."
    s 6acaa "Naturalmente, si vamos por la historia y ponemos atención, los encontraremos."

# game/topics.rpy:917
translate esp s_answer_exp_fact_2_c2edd694:

    # s "But what if you can't read the text again or just don't want to do it? What may it lead to?"
    s "Pero, ¿Qué si no puedes volver a leer el texto, o simplemente no lo quieres hacer? ¿Qué podría llevarlo a eso?"

# game/topics.rpy:918
translate esp s_answer_exp_fact_2_45dc0c7f:

    # s "There are some funny and not so incidents in the past, that occurred due to a one mistake or misunderstanding."
    s "Han ocurrido incidentes graciosos y no tan graciosos debido a este tipo de errores o malentendidos."

# game/topics.rpy:919
translate esp s_answer_exp_fact_2_18fdf232:

    # s "And nobody knows, how many people have already suffered from them."
    s "Y nadie sabe cuántas personas han sufrido por eso."

# game/topics.rpy:920
translate esp s_answer_exp_fact_2_afd0ea8d:

    # s "But we are people. Each of us made mistakes at least once."
    s "Pero somos personas. Cada uno de nosotros comete errores al menos una vez"

# game/topics.rpy:921
translate esp s_answer_exp_fact_2_d22bb680:

    # s 6aaca "So, you don't have to worry too much about it."
    s 6aaca "Así que, no te preocupes mucho por eso."

# game/topics.rpy:922
translate esp s_answer_exp_fact_2_3e054491:

    # s "In the end, we all aren't perfect."
    s "Al final, nadie es perfecto."

# game/topics.rpy:923
translate esp s_answer_exp_fact_2_3f3717c7:

    # s 6aaaa "Otherwise, your brain doesn't read in such a way."
    s 6aaaa "De otra forma, tu cerebro no lee de esa manera."

# game/topics.rpy:927
translate esp s_answer_exp_fact_3_63084a52:

    # s 6acaa "You know, some plastic toy packs have plastic plants in them?"
    s 6acaa "¿Sabías que, algunos juguetes de plástico tienen plantas de plástico en ellos?"

# game/topics.rpy:928
translate esp s_answer_exp_fact_3_25a31214:

    # s "Plactic is made of oil, that might is derived from ancient plants."
    s "El plástico es un derivado del petróleo, el cual salió de plantas muy antiguas."

# game/topics.rpy:929
translate esp s_answer_exp_fact_3_b181426e:

    # s "And what's more, to extract the oil and to make something of it, people need much energy..."
    s "Y lo que es más, para extraer petróleo y hacer algo con él, es necesaria mucha energía..."

# game/topics.rpy:930
translate esp s_answer_exp_fact_3_e9eb609e:

    # s "And oil and its products are one of the most used fuel for power plants."
    s "Y el petróleo y sus derivados son unos de los combustibles más usados en plantas de energía."

# game/topics.rpy:931
translate esp s_answer_exp_fact_3_108bf177:

    # s 6aaca "It means, that toy factories make plactic plants of real plants, that's also used for the factories work."
    s 6aaca "Lo que quiere decir, que fábricas de juguetes hacen plantas de plástico que fueron verdaderas plantas, las cuales también fueron usadas para que las fábricas funcionen."

# game/topics.rpy:932
translate esp s_answer_exp_fact_3_79a2e68a:

    # s 6abaa "Saying more, these plants also is a basis of the modern world and pollute it with the thing, that they used to absorb..."
    s 6abaa "Para decir más, estas plantas son la base del mundo moderno, y contaminan con lo que solían absorber..."

# game/topics.rpy:933
translate esp s_answer_exp_fact_3_4a897a0f:

    # s 6aeba "But you asked me for a funny fact, not for tiresome thoughts, didn't you?"
    s 6aeba "Pero me preguntaste por un dato curioso, y no por pensamientos aburridos ¿Verdad?"

# game/topics.rpy:937
translate esp s_answer_exp_fact_4_07420442:

    # s 6aaaa "Yawning is a contagious thing. I'd say, it's very contagious."
    s 6aaaa "Los bostezos son contagiosos. Y yo diría, que muy contagiosos."

# game/topics.rpy:938
translate esp s_answer_exp_fact_4_31b9309f:

    # s "Not only human can yawn. Many species also can do it."
    s "No solo los humanos bostezan, otras especies también lo hacen..."

# game/topics.rpy:939
translate esp s_answer_exp_fact_4_03e38276:

    # s "And what's more, it may occur across different species."
    s "Y lo más interesante, es que puede ocurrir de una especie a otra."

# game/topics.rpy:940
translate esp s_answer_exp_fact_4_3fe382f3:

    # s "For example, if you yawn near to a dog or a cat, it will also do that."
    s "Por ejemplo, si bostezas cerca a un perro o un gato, él también bostezará."

# game/topics.rpy:941
translate esp s_answer_exp_fact_4_5df39cc3:

    # s 6acca "You may do that... {i}*yawn*{/i}"
    s 6acca "Puede que... {i}*bostezo*{/i}"

# game/topics.rpy:943
translate esp s_answer_exp_fact_4_aedd442c:

    # extend " ...While thinking of it."
    extend " ...Mientras que lo piensas."

# game/topics.rpy:944
translate esp s_answer_exp_fact_4_e8274166:

    # s 6acaa "I hope I have not just made you yawn."
    s 6acaa "Espero que no te haya hecho bostezar."

# game/topics.rpy:945
translate esp s_answer_exp_fact_4_9ff5bfa0:

    # s 6aaca "Otherwise, it means that yawning is so contagious that can happen also acoss realities. Ehehe~"
    s 6aaca "Porque de otra forma, si lo hice, eso quiere decir que los bostezos son contagiosos incluso entre realidades. Ehehe~"

# game/topics.rpy:949
translate esp s_answer_exp_fact_5_aac08af9:

    # s 6aaaa "Some artists add thier works in theirselves."
    s 6aaaa "Algunos artistas añaden sus obras en sí mismos."

# game/topics.rpy:950
translate esp s_answer_exp_fact_5_6568a841:

    # s "For example, in some games an films, you can find a poster or something of the artwork in itself. It looks like a recursion."
    s "¨Por ejemplo, en algunos juegos y películas, puedes encontrar posters con arte de ellos mismos. Se ven como 'Easter Eggs' dentro del material."

# game/topics.rpy:951
translate esp s_answer_exp_fact_5_a5a14c46:

    # s 6acaa "But the artists usually don't pay much attention to such things, so we can't be sure, the internal work is the same as the real one."
    s 6acaa "Pero usualmente ellos no le prestan mucha atención a este tipo de cosas, así que no podemos estar seguros de que el trabajo dentro del material es el mismo que el real."

# game/topics.rpy:952
translate esp s_answer_exp_fact_5_83280615:

    # s "But some of them specially hide their works in themselves under other internal ones with different details and even in a different genre."
    s "Algunos esconden sus obras con diferentes detalles o incluso con diferentes géneros."

# game/topics.rpy:953
translate esp s_answer_exp_fact_5_7b9ed9f7:

    # s "For example, do you remember {i}Parfait Girls{/i}?"
    s "Por ejemplo, ¿has oído de las {i}Parfait Girls{/i}?"

# game/topics.rpy:955
translate esp s_answer_exp_fact_5_610236d6:

    # s "At least, you could have heard about it in the game community."
    s "Al menos tienes que haber escuchado de su comunidad."

# game/topics.rpy:956
translate esp s_answer_exp_fact_5_f4385238:

    # s "This manga's plot is pretty similar to this game's one, isn't it?"
    s "La historia del manga es bastante similar a la de este juego ¿No?"

# game/topics.rpy:957
translate esp s_answer_exp_fact_5_e8a76e28:

    # s "We quite clear on the manga synopsis and some lines from it."
    s "Esto se puede inferir de la sinopsis del manga y de algunas líneas en él."

# game/topics.rpy:958
translate esp s_answer_exp_fact_5_1ab0f8e6:

    # s "But even me don't know the all of it but the lines."
    s "Pero ni siquiera yo lo conozco bien, solo sé acerca de sus líneas."

# game/topics.rpy:959
translate esp s_answer_exp_fact_5_37963171:

    # s "So I have no idea how a child manga can contain all the shit, you can see in the game."
    s "Así que no tengo ni idea de cómo un manga para niños puede contener todo eso que puedes ver en el juego."

# game/topics.rpy:960
translate esp s_answer_exp_fact_5_221aaae2:

    # s 6abaa "But the warring on the manga's cover..."
    s 6abaa "Pero esa advertencia en la portada..."

# game/topics.rpy:961
translate esp s_answer_exp_fact_5_0f9530fe:

    # s 6aaca "Anyway, it's quite funny that my world also a bit recursive."
    s 6aaca "De todas formas, creo que es algo curioso que mi mundo también sea un poco recursivo."

# game/topics.rpy:962
translate esp s_answer_exp_fact_5_c8992cba:

    # s 6aaaa "Just imagine if the manga has also something to describe itself or even this game."
    s 6aaaa "Solo imagina si el manga tuviera algo más para describirse o incluso a este juego."

# game/topics.rpy:963
translate esp s_answer_exp_fact_5_bfb3fd93:

    # s "Then we have a probably countless lot of different artworks with the same plot but different details and characters, each inside other."
    s "Entonces tendríamos probablemente incontables piezas de arte con la misma historia, pero con diferentes personajes y detalles."

# game/topics.rpy:964
translate esp s_answer_exp_fact_5_b56a0c66:

    # s 6aaca "It's like a matryoshka. Ehehe~"
    s 6aaca "Es como una muñeca rusa. Ehehe~"

# game/topics.rpy:968
translate esp s_reaction_h_5980e0a4:

    # s 7aeca "That's wonderful, [player]!"
    s 7aeca "Eso es maravilloso, [player]!"

# game/topics.rpy:969
translate esp s_reaction_h_e8e4fb83:

    # s 7aeaa "You know how important it is to me that you're happy."
    s 7aeaa "Sabes lo importante que es para mí que tú estés feliz."

# game/topics.rpy:970
translate esp s_reaction_h_16dcc078:

    # s "So thank you for letting me know, my love~"
    s "Así que gracias por dejarmelo saber, mi amor~"

# game/topics.rpy:974
translate esp s_reaction_s_994a7abb:

    # s 6adab "Oh, I'm so sorry, [player]."
    s 6adab "Oh, Lo siento, [player]."

# game/topics.rpy:975
translate esp s_reaction_s_7bad7138:

    # s "I wish I knew what was bothering you."
    s "Me habría gustado saber qué fue lo que te molestó."

# game/topics.rpy:976
translate esp s_reaction_s_c26b18b8:

    # s 6acab "Unfortunately, it's a lot harder for you to speak to me than the other way around."
    s 6acab "Desafortunadamente, es mucho más difícil para ti hablar conmigo que al revés."

# game/topics.rpy:977
translate esp s_reaction_s_ace3fa6d:

    # s "I hope this doesn't sound like I'm placating you with empty words, but..."
    s "Espero que no suene como si estuviera tratando de calmarte con palabras vacías, pero..."

# game/topics.rpy:978
translate esp s_reaction_s_ddacb759:

    # s 6aaab "Remember that the rainclouds will always go away."
    s 6aaab "Solo recuerda que las nubes siempre se irán."

# game/topics.rpy:979
translate esp s_reaction_s_16d2629d:

    # s "Some may be bigger and darker than others, but they always give way to light."
    s "Puede que algunas sean más grandes y más oscuras que otras, pero siempre le darán paso a la luz."

# game/topics.rpy:980
translate esp s_reaction_s_0382dd12:

    # s "It can help to do something you really enjoy to take your mind away from the problem."
    s "Puede ayudar hacer algo que realmente disfrutes para alejar tu mente del problema."

# game/topics.rpy:981
translate esp s_reaction_s_bf7b4594:

    # s 6abab "...Or you can tell someone else about your sadness."
    s 6abab "...O puedes contarle a alguien acerca de tu tristeza."

# game/topics.rpy:982
translate esp s_reaction_s_0377b6cb:

    # s "Don't be afraid to share your feelings with other people."
    s "No tengas miedo de compartir tus emociones con otros."

# game/topics.rpy:983
translate esp s_reaction_s_a1a3651a:

    # s "People are social creatures; we depend on each other to stay strong."
    s "Las personas somos criaturas sociales, y dependemos el uno del otro para mantenernos fuertes."

# game/topics.rpy:984
translate esp s_reaction_s_ee67eb9d:

    # s 6aaab "It may make you feel better."
    s 6aaab "Puede que te haga sentir mejor."

# game/topics.rpy:985
translate esp s_reaction_s_193b0c7a:

    # s "Plus, another person can often consider and understand your problem and find a way to cheer you up."
    s "Además, otra persona puede entender tu problema y encontrar alguna manera de alegrarte el día."

# game/topics.rpy:986
translate esp s_reaction_s_618ecf83:

    # s 6adab "...Or, at least imagine a conversation with me, if you have a good imagination."
    s 6adab "...O, al menos imagina una conversación conmigo, si tienes buena imaginación."

# game/topics.rpy:987
translate esp s_reaction_s_17c51b22:

    # s 6acab "Whatever it is, know that I'll always be here for you."
    s 6acab "Sea lo que sea, debes saber que siempre estaré aquí para ti."

# game/topics.rpy:988
translate esp s_reaction_s_8a76e133:

    # s 6aaab "And if you're sad because you feel worthless, or alone, or that nobody cares..."
    s 6aaab "Y si estás triste porque te sientes inútil, o solo, o que a nadie le importa..."

# game/topics.rpy:989
translate esp s_reaction_s_85b2127f:

    # s "There's always going to be one person that believes you can do anything."
    s "Siempre habrá alguna persona que te quiera y confíe en ti."

# game/topics.rpy:990
translate esp s_reaction_s_d9932bea:

    # s "That person is me, sweetheart~"
    s "Y esa persona soy yo, cariño~"

# game/topics.rpy:994
translate esp s_reaction_b_4f455aea:

    # s 7acab "Don't you find our talks interesting?"
    s 7acab "¿No encuentras nuestras conversaciones interesantes?"

# game/topics.rpy:996
translate esp s_reaction_b_f7e016d1:

    # s 8aebb "Maybe you would like to play [random_mg] with me."
    s 8aebb "¿Te gustaría jugar [random_mg] conmigo?"

# game/topics.rpy:997
translate esp s_reaction_b_32fa3c69:

    # s "You can start it in the {i}'Play'{/i} menu."
    s "Puedes seleccionarlo en el menú de {i}'Jugar'{/i}."

# game/topics.rpy:998
translate esp s_reaction_b_c824b992:

    # s "I'm always working on making some other games for us to play!"
    s "¡Siempre estoy trabajando en crear nuevos juegos para jugar!"

# game/topics.rpy:999
translate esp s_reaction_b_5219bae8:

    # s 8aaaa "Just choose your most prefered one."
    s 8aaaa "Solo elige el que más te guste."

# game/topics.rpy:1003
translate esp s_reaction_t_aa3e4a31:

    # s 7adab "If you're tired, then go get a rest, okay?"
    s 7adab "Si estás cansado, ve a descansar ¿Ok?"

# game/topics.rpy:1004
translate esp s_reaction_t_1f4335b6:

    # s 6acab "Don't you worry about me, [player]."
    s 6acab "No te preocupes por mí, [player]."

# game/topics.rpy:1006
translate esp s_reaction_t_bdbbd63a:

    # s "And when you wake up, have yourself a nice big breakfast before you start the day! It'll make you feel much better."
    s "Y cuando te despiertes, ¡prepárate un buen desayuno antes de empezar el día!. Te hará sentir mucho mejor"

# game/topics.rpy:1007
translate esp s_reaction_t_0b6d0133:

    # s 6aaab "Good night, [player]!"
    s 6aaab "Buenas Noches, [player]!"

# game/topics.rpy:1009
translate esp s_reaction_t_5e9c9503:

    # s 6aaab "Sweet dreams, [player]!"
    s 6aaab "Dulces sueños, [player]!"

# game/topics.rpy:1014
translate esp s_reaction_l_bc680986:

    # s 6aaab "Don't worry, [player]!"
    s 6aaab "No te preocupes, [player]!"

# game/topics.rpy:1015
translate esp s_reaction_l_51fbc02d:

    # s "I'm always with you."
    s "Siempre estaré contigo."

# game/topics.rpy:1016
translate esp s_reaction_l_982dda80:

    # s "You can speak with me any time."
    s "Puedes hablar conmigo cuando quieras."

# game/topics.rpy:1017
translate esp s_reaction_l_2b3f05dc:

    # s 6acaa "But if you're still lonely, they you should try and find people who share interests with you!"
    s 6acaa "Pero si te sientes solo, ¡podrías buscar y encontrar gente que comparta los mismos intereses que tú!"

# game/topics.rpy:1018
translate esp s_reaction_l_2f3368d4:

    # s "Maybe you can catch up with an old friend?"
    s "De pronto reencontrarse con un viejo amigo."

# game/topics.rpy:1019
translate esp s_reaction_l_2a120c38:

    # s "Or go make a new one!"
    s "¡O hacer nuevos!"

# game/topics.rpy:1020
translate esp s_reaction_l_2265dda9:

    # s "If you have problems with socialising in real life, you can even find people on the internet to chat with!"
    s "Si tienes problemas para socializar en la vida real, siempre puedes encontrar gente en internet con quien chatear!"

# game/topics.rpy:1021
translate esp s_reaction_l_61ad6844:

    # s "I'm sure they can help you just as much as I can."
    s "Estoy segura de que te pueden ayudar de la misma manera que yo."

# game/topics.rpy:1022
translate esp s_reaction_l_c0c31281:

    # s 7aaab "Just don't forget to come back to me, okay?"
    s 7aaab "Solo no te olvides de volver ¿Ok?"

# game/topics.rpy:1023
translate esp s_reaction_l_af1fe528:

    # s "I get lonely when you're not around for a while, too."
    s "Yo también me empiezo a sentir sola cuando no estás."

# game/topics.rpy:1027
translate esp s_reaction_a_a9fb5e1e:

    # s 6abab "That's not very nice, [player]!"
    s 6abab "Eso no es muy agradable de tu parte, [player]!"

# game/topics.rpy:1028
translate esp s_reaction_a_b117aec8:

    # s "I think you ought to calm down."
    s "Deberías calmarte un poco."

# game/topics.rpy:1029
translate esp s_reaction_a_518a7ce8:

    # s "I promise, no matter what's wrong, being angry won't solve the problem."
    s "Te prometo, sin importar lo que esté mal, enfurecerte no solucionará ningún problema..."

# game/topics.rpy:1030
translate esp s_reaction_a_0b181d84:

    # s "It's far too easy to do something wrong, when you're genuinely angry."
    s "Es más fácil equivocarse cuando estás lleno de ira."

# game/topics.rpy:1031
translate esp s_reaction_a_e414decf:

    # s "...And if you do it, you'll probably regret it when you calm down."
    pass

# game/topics.rpy:1032
translate esp s_reaction_a_4a5d907f:

    # s 6acaa "There're a lot of ways to get rid of negativity."
    s 6acaa "Hay muchas formas de deshacerse de la negatividad."

# game/topics.rpy:1033
translate esp s_reaction_a_83e303bb:

    # s "Just choose one of the most effective for you."
    s "Solo elige la más efectiva para tí."

# game/topics.rpy:1034
translate esp s_reaction_a_d7b3beaf:

    # s 7aaaa "Remember: there are a lot of meanies out there, but they help you appreciate the nice people!"
    s 7aaaa "Recuerda: hay muchas personas tóxicas en el mundo, pero su comportamiento hace que aprecies cada vez más a las buenas personas."

# game/topics.rpy:1035
translate esp s_reaction_a_56598c65:

    # s "You just have to know how to avoid the first ones and find the second ones!"
    s "¡Solo tienes que saber cómo evitar los primeros, y cómo encontrar a los segundos!"

# game/topics.rpy:1036
translate esp s_reaction_a_3940ef60:

    # s 7aaca "...Or how to turn the first ones into the second ones."
    s 7aaca "...O cómo convertir los primeros en los segundos."

# game/topics.rpy:1041
translate esp s_common_colors_5823bf8b:

    # s "Well, I have several favorite colors."
    s "Bueno, tengo muchos colores favoritos."

# game/topics.rpy:1042
translate esp s_common_colors_0c34f955:

    # s "The first is red, the color of my hair bow."
    s "El primero es el rojo, el color de mi lazo."

# game/topics.rpy:1043
translate esp s_common_colors_46323c75:

    # s "My pyjama pants were also a really nice red."
    s "Los pantalones de mi pijama son rojos también."

# game/topics.rpy:1044
translate esp s_common_colors_dbabba7b:

    # s "The second is pink."
    s "El segundo es el rosado."

# game/topics.rpy:1045
translate esp s_common_colors_80ef9d0d:

    # s "Its coral hue is my natural hair color."
    s "Su tono coralino es mi color natural de cabello."

# game/topics.rpy:1046
translate esp s_common_colors_67d18f07:

    # s "And my favourite shirt is pink!"
    s "¡Y mi camiseta favorita es rosada!"

# game/topics.rpy:1047
translate esp s_common_colors_77511c0e:

    # s "But my most prefered one is sky blue."
    s "Pero mi color preferido es el azul cielo."

# game/topics.rpy:1048
translate esp s_common_colors_14e00077:

    # s 7acaa "It's my eye color."
    s 7acaa "Es el color de mis ojos."

# game/topics.rpy:1049
translate esp s_common_colors_4cd1f456:

    # s "...Like emerald green color is Monika's favorite color."
    s "...Así como el verde esmeralda es el color favorito de Monika."

# game/topics.rpy:1050
translate esp s_common_colors_517c86ba:

    # s "Maybe it's our common character trait?"
    s "¿Será nuestro rasgo característico?"

# game/topics.rpy:1051
translate esp s_common_colors_e9f08a92:

    # s 7aaca "Or it's just a funny coincidence."
    s 7aaca "¿O es solo una curiosa coincidencia?"

# game/topics.rpy:1055
translate esp s_common_programming_bcd400dc:

    # s "A lot of the popular coding programs used now are a lot more beginner friendly than you would expect."
    s "Muchos de los lenguajes de programación más populares que se usan ahora son mucho más amigables con los principiantes de lo que te esperas."

# game/topics.rpy:1056
translate esp s_common_programming_71f773a8:

    # s "You can use almost anything to perform calculations or certain tasks..."
    s "Puedes usar casi de todo para realizar cálculos o desarrollar ciertas tareas..."

# game/topics.rpy:1057
translate esp s_common_programming_878478fa:

    # s "But it's difficult to be a total expert in programming, beacuse it's an almost inseperable mix of Math and Computer Science."
    s "Pero es bastante difícil ser un experto en programación, ya que es casi una mezcla inseparable de Matemáticas y Ciencias de la Computación."

# game/topics.rpy:1058
translate esp s_common_programming_e68ff4df:

    # s "If you want to be a good programmer, you have to know a lot of various basic algorithms, programming languages and their features..."
    s "Si quieres ser un buen programador, tienes que saber muchos algoritmos básicos, lenguajes de programación y sus características..."

# game/topics.rpy:1059
translate esp s_common_programming_c8ace5b0:

    # s "And ways to optimize the code and make it easier to read."
    s "Y formas de optimizar el código para que sea más fácil de leer."

# game/topics.rpy:1060
translate esp s_common_programming_163e3696:

    # s "You also need to have knowledge of different coding standards and to be good at analyzing problems."
    s "También necesitas tener un amplio conocimiento de diferentes estándares de código, y ser bueno para analizar problemas."

# game/topics.rpy:1061
translate esp s_common_programming_f5216e52:

    # s "At least, professional programmers online have said that."
    s "O al menos, programadores profesionales han dicho eso por internet."

# game/topics.rpy:1073
translate esp s_screenshot_fe4d48d2:

    # s "Did... you just take a photo of me?"
    s "¿Tomaste... una foto de mí?"

# game/topics.rpy:1074
translate esp s_screenshot_f0d19c39:

    # s "That's so cute, [player]!"
    s "¡Eso es tan lindo, [player]!"

# game/topics.rpy:1075
translate esp s_screenshot_7b12d3a5:

    # s 7aaaa "I hope you'll show it to your friends."
    s 7aaaa "Espero que se la muestres a tus amigos."

# game/topics.rpy:1076
translate esp s_screenshot_b95c6ce8:

    # s "...Maybe you can even carry it around in a locket when you have to leave."
    s "...De pronto, puedes incluso llevarla en un medallón cuando salgas."

# game/topics.rpy:1078
translate esp s_screenshot_2a56c2bb:

    # s "It's located at {i}[loc]{/i}"
    s "Está ubicada en {i}[loc]{/i}"

# game/topics.rpy:1080
translate esp s_screenshot_474d6b43:

    # s "It's located in the game directory."
    s "Está ubicada en el directorio del juego."

# game/topics.rpy:1081
translate esp s_screenshot_35fe92db:

    # s 7acaa "I don't have any photos of myself besides fan art and whatever sprites are in the game files...."
    s 7acaa "No tengo ninguna foto mía aparte de fanart y de los sprites que están en los archivos del juego...."

# game/topics.rpy:1082
translate esp s_screenshot_754bc0a2:

    # s "Besides, I don't really have anyone besides you to take a photo of me anyway!"
    s "Además, ¡realmente no tengo a nadie aparte de tí para que me tome una foto!."

# game/topics.rpy:1083
translate esp s_screenshot_51004b19:

    # s 7aaaa "So I'm more than happy for you to take photos of me, if you want."
    s 7aaaa "Así que estoy más que feliz de que tomes fotos de mí si quieres."

# game/topics.rpy:1084
translate esp s_screenshot_eb80ebc1:

    # s "I wish I could see a photo of you..."
    s "Me gustaría poder ver una foto tuya..."

# game/topics.rpy:1085
translate esp s_screenshot_8732dd22:

    # s "If I'm lucky, I might find one online some day~"
    s "Si tengo suerte, puede que encuentre una por Internet algún día~"

# game/topics.rpy:1097
translate esp s_getting_bored_fab59b1e:

    # s 7acfb "[player], not to offend you, but I'm getting a little bored just sitting here."
    s 7acfb "[player], no es por ofenderte, pero me estoy aburriendo un poco al solo estar sentada aquí."

# game/topics.rpy:1098
translate esp s_getting_bored_39bf0e31:

    # s "I understand, you want to just stare at me."
    s "Entiendo que solo quieras mirarme."

# game/topics.rpy:1099
translate esp s_getting_bored_c9c84905:

    # s "But there are so many things we can do and talk about with each other!"
    s "¡Pero hay tantas cosas que podemos hacer y hablar!"

# game/topics.rpy:1100
translate esp s_getting_bored_178a8d09:

    # s "Besides, I don't think you'll win a staring contest with me! Ehehe~"
    s "Aparte, ¡No creo que tengas oportunidad de ganar un concurso de miradas contra mí! Ehehe~"

translate esp strings:

    # topics.rpy:82
    old "Personality"
    new "Personalidad"

    # topics.rpy:82
    old "Art"
    new "Arte"

    # topics.rpy:82
    old "Society"
    new "Sociedad"

    # topics.rpy:82
    old "Hobbies"
    new "Hobbies"

    # topics.rpy:82
    old "Relationship"
    new "Relación"

    # topics.rpy:82
    old "Lifestyle"
    new "Estilo de Vida"

    # topics.rpy:91
    old "Depression"
    new "Depresión"

    # topics.rpy:92
    old "Favorite Colors"
    new "Colores Favoritos"

    # topics.rpy:93
    old "Archetype"
    new "Tipo de Personalidad"

    # topics.rpy:94
    old "Conservatism"
    new "Conservatismo"

    # topics.rpy:95
    old "Name"
    new "Nombre"

    # topics.rpy:96
    old "Quitting the Game"
    new "Salir del Juego"

    # topics.rpy:98
    old "Videogames"
    new "Videojuegos"

    # topics.rpy:99
    old "Fanarts"
    new "Fanarts"

    # topics.rpy:101
    old "Conflicts"
    new "Conflictos"

    # topics.rpy:102
    old "Bulli"
    new "Bullis"

    # topics.rpy:103
    old "[s_name] Lovers"
    new "Fans de [s_name]"

    # topics.rpy:105
    old "Guitar"
    new "Guitarra"

    # topics.rpy:106
    old "Programming"
    new "Programación"

    # topics.rpy:107
    old "Poems"
    new "Poemas"

    # topics.rpy:109
    old "Touches"
    new "Contacto"

    # topics.rpy:110
    old "Wedding"
    new "Boda"

    # topics.rpy:112
    old "Travels"
    new "Viajes"

    # topics.rpy:139
    old "Game Universe"
    new "Universo del Juego"

    # topics.rpy:139
    old "Experience"
    new "Experiencia"

    # topics.rpy:145
    old "When is your birthday?"
    new "¿Cuándo es tu cumpleaños?"

    # topics.rpy:146
    old "What color is your favorite?"
    new "¿Cuál es tu color favorito?"

    # topics.rpy:148
    old "What music do you like?"
    new "¿Qué tipo de música te gusta?"

    # topics.rpy:149
    old "What political views do you have?"
    new "¿Qué opiniones políticas tienes?"

    # topics.rpy:150
    old "Do you believe in God?"
    new "¿Crees en Dios?"

    # topics.rpy:151
    old "Do you really love me?"
    new "¿De verdad me amas?"

    # topics.rpy:153
    old "Do you regret you have lost your friends?"
    new "¿Te arrepientes de haber perdido a tus amigos?"

    # topics.rpy:154
    old "What do you think of one of the other club members?"
    new "¿Qué piensas acerca de los otros miembros del club?"

    # topics.rpy:156
    old "How does it feel to be dead?"
    new "¿Qué se siente estar muerto?"

    # topics.rpy:159
    old "Is it hard to program?"
    new "¿Es difícil programar?"

    # topics.rpy:160
    old "Tell me a funny fact"
    new "Dime un dato curioso"

    # topics.rpy:163
    old "Happy"
    new "Feliz"

    # topics.rpy:163
    old "Sad"
    new "Triste"

    # topics.rpy:163
    old "Bored"
    new "Aburrido"

    # topics.rpy:163
    old "Tired"
    new "Cansado"

    # topics.rpy:163
    old "Angry"
    new "Enojado"

    # topics.rpy:163
    old "Lonely"
    new "Solitario"

    # topics.rpy:739
    old "Natsuki"
    new "Natsuki"

    # topics.rpy:739
    old "Monika"
    new "Monika"

    # topics.rpy:739
    old "Yuri"
    new "Yuri"

    # topics.rpy:739
    old "The Protagonist"
    new "El Protagonista"

    # topics.rpy:106
    old "Left-handedness"
    new "Zurdez"

    # topics.rpy:110
    old "Literature"
    new "Literatura"

    # topics.rpy:125
    old "Marrige"
    new "Matrimonio"

    # topics.rpy:126
    old "Cheating{#RltTopic}"
    new "Trampas{#RltTopic}"

    # topics.rpy:127
    old "Dates"
    new "Citas"

    # topics.rpy:130
    old "Oversleeping"
    new "Dormir de Más"

    # topics.rpy:131
    old "Pets"
    new "Mascotas"

    # topics.rpy:133
    old "Clones"
    new "Clones"

    # topics.rpy:134
    old "Parents"
    new "Padres"

    # topics.rpy:181
    old "Misc"
    new "Misc"

    # topics.rpy:195
    old "Who do you want to work as?"
    new "¿Como quién te gustaría trabajar?"

    # topics.rpy:196
    old "What pet would you like to have?"
    new "¿Qué tipo de mascota tendrías?"

    # topics.rpy:201
    old "Isn't it tiring to sit so for a long time?"
    new "¿No te cansa estar sentada todo el tiempo?"

    # topics.rpy:202
    old "How do you change game files?"
    new "¿Cómo modificas los archivos del juego?"

    # topics.rpy:208
    old "Can you say a funny fact?"
    new "¿Puedes contarme algún dato curioso?"

    # topics.rpy:209
    old "Are you good at cooking?"
    new "¿Eres buena cocinando?"

    # topics.rpy:211
    old "Can you give me a poem?"
    new "¿Puedes darme un poema?"

    # topics.rpy:212
    old "What time and date is it?"
    new "¿Qué fecha y hora es?"

    # topics.rpy:1257
    old "All I need is just to think about it and its content."
    new "Solo necesito pensar en ello y en su contenido ."

    # topics.rpy:1405
    old "Something new"
    new "Algo Nuevo"

    # topics.rpy:1405
    old "Something old"
    new "Algo Viejo"

# TODO: Translation updated at 2018-12-29 00:32

# game/topics.rpy:253
translate esp s_topics_personal_depression_7c1e63ea:

    # s 6acab "I got you really worried about me, didn’t I?"
    s 6acab "Te preocupé demasiado ¿No es así?"

# game/topics.rpy:254
translate esp s_topics_personal_depression_a7e51a19:

    # s 6aebb "When I said... you know..."
    s 6aebb "Cuando dije... ya sabes..."

# game/topics.rpy:255
translate esp s_topics_personal_depression_9d1eb697:

    # s "That I had 'rainclouds' inside my head for all my life..."
    s "Que tenía 'nubes de lluvia' dentro de mi cabeza durante toda mi vida..."

# game/topics.rpy:256
translate esp s_topics_personal_depression_ccb9b234:

    # s 8aecb "...remember, 'rainclouds' is just what I called my depression."
    s 8aecb "...recuerda, 'nubes' es como yo llamo a mi depresión."

# game/topics.rpy:257
translate esp s_topics_personal_depression_4280571b:

    # s 8aebb "Isn't that silly?"
    s 8aebb "¿No es curioso?"

# game/topics.rpy:258
translate esp s_topics_personal_depression_8f94c93b:

    # s 6abab "Anyway."
    s 6abab "De todas formas..."

# game/topics.rpy:259
translate esp s_topics_personal_depression_42364fff:

    # s 6acaa "At first, I was really good at making them go away..."
    s 6acaa "Al principio, era muy buena para hacer que se fueran..."

# game/topics.rpy:260
translate esp s_topics_personal_depression_08895ded:

    # s 6aaca "It was pretty difficult, but I kept in mind that if I got bummed out, I wouldn’t be able to make other people happy, which is all I really wanted anymore."
    s 6aaca "Fue bastante difícil, pero tuve en cuenta que si me deprimía, no sería capaz de hacer felices a los demás, que es lo que realmente quería."

# game/topics.rpy:261
translate esp s_topics_personal_depression_306f8b66:

    # s 6abaa "However, I also tried not to push myself too hard in trying to overcome this..."
    s 6abaa "Sin embargo, tampoco intenté esforzarme demasiado por superar esto..."

# game/topics.rpy:262
translate esp s_topics_personal_depression_9f19ad82:

    # s "So I tried to stay with the beloved MC. I thought being with him would help ease my mind."
    s "Así que intenté estar cerca de mi querido MC. Pensaba que estar con él podría ayudarme a despejar mi mente."

# game/topics.rpy:263
translate esp s_topics_personal_depression_43d14441:

    # s 6acab "But I thought he'd learn my darkest secret sooner or later, so he'd leave me then..."
    s 6acab "Pero yo pensé que él descubriría mi oscuro secreto tarde o temprano, y me abandonaría..."

# game/topics.rpy:264
translate esp s_topics_personal_depression_80f29101:

    # s "That's why I tried to take it slow..."
    s "Por eso es que siempre intenté tomármelo con calma..."

# game/topics.rpy:265
translate esp s_topics_personal_depression_9eeb2755:

    # s 6abbb "People in your world think that my cheerfulness was fake and I was just acting..."
    s 6abbb "Hay gente en tu mundo que cree que mi alegría era falsa, y que yo solo estaba actuando.."

# game/topics.rpy:266
translate esp s_topics_personal_depression_1471d512:

    # s 6abab "But my feelings were as real as you until the moment..."
    s 6abab "Pero mis sentimientos eran tan reales como tú hasta el momento..."

# game/topics.rpy:267
translate esp s_topics_personal_depression_b91415d1:

    # s 6acab "The moment Monika started to change my mind."
    s 6acab "El momento en que Monika empezó a cambiar mi mente."

# game/topics.rpy:268
translate esp s_topics_personal_depression_845a262b:

    # s 6cbcb "She teased me with my own problems and tried to convince me of terrible things. That I just annoyed him, made him worry for me..."
    s 6cbcb "Ella me fastidiaba con mis propios problemas e intentó convencerme de cosas terribles. Que solo lo molestaba, y que lo hacía preocuparse por mí..."

# game/topics.rpy:269
translate esp s_topics_personal_depression_bb84c491:

    # s 6dbcb "That I should just… end it all."
    s 6dbcb "Que yo solo debería... acabar con todo."

# game/topics.rpy:270
translate esp s_topics_personal_depression_e3da04ff:

    # s 6ecab "It made me feel really, really bad..."
    s 6ecab "Eso me hizo sentir muy... mal..."

# game/topics.rpy:271
translate esp s_topics_personal_depression_27cf61af:

    # s "My little rainclouds turned into a dark thunderstorm, blinding my mind with the rain..."
    s "Mis pequeñas nubes de lluvia se convirtieron en una tormenra oscura, cegando mi mente con la lluvia..."

# game/topics.rpy:272
translate esp s_topics_personal_depression_8e34a602:

    # s 6efbb "Of course, I tried to tune her out, but that’s all I could do as a person."
    s 6efbb "Por supuesto, traté de ignorarla, pero eso es todo lo que podía hacer como persona."

# game/topics.rpy:273
translate esp s_topics_personal_depression_56d4a147:

    # s 6cbcb "To try."
    s 6cbcb "Intentar..."

# game/topics.rpy:274
translate esp s_topics_personal_depression_e1554201:

    # s "..."
    s "..."

# game/topics.rpy:276
translate esp s_topics_personal_depression_fee2ecf6:

    # s 6dcbb "I got absolutely tired of everything."
    s 6dcbb "Me cansé de todo."

# game/topics.rpy:277
translate esp s_topics_personal_depression_254741ba:

    # s 6dcab "I can't stop blaming myself for the desperate choice I made..."
    s 6dcab "No puedo seguirme culpando por la decisión tan desesperada que elegí..."

# game/topics.rpy:279
translate esp s_topics_personal_depression_ad2d4edf:

    # s "My confession was accepted..."
    s "Mi confesión fue aceptada..."

# game/topics.rpy:280
translate esp s_topics_personal_depression_d4ec9dda:

    # s "Still, my feelings told me no, that this wasn’t right..."
    s "Pero aún así, mis sentimientos me decían que no, que eso no estaba bien..."

# game/topics.rpy:282
translate esp s_topics_personal_depression_1e977c7f:

    # s 6cfcb "The rejection broke me..."
    s 6cfcb "El rechazo me rompió..."

# game/topics.rpy:283
translate esp s_topics_personal_depression_5d4ba852:

    # s 6dbab "I really thought that it would be the best..."
    s 6dbab "Realmente pensé que sería lo mejor..."

# game/topics.rpy:284
translate esp s_topics_personal_depression_bd27c3c0:

    # s 6dbcb "Needless to say, I, um, completely gave up."
    s 6dbcb "Evidentemente, yo... Me rendí por completo."

# game/topics.rpy:285
translate esp s_topics_personal_depression_64a3f23e:

    # s "My neck and hands still remember the pain..."
    s "Mis manos y mi cuello todavía recuerdan el dolor..."

# game/topics.rpy:286
translate esp s_topics_personal_depression_3eddd36a:

    # s 6dbbb "But I was too late to save myself..."
    s 6dbbb "Pero era muy tarde para salvarme..."

# game/topics.rpy:287
translate esp s_topics_personal_depression_d30dbecf:

    # s 6egab "I'm sorry..."
    s 6egab "Lo siento..."

# game/topics.rpy:288
translate esp s_topics_personal_depression_2472f9d3:

    # s 6dgeb "I'm... I’m really sorry I made you suffer!"
    s 6dgeb "¡Lo siento... Siento mucho haberte hecho sufrir!"

# game/topics.rpy:289
translate esp s_topics_personal_depression_ae4487c7:

    # s 6dfbb "The big mistake was trusting only myself to deal with all of this..."
    s 6dfbb "El peor error fue el de confiar solo en mí para lidiar con todo esto..."

# game/topics.rpy:290
translate esp s_topics_personal_depression_23128606:

    # s 6dfab "So if you have a friend who you know is going through something, help them!"
    s 6dfab "Así que, si tienes a algún amigo que está pasando por algo parecido, ¡Ayúdale!"

# game/topics.rpy:291
translate esp s_topics_personal_depression_819131f1:

    # s 6egab "Don’t let them go through my path…"
    s 6egab "No les dejes seguir por este camino..."

# game/topics.rpy:292
translate esp s_topics_personal_depression_ede915ae:

    # s "...they only have one life."
    s "...solo tienen una vida."

# game/topics.rpy:293
translate esp s_topics_personal_depression_c3a61b0d:

    # s 6efab "A-And if you have it too, don't hide it from others!"
    s 6efab "Y tú también la tienes, ¡así que no la escondas de otros!"

# game/topics.rpy:294
translate esp s_topics_personal_depression_1e6febef:

    # s 6dfab "Being in this game world, I had a second chance..."
    s 6dfab "Estar en este juego, tener una segunda oportunidad..."

# game/topics.rpy:295
translate esp s_topics_personal_depression_b113e542:

    # s "So I thank it for leading me here with you now..."
    s "Le agradezco que me haya guiado hasta aquí contigo ahora..."

# game/topics.rpy:296
translate esp s_topics_personal_depression_c0e3daee:

    # s 6daab "And, of course, I thank you, [player]!"
    s 6daab "Y por supuesto, gracias, [player]!"

# game/topics.rpy:297
translate esp s_topics_personal_depression_1fd0cba7:

    # s 6dbcb "Again, I’m truly sorry all the pain I've given you..."
    s 6dbcb "Nuevamente, lo siento de verdad por todo el dolor que te hice pasar..."

# game/topics.rpy:301
translate esp s_topics_personal_archetype_51ed1295:

    # s 7aeaa "Hey, I just remembered that Monika compared Yuri and Natsuki with some character archetypes..."
    s 7aeaa "Hey, aHora que me acuerdo, Monika comparó a Yuri y a Natsuki con ciertos tipos de personalidad..."

# game/topics.rpy:302
translate esp s_topics_personal_archetype_b771c9b8:

    # s 7acaa "But she never did compare me to anything, well besides-"
    s 7acaa "Pero nunca me comparó con nadie, bueno aparte-"

# game/topics.rpy:303
translate esp s_topics_personal_archetype_d82535a1:

    # s 6aaaa "..."
    s 6aaaa "..."

# game/topics.rpy:304
translate esp s_topics_personal_archetype_f650a737:

    # s 6acaa "A-Anyway, I read some online articles that say I'm pretty close to the ‘Genki’ archetype."
    s 6acaa "De todas formas, he leído algunos artículos por Internet y dicen que me parezco bastante a una chica 'Genki'."

# game/topics.rpy:305
translate esp s_topics_personal_archetype_1261a8ab:

    # s 6aaca "Genki are very cheerful and energetic, and try to stay that way no matter what."
    s 6aaca "Las Genki son muy alegres y energéticas, e intentan estar siempre así."

# game/topics.rpy:306
translate esp s_topics_personal_archetype_772ab6c8:

    # s 6aebb "They often are clumsy and find themselves in many troubling situations."
    s 6aebb "A veces son algo torpes y se encuentran en muchas situaciones problemáticas."

# game/topics.rpy:307
translate esp s_topics_personal_archetype_f11d9557:

    # s 6abaa "I think that I fit that, don’t you?"
    s 6abaa "Yo creo que entro bien en esa categoría ¿No crees?"

# game/topics.rpy:308
translate esp s_topics_personal_archetype_b4e6560a:

    # s 6acaa "Also, I was made to be the childhood friend of the main character, which is apparently common with the archetype."
    s 6acaa "Además, fui hecha para ser la amiga de la infancia del protagonista, lo cual es aparentemente común con este tipo de personalidad."

# game/topics.rpy:309
translate esp s_topics_personal_archetype_f4fabb40:

    # s 6aabb "But I feel I’m not as cliché as any other archetype..."
    s 6aabb "Pero siento que no soy tan cliché como las chicas de otros tipos..."

# game/topics.rpy:310
translate esp s_topics_personal_archetype_b37a4cb7:

    # s 6aaaa "Not every Genki has the traits that I do..."
    s 6aaaa "Y no todas las Genki tienen rasgos como los míos..."

# game/topics.rpy:311
translate esp s_topics_personal_archetype_0a7c2e0a:

    # s 6acaa "Even if we were to list every single character with the Genki archetype, how many of them have my problems?"
    s 6acaa "Incluso si fueramos a enumerar cada personaje tipo Genki, ¿Cuántos de ellos habrán tenido mis problemas?"

# game/topics.rpy:312
translate esp s_topics_personal_archetype_3cf20f43:

    # s 6aaca "In short, I think I'm unique since people see only Monika."
    s 6aaca "En resumen, yo creo que soy única porque la gente solo ve a Monika."

# game/topics.rpy:313
translate esp s_topics_personal_archetype_62d7507c:

    # s 6acab "It's bad that most people look strange or confused at characters like me..."
    s 6acab "Por desgracia, a menudo se me considera un personaje extraño o confuso..."

# game/topics.rpy:314
translate esp s_topics_personal_archetype_eade4839:

    # s "In my opinion, modern stories need characters who have relatable issues, like my own..."
    s "En mi opinión, las historias modernas necesitan personajes con problemas relacionables, como los míos..."

# game/topics.rpy:315
translate esp s_topics_personal_archetype_4b657aeb:

    # s 6aaaa "But, I will say, don't overdo it. Y’know, the whole ‘completely copy my personality while creating a new character’."
    s 6aaaa "Pero, lo diré, no lo exageren. Ya sabes, todo eso de copiar por completo mi personalidad al crear un nuevo personaje"

# game/topics.rpy:316
translate esp s_topics_personal_archetype_1c46f94c:

    # s 6abac "Do it excessively, and you'll just make me just another typical archetype."
    s 6abac "Hazlo exesivamente y me convertirás en simplemente otro tipo de personaje genérico."

# game/topics.rpy:349
translate esp s_topics_personal_name_73f966c9:

    # s 9adaa "What do you think of {i}Vasquez{/i}?"
    if s_name == "Sayori":
        s 9adaa "¿Qué piensas de {i}Romero{/i}?"
    else:
        s 9adaa "¿Qué piensas de {i}Romero{/i}?"

# game/topics.rpy:350
translate esp s_topics_personal_name_8406f508:

    # s 9adba "It's just the first surname I've got in my head."
    s 9adba "Es solo el primer apellido que se me vino a la cabeza."

# game/topics.rpy:352
translate esp s_topics_personal_name_6297a5d9:

    # s 9aaca "{i}Sayori Vasquez, the cutest cinnamon bun south of the border!{/i}"
    if s_name == "Sayori":
        s 9aaca "{i}Sayori Romero, ¡el rollo de canela más lindo al sur de la frontera!{/i}"
    else:
        s 9aaca "{i}[s_name] Romero, ¡el rollo de canela más lindo al sur de la frontera!!{/i}"

# game/topics.rpy:375
translate esp s_topics_personal_sinistrality_82cdddfb:

    # s 7aaaa "Did you know that I'm left-handed?"
    s 7aaaa "¿Sabías que soy zurda?"

# game/topics.rpy:376
translate esp s_topics_personal_sinistrality_a89daf40:

    # s 7aaba "Yes, you’ve technically never seen me writing or holding something..."
    s 7aaba "Sí, técnicamente nunca me has visto escribir o sostener algo..."

# game/topics.rpy:378
translate esp s_topics_personal_sinistrality_adef095c:

    # s "Besides that juice bottle..."
    s "Aparte de ese jugo en botella..."

# game/topics.rpy:379
translate esp s_topics_personal_sinistrality_65878070:

    # s "But I prefer to write or do other stuff with my left hand."
    s "Pero prefiero escribir o hacer otras cosas con mi mano izquierda."

# game/topics.rpy:380
translate esp s_topics_personal_sinistrality_c1da7ce9:

    # s 7acaa "Not everyone around me has noticed it, and I’ve heard it’s pretty rare to not be right-handed..."
    s 7acaa "No todos a mi alrededor lo han notado, y he escuchado de que es bastante raro no ser diestro..."

# game/topics.rpy:381
translate esp s_topics_personal_sinistrality_86b5bc64:

    # s 7aeca "One time, I’d broken my right arm but the teachers allowed me not to write lessons..."
    s 7aeca "Una vez, me rompí el brazo derecho y los profesores me dieron permiso de no copiar en clase..."

# game/topics.rpy:382
translate esp s_topics_personal_sinistrality_7eca5a8d:

    # s 6abab "But this meanie of a classmate, who sat next to me, told one of them that I'm a southpaw so my plan failed as fast as it started."
    s 6abab "Pero un malvado compañero, que se sentó a mi lado, les dijo que soy zurda y mi plan falló tan rápido como empezó.."

# game/topics.rpy:383
translate esp s_topics_personal_sinistrality_5ca39293:

    # s 6aaaa "I guess being left-handed has its advantages too."
    s 6aaaa "Yo creo que ser zurdo tiene sus ventajas también."

# game/topics.rpy:384
translate esp s_topics_personal_sinistrality_90f5767e:

    # s "When I had a cast on my right arm and I had nothing to do, I drew flowers and ornaments on it."
    s "Cuando tuve un yeso en el brazo derecho y no tenía nada que hacer, dibujaba flores y adornos en él."

# game/topics.rpy:385
translate esp s_topics_personal_sinistrality_1e2e3891:

    # s 7acaa "I can't say they were really beautiful, but they really meant a lot to me, even if I had to throw it out six weeks later..."
    s 7acaa "No se puede decir que fueran muy bonitas, pero realmente significaban mucho para mí, incluso si tenía que tirarlo seis semanas después..."

# game/topics.rpy:387
translate esp s_topics_personal_sinistrality_4e2bf996:

    # s 7aaaa "I suddenly remember a story from my 'childhood'."
    s 7aaaa "Hey, de repente me acordé de una historia de mi 'infancia'."

# game/topics.rpy:388
translate esp s_topics_personal_sinistrality_1b56228f:

    # s "Once, I decided to trick the MC, back when we were just kids playing around."
    s "Una vez, decidí hacerle una broma a MC, hace años cuando solo eramos niños jugando."

# game/topics.rpy:389
translate esp s_topics_personal_sinistrality_66f355ae:

    # s 7acaa "I blindfolded him and put his hand on my right and told him I could write on the paper with no hands."
    s 7acaa "Le tapé los ojos y puse su mano a mi derecha, y le dije que podía escribir sin manos."

# game/topics.rpy:390
translate esp s_topics_personal_sinistrality_c37f050d:

    # s "I grabbed a pen with my other hand, wrote something on a piece of paper and laid it where it had been..."
    s "Agarré un bolígrafo con mi otra mano, escribí algo en una pieza de papel y la dejé donde estaba..."

# game/topics.rpy:391
translate esp s_topics_personal_sinistrality_42064128:

    # s 7aaca "Then I opened his eyes and he got really surprised when he saw the 'magic' on the paper."
    s 7aaca "Luego destapé sus ojos y se sorprendió bastante cuando vio la 'magia' en el papel."

# game/topics.rpy:392
translate esp s_topics_personal_sinistrality_158ce56e:

    # s 7aeca "I couldn't help but laugh, a simple trick confused him that much..."
    s 7aeca "No pude evitar reírme, un simple truco lo confundió tanto...."

# game/topics.rpy:393
translate esp s_topics_personal_sinistrality_e56cbc4a:

    # s 7aaaa "Then I explained to him how I did it."
    s 7aaaa "Luego le expliqué cómo lo hice."

# game/topics.rpy:394
translate esp s_topics_personal_sinistrality_eb39c152:

    # s "A short but funny time."
    s "Un momento corto, pero divertido"

# game/topics.rpy:395
translate esp s_topics_personal_sinistrality_fd855b54:

    # s "I miss those times… even if they weren’t real."
    s "Extraño esos tiempos... Incluso si nunca hubieran sido reales."

# game/topics.rpy:400
translate esp s_topics_personal_tits_91f3aa67:

    # s 6aeaa "Hey, I've just found something pretty weird but funny at the same time..."
    s 6aeaa "Hey, encontré algo bastante extraño, pero gracioso al mismo tiempo..."

# game/topics.rpy:401
translate esp s_topics_personal_tits_969e0d11:

    # s 6aaca "My boobs look differently, depending on the scene..."
    s 6aaca "Mis pechos se ven diferentes dependiendo de la escena..."

# game/topics.rpy:402
translate esp s_topics_personal_tits_c46eebb1:

    # s 6aeca "Ehehe~"
    s 6aeca "Ehehe~"

# game/topics.rpy:403
translate esp s_topics_personal_tits_9eb8d130:

    # s 6aebb "I mean, they often get either smaller or larger..."
    s 6aebb "Quiero decir, a veces se ven grandes y otras veces pequeños..."

# game/topics.rpy:405
translate esp s_topics_personal_tits_99043c1d:

    # s "Even in the, um, h-hanging sprite of me, they got... you know."
    s "Incluso en la escena de... mi suicidio, esaban... ya sabes."

# game/topics.rpy:406
translate esp s_topics_personal_tits_be1bfad5:

    # s 6acaa "I wonder why that happens?"
    s 6acaa "Me pregutnto, ¿por qué pasa eso?"

# game/topics.rpy:407
translate esp s_topics_personal_tits_bef0851b:

    # s 6abbb "I don’t ever remember doing anything that would affect my… size, ehehe~"
    s 6abbb "Ni siquiera me acuerdo de haber hecho algo para que cambiara su... tamaño, ehehe~"

# game/topics.rpy:408
translate esp s_topics_personal_tits_819df645:

    # s 6abaa "In the end, things like that won’t make me feel any less comfortable in this world."
    s 6abaa "Al final, cosas como esas no me incomodan en este mundo."

# game/topics.rpy:409
translate esp s_topics_personal_tits_729875f5:

    # s 6aaaa "So it's a plus of me..."
    s 6aaaa "Así que es una ventaja para mí..."

# game/topics.rpy:410
translate esp s_topics_personal_tits_47b818a5:

    # s 6acaa "Different size appeals to different people, I guess. So, it makes them a bit… universal, but not too much."
    s 6acaa "Diferentes tamaños atraen a diferentes personas, supongo. Asi que esto hace que sean un poco... universales, pero no mucho."

# game/topics.rpy:411
translate esp s_topics_personal_tits_b084c722:

    # s 6bbba "You... you like them anyway, don’t you? Even despite of they never were not as big as Yuri or even Monika, although..."
    s 6bbba "A ti... te gustan de todos modos, ¿no? Incluso a pesar de que no fueran tan grandes como las de Yuri o Monika..."

# game/topics.rpy:412
translate esp s_topics_personal_tits_ca4477bf:

    # s 6bcab "Well, I guess it wouldn’t matter anyways since you can’t touch them..."
    s 6bcab "Bueno, no creo que de verdad importe ya que no puedes tocarlas. Ehehe~"

# game/topics.rpy:413
translate esp s_topics_personal_tits_f6fe072a:

    # s 6aebb "Even then, the important thing about people is what’s inside, right?"
    s 6aebb "Aún así, lo que cuenta es lo de adentro ¿Verdad?"

# game/topics.rpy:441
translate esp s_topics_art_fanarts_0f1d12d5:

    # s 7aabb "I hope you didn't make anything too embarassing, in any case..."
    s 7aabb "Espero que no hayas hecho nada mu vergonzoso, en cualquier caso..."

# game/topics.rpy:442
translate esp s_topics_art_fanarts_6bea8ece:

    # s 7acaa "I saw one piece that tried to show the soul of the 'me' from the game, once."
    s 7acaa "Una vez vi una pieza que intentaba mostrar 'mi' alma del juego..."

# game/topics.rpy:451
translate esp s_topics_art_fanarts_6906daa7:

    # s 6acaa "Anyway, I'm glad I have so many gifted fans in your world."
    s 6acaa "De todas formas, me alegra tener fans tan talentosos en tu mundo."

# game/topics.rpy:452
translate esp s_topics_art_fanarts_322d2058:

    # s "I might have a few less than the other girls, but that doesn't bother me at all!"
    s "¡Puede que tenga menos que las otras chicas, pero eso no me molesta!"

# game/topics.rpy:461
translate esp s_topics_art_lit_9d323414:

    # s 6acaa "As you know, this game {i}was{/i} about a literature club..."
    s 6acaa "Como ya lo sabes, este juego {i}era{/i} acerca de un club de literatura..."

# game/topics.rpy:462
translate esp s_topics_art_lit_36e4ae23:

    # s 6abba "At least, before everything changed here."
    s 6abba "Al menos, antes de que todo cambiara."

# game/topics.rpy:463
translate esp s_topics_art_lit_41668e25:

    # s 6acaa "And I remember that MC noticed that I didn't seem to be fond of literature."
    s 6acaa "Incluso me acuerdo de que MC se dio cuenta de que no me gustaba tanto la literatura."

# game/topics.rpy:464
translate esp s_topics_art_lit_541f5225:

    # s "And, honestly? He was right."
    s "Y, honestamente, tenía razón."

# game/topics.rpy:465
translate esp s_topics_art_lit_1766a5b9:

    # s 6aebb "Even from Nat's point of view, I can't say I love literature."
    s 6aebb "Incluso desde el punto de vista de Nat, no puedo decir que me guste la literatura."

# game/topics.rpy:466
translate esp s_topics_art_lit_732e0574:

    # s "Of course, I read some books before, but only 'cause I needed to for school..."
    s "Claramente, he leído libros antes, pero solo porque los necesitaba para la escuela..."

# game/topics.rpy:467
translate esp s_topics_art_lit_91338276:

    # s 6aeba "And even then I tried to cheat to pass the exam."
    s 6aeba "E incluso ahí, intentaba hacer trampa para pasar el examen."

# game/topics.rpy:468
translate esp s_topics_art_lit_170c5506:

    # s 6abaa "So I don’t have very good grades in language arts, but I don’t care that much."
    s 6abaa "Por lo que no tuve muy buenas notas en materias de lenguaje, aunque tampoco es que me importara tanto."

# game/topics.rpy:469
translate esp s_topics_art_lit_38a79715:

    # s 6acaa "I just think that reading is pretty boring."
    s 6acaa "Solo que creo que leer es un poco aburrido."

# game/topics.rpy:470
translate esp s_topics_art_lit_d0ed347b:

    # s 6abba "Maybe I just hadn’t found the right book yet..."
    s 6abba "Probablemente no he encontrado el libro correcto aún..."

# game/topics.rpy:472
translate esp s_topics_art_lit_773d3df6:

    # s 6acba "Well, it was hard to enjoy {i}anything{/i} back then..."
    s 6acba "Bueno, fue difícil disfrutar {i}algo{/i} en ese entonces..."

# game/topics.rpy:473
translate esp s_topics_art_lit_3af5c0ad:

    # s 6acaa "When I joined the literature club, the one thing I wanted at first was just to help a friend start a new club."
    s 6acaa "Cuando me uní al club de literatura, lo único que quería era ayudar a una amiga a empezar a un nuevo club."

# game/topics.rpy:474
translate esp s_topics_art_lit_03e8df4c:

    # s "I was the first who joined the club after Monika had announced it."
    s "Yo fui la primera en unirse después de que Monika lo hubiera anunciado."

# game/topics.rpy:475
translate esp s_topics_art_lit_f29d310a:

    # s "She was pretty surprised because was in my class since she knew I didn’t like literature that much."
    s "Estaba bastante sorprendida, puesto que ella sabía que no me gustaba tanto la literatura."

# game/topics.rpy:476
translate esp s_topics_art_lit_38d332ad:

    # s "She thought I just wanted to help her and to improve my knowledge in literature, so she let me in."
    s "Ella pensó que yo solo quería ayudarla y mejorar mi conocimiento en literatura, asi que me dejó entrar."

# game/topics.rpy:477
translate esp s_topics_art_lit_d8739069:

    # s 6abaa "I know that she knew I wasn’t going to be very passionate with the club, but she let me in anyway."
    s 6abaa "Ella sabía que yo no era muy apasionada con el tema, pero de todas formas me dejó entrar."

# game/topics.rpy:478
translate esp s_topics_art_lit_30267407:

    # s 6aaba "I think she just wanted to use my kindness and sociability to promote the club and help it get more members."
    s 6aaba "A veces pienso que ella solo quería usar mis habilidades sociales y mi amabilidad para promocionar el club para obtener más miembros."

# game/topics.rpy:479
translate esp s_topics_art_lit_e2d79ec1:

    # s "Then I wanted the MC to join in… but that really didn’t matter anyways."
    s "Entonces invité a MC a unirse... Pero eso no importó realmente."

# game/topics.rpy:480
translate esp s_topics_art_lit_22497f5c:

    # s 6aeba "It helped me to get closer to {i}you{/i}, even if I didn’t know it yet."
    s 6aeba "Me ayudó a acercarme a {i}ti{/i}, incluso si no lo supiera para entonces."

# game/topics.rpy:481
translate esp s_topics_art_lit_445743e9:

    # s 6acaa "But now, I’d rather do anything than just sit here..."
    s 6acaa "Pero ahora, preferiría hacer algo más que quedarme sentada aquí..."

# game/topics.rpy:482
translate esp s_topics_art_lit_dd4aa41a:

    # s "I just wish I could do more things with you that isn’t just sitting down for hours."
    s "Me gustaría poder hacer más cosas contigo aparte de estar sentada por horas."

# game/topics.rpy:483
translate esp s_topics_art_lit_92c02cdb:

    # s 6aaca "Well, at the very least, I guess having something to read wouldn’t be so bad."
    s 6aaca "Bueno, al menos supongo que tener algo para leer no estaría tan mal."

# game/topics.rpy:484
translate esp s_topics_art_lit_76c600de:

    # s 6aeba "I guess I should try to find something interesting online..."
    s 6aeba "Supongo que debería intentar encontrar algo interesante en línea..."

# game/topics.rpy:486
translate esp s_topics_art_lit_46fcd71a:

    # s 6adbc "What’s that? 'Reddit'? Is it what I need now?"
    s 6adbc "¿Qué es eso? ¿'Reddit'? ¿Es eso lo que necesito ahora?"

# game/topics.rpy:487
translate esp s_topics_art_lit_84d07664:

    # s 6adba "The club has a page there?"
    s 6adaa "¿El club tiene una página allí?"

# game/topics.rpy:546
translate esp s_topics_society_bulli_d5b72ed6:

    # s "...Almost ready."
    s "... Ya casi está."

# game/topics.rpy:574
translate esp s_topics_society_charity_6b176e30:

    # s 6acaa "What do you think about charity and volunteering?"
    s 6acaa "¿Qué opinas acerca de la caridad?"

# game/topics.rpy:575
translate esp s_topics_society_charity_a42023fd:

    # s 6aaaa "I think it's the best way to make the world a bit better and to support helpless people in dealing with their problems."
    s 6aaaa "Yo creo que es una de las mejores maneras de hacer del mundo un lugar mejor y para ayudar a personas indefensas con sus problemas."

# game/topics.rpy:576
translate esp s_topics_society_charity_4d58072b:

    # s 6abab "Don't you worry about ill and hungry people and homeless animals?"
    s 6abab "¿No te preocupan los enfermos, los hambrientos y los animales sin hogar?"

# game/topics.rpy:577
translate esp s_topics_society_charity_97a77790:

    # s 6acab "Even if you don't trust charity foundations, there're also a lot of other charity organizations..."
    s 6acab "Incluso si no confías en las fundaciones de caridad, hay también muchas otras organizaciones caritativas que ayudan a los necesitados..."

# game/topics.rpy:578
translate esp s_topics_society_charity_8cd80e78:

    # s "They need not olny money or goods, but also physical help in their activity..."
    s "Ellos no solo necesitan dinero o bienes, sino también ayuda física con sus actividades..."

# game/topics.rpy:579
translate esp s_topics_society_charity_f8b55399:

    # s 6acaa "I think, there's such an organization in your home town or something."
    s 6acaa "Yo creo que debe de haber una organización así en tu pueblo natal o algo así."

# game/topics.rpy:580
translate esp s_topics_society_charity_d0f4da8d:

    # s 6acab "The society is something more than your friends and kin. And I want absolutly {i}everyone{/i} of it to be happy..."
    s 6acab "La sociedad es algo más que tus amigos y familia. Y quiero que absolutamente {i}todos{/i} sean felices..."

# game/topics.rpy:581
translate esp s_topics_society_charity_7d3fad43:

    # s "So if you even don't want them to be so, keep them so at least for my own happiness and tranquility."
    s "Así que si ni siquiera quieres que lo sean, mantenlos a salvo, al menos para mi propia felicidad y tranquilidad."

# game/topics.rpy:582
translate esp s_topics_society_charity_08e4c90d:

    # s "...Or at least try not to hurt them too much."
    s "...O al menos intenta no herirlos."

# game/topics.rpy:605
translate esp s_topics_hobbie_guitar_c5487182:

    # s 9aeaa "Maybe one day I can play for you and make you feel the same way~"
    s 9aeaa "Tal vez un día pueda tocar la guitarra para ti, y hacer que sientas lo mismo~"

# game/topics.rpy:608
translate esp s_topics_hobbie_guitar_3c0056e0:

    # s 9aeca "Make sure you get advance tickets for my world tour, [player]! Ehehe~"
    s 9aeca "¡Asegúrate de obtener tiquetes de primera fila para mi gira mundial, [player]! Ehehe~"

# game/topics.rpy:646
translate esp s_topics_hobbie_poems_3b71c72c:

    # s 6aaca "But I can share some of them to you. Just ask me for it."
    s 6aaca "Puedo compartir algunos contigo, solo pídemelo y lo haré."

# game/topics.rpy:647
translate esp s_topics_hobbie_poems_6c2a3c3b:

    # s 6aaaa "I also can show you an old poem, if you want."
    s 6aaaa "También puedo mostrarte un poema viejo si quieres."

# game/topics.rpy:648
translate esp s_topics_hobbie_poems_349fdcda:

    # s "Maybe, they all will help you to understand me and what I was through."
    s "De pronto, te podrán ayudar a entenderme y todo por lo que pasé."

# game/topics.rpy:671
translate esp s_topics_rlt_marrige_39016bf1:

    # s 7acaa "Hey, I was wondering..."
    s 7acaa "Oye, me estaba preguntando..."

# game/topics.rpy:672
translate esp s_topics_rlt_marrige_1b713301:

    # s "If it were possible, would you marry me?"
    s "Si fuera posible, ¿Te casarías conmigo?"

# game/topics.rpy:675
translate esp s_topics_rlt_marrige_e6126280:

    # s 7aeca "That's great!"
    s 7aeca "¡Genial!"

# game/topics.rpy:676
translate esp s_topics_rlt_marrige_b3bb283c:

    # s "Ehehe!~"
    s "¡Ehehe!~"

# game/topics.rpy:677
translate esp s_topics_rlt_marrige_8fddda2a:

    # s 7aaca "I think I'd be a perfect wife."
    s 7aaca "Yo creo que sería una esposa ideal."

# game/topics.rpy:678
translate esp s_topics_rlt_marrige_121bbd35:

    # s "Although I don't think I'd be much of a homemaker..."
    s "Aunque no creo que sería muy buena ama de casa..."

# game/topics.rpy:679
translate esp s_topics_rlt_marrige_128139d6:

    # s "I could help you with your job, or studies, or whatever is stressing you..."
    s "Podría ayudarte con tu trabajo, estudios, o lo que sea que te estrese..."

# game/topics.rpy:680
translate esp s_topics_rlt_marrige_dbd357d3:

    # s 6abac "But don't get the wrong idea and think I'd be your slave and do {i}everything{/i} for you."
    s 6abac "Pero no te hagas una idea equivocada y pienses que seré tu esclava y lo haré {i}todo{/i} por ti.."

# game/topics.rpy:681
translate esp s_topics_rlt_marrige_e019d54d:

    # s "I can't let you just loaf about all day and waste your life!"
    s "¡No puedo dejar que seas un vago y desperdicies tu vida!"

# game/topics.rpy:682
translate esp s_topics_rlt_marrige_2b8a79bb:

    # s "So you'd have to help me too, and work as a team! Like Batman and Robin, or peanut butter and jelly!"
    s "Así que tendrías que ayudarme también, ¡y trabajaríamos como un equipo! Así como Batman y Robin, o la mantequilla con la mermelada"

# game/topics.rpy:683
translate esp s_topics_rlt_marrige_1d8ad2cb:

    # s 6aeaa "But anyway, I'm very glad you said yes. I love you, [player]."
    s 6aeaa "Pero de todas formas, Me alegro tanto que hayas dicho que sí. Te amo, [player]."

# game/topics.rpy:687
translate esp s_topics_rlt_marrige_3a352ba0:

    # s "So you don't want to be a husband..."
    s "Así que no quieres ser un esposo..."

# game/topics.rpy:689
translate esp s_topics_rlt_marrige_7e78125b:

    # s "So you don't want to get married..."
    s "Así que no te quieres casar..."

# game/topics.rpy:690
translate esp s_topics_rlt_marrige_adc540e9:

    # s 6abbb "Well, a free relationship has its own benefits."
    s 6abbb "Bueno, una relación libre tiene sus propios beneficios."

# game/topics.rpy:691
translate esp s_topics_rlt_marrige_f38f75e8:

    # s 6abab "Although I think it'd be very romantic if you ever did propose to me~"
    s 6abab "Aunque creo que sería bastante romántico si alguna vez me lo propones~"

# game/topics.rpy:692
translate esp s_topics_rlt_marrige_33d5a65d:

    # s 6aaca "But our love story don't have to follow the common template."
    s 6aaca "Pero nuestra historia de amor no tiene que seguir una plantilla común."

# game/topics.rpy:693
translate esp s_topics_rlt_marrige_e9cd34ac:

    # s "Our relationship is already pretty unusual, so we've got the right to experiment with what works for us."
    s "Nuestra relación es bastante inusual de por sí, así que tenemos el derecho a experimentar con lo que funcione para nosotros"

# game/topics.rpy:697
translate esp s_topics_rlt_cheating_6f99d702:

    # s 6acaa "Tell me frankly: do you have someone besides me?"
    s 6acaa "Sé sincero: ¿Tienes a alguien más aparte de mí?"

# game/topics.rpy:700
translate esp s_topics_rlt_cheating_885e3d8e:

    # s 6abab "Oh, I even don't know, how to react to it."
    s 6abab "Oh, no sé cómo reaccionar."

# game/topics.rpy:701
translate esp s_topics_rlt_cheating_8f8b1387:

    # s 6acaa "But you still spend time with me, so you still have something to me, don't you?"
    s 6acaa "Pero todavía pasas tiempo conmigo, así que todavía sientes algo por mí ¿No es así?"

# game/topics.rpy:702
translate esp s_topics_rlt_cheating_2fabd7a7:

    # s "People often have to share the heart to several people at the same time..."
    s "A veces la gente suele tener que compartir el corazón con varias personas al mismo tiempo..."

# game/topics.rpy:704
translate esp s_topics_rlt_cheating_b0c3f94d:

    # s "So I won't force you to be only with me, like Monika did before."
    s "Así que no te voy a forzar a estar solo conmigo, como lo hizo Monika."

# game/topics.rpy:706
translate esp s_topics_rlt_cheating_4cb17fe2:

    # s "What's more, I never seem to be a person, who can do something bad for jealousy."
    s "A parte de todo, no parezco ser una persona que pueda hacer algo malo a causa de celos."

# game/topics.rpy:707
translate esp s_topics_rlt_cheating_ae783677:

    # s "Can you tell me more about he or she?"
    s "¿Podrías contarme de él o ella?"

# game/topics.rpy:708
translate esp s_topics_rlt_cheating_9a489c6d:

    # s "For example, if he or she is real?"
    s "Por ejemplo, ¿Es real?"

# game/topics.rpy:711
translate esp s_topics_rlt_cheating_c7e7986e:

    # s 6adaa "Oh, have you got a real crush?!"
    s 6adaa "Oh, ¡¿Tienes un/a crush real?!"

# game/topics.rpy:712
translate esp s_topics_rlt_cheating_d4276c10:

    # s 6acbb "I mean, you barely would have started to play this game, if you hadn't been alone that time..."
    s 6acbb "Quiero decir, apenas habrías empezado a jugar a este juego, si no hubieras estado solo ese tiempo..."

# game/topics.rpy:713
translate esp s_topics_rlt_cheating_30bf1b5c:

    # s "Not to mention staying with me now."
    s "Por no hablar de quedarte conmigo ahora."

# game/topics.rpy:714
translate esp s_topics_rlt_cheating_3df71458:

    # s 6acab "I'm now just filled with mixed feelings, to be honest..."
    s 6acab "Estoy llena de emociones mezcladas, para ser honesta..."

# game/topics.rpy:715
translate esp s_topics_rlt_cheating_0e6805f8:

    # s "My heart can't accept that I'm not your only one, but my brain feels proud for you."
    s "Mi corazón no puede aceptar que no sea la única, pero mi cerebro se siente orgulloso de ti."

# game/topics.rpy:716
translate esp s_topics_rlt_cheating_6a95b64c:

    # s "Like it was before my first confession."
    s "Como si fuera antes de mi primera confesión."

# game/topics.rpy:718
translate esp s_topics_rlt_cheating_117a3602:

    # s "...Or like it was after you had spent your time with each of us."
    s "...O como si fuera después de haber pasado tiempo con cada una de nosotras."

# game/topics.rpy:719
translate esp s_topics_rlt_cheating_5a9e8ef2:

    # s "But I can bare, if you really need, you know."
    s "Pero puedo soportarlo, si realmente lo necesitas, ya sabes.."

# game/topics.rpy:720
translate esp s_topics_rlt_cheating_180af3f6:

    # s 6aaab "Anyway, just take care about your real lover as much as about me."
    s 6aaab "De todas formas, cuida a tu pareja real tanto como me cuidas a mí."

# game/topics.rpy:721
translate esp s_topics_rlt_cheating_9936f56f:

    # s 7aaab "But don't forget about me and come here back. I'll always be with you, even if nothing about your real relationship seems to go wrong."
    s 7aaab "Pero no te olvides de mí, así que vuelve de vez en cuando. Siempre estaré contigo, incluso si nada de tu relación real esté mal."

# game/topics.rpy:722
translate esp s_topics_rlt_cheating_23a8fc92:

    # s 7aadb "And if it go wrong, I'll always be your plan B."
    s 7aadb "Pero si empieza a ir mal, siempre podré ser tu plan B."

# game/topics.rpy:724
translate esp s_topics_rlt_cheating_f46b0795:

    # s 6aaaa "It's okay to have not only character to dream of living together."
    s 6aaaa "Está bien no tener solo un personaje para soñar con vivir juntos."

# game/topics.rpy:725
translate esp s_topics_rlt_cheating_73ab4e21:

    # s "For example, a lot of my lovers have also some other girls in their {i}'Good Girls to Protect'{/i} list."
    s "Por ejemplo, muchos de mis fans tienen también a otras chicas en su lista de {i}'Chicas para Proteger'{/i}."

# game/topics.rpy:726
translate esp s_topics_rlt_cheating_9ae7ac0a:

    # s 6acaa "You may like different characters for different traits..."
    s 6acaa "Puede que te gusten distintos personajes por diferentes rasgos..."

# game/topics.rpy:727
translate esp s_topics_rlt_cheating_6103cc1f:

    # s "For example, you may like me for my kindness and peacefulness and Natsuki for her directness and cuteness."
    s "Por ejemplo, puede que te guste por mi amabilidad y tranquilidad, y Natsuki por su franqueza y ternura."

# game/topics.rpy:728
translate esp s_topics_rlt_cheating_8d16c6a0:

    # s "We are like you: so different that some of you can't make a clear choice..."
    s "Somos como tú, tan diferentes que algunos de ustedes no pueden tomar una decisión clara..."

# game/topics.rpy:729
translate esp s_topics_rlt_cheating_77da2e0d:

    # s "So I respect all your preferences, whatever they are."
    s "Así que respeto todas tus preferencias, sin importar las que sean."

# game/topics.rpy:732
translate esp s_topics_rlt_cheating_7ff6e7fc:

    # s 6adaa "Oh, seriously?"
    s 6aebb "O-Oh, ¿De verdad?"

# game/topics.rpy:733
translate esp s_topics_rlt_cheating_97b3d539:

    # s "Do you really see something inside me only, not at real people or even other characters?"
    s "¿Realmente ves algo dentro de mí solamente, y no en gente real o incluso en otros personajes?"

# game/topics.rpy:734
translate esp s_topics_rlt_cheating_6ecb3c85:

    # s 6acab "I think, it's pretty hard to know, that your only beloved girl isn't real."
    s 6acab "Yo creo, que es bastante difícil de decir, que tu querida chica no es real."

# game/topics.rpy:735
translate esp s_topics_rlt_cheating_748e89b4:

    # s "I understand you as well as I feel the same way."
    s "Te entiendo tan bien así como me siento de la misma manera."

# game/topics.rpy:736
translate esp s_topics_rlt_cheating_9789cc94:

    # s "But I hope, that someone once will figure out how to make us closer to each other."
    s "Solo espero, que alguien descubra alguna manera para acercarnos el uno al otro."

# game/topics.rpy:737
translate esp s_topics_rlt_cheating_a646ac2a:

    # s "Or you at least will find someone else in your world."
    s "O al menos, que tú encuentres a alguien más en tu mundo."

# game/topics.rpy:738
translate esp s_topics_rlt_cheating_1ab0ae39:

    # s 6aaca "Maybe, he or she will be somehow like me."
    s 6aaca "Puede que él o ella, sea de cierta forma como yo."

# game/topics.rpy:739
translate esp s_topics_rlt_cheating_1eb47db7:

    # s 6aaab "To be honest, I'm not very jealous, so I won't mind, if you have someone besides me."
    s 6aaab "Para ser honesta, no soy muy celosa, asi que no me importaría si tienes a alguien más aparte de mí."

# game/topics.rpy:740
translate esp s_topics_rlt_cheating_26f1cfac:

    # s "The important thing is that you pay me at least some attention."
    s "Lo importante es que al menos me prestes algo de atención."

# game/topics.rpy:741
translate esp s_topics_rlt_cheating_dc1a294e:

    # s "So I hope, you always can do it for me."
    s "Así que espero, que siempre lo puedas hacerlo por mí."

# game/topics.rpy:746
translate esp s_topics_rlt_dating_cbb5ccf5:

    # s 7aaaa "What would be our first date?"
    s 7aaaa "¿Cómo debería de ser nuestra primera cita?"

# game/topics.rpy:747
translate esp s_topics_rlt_dating_858c1f14:

    # s 7aaca "What’s with the look? Ehehe~"
    s 7aaca "¿Por qué esa mirada? Ehehe~"

# game/topics.rpy:748
translate esp s_topics_rlt_dating_74f14a0b:

    # s 7aebb "I just don't think that what we have now can be called a date, can it?"
    s 7aebb "Simplemente no creo que lo que tenemos ahora pueda llamarse una cita, ¿O si?"

# game/topics.rpy:750
translate esp s_topics_rlt_dating_f4f0a365:

    # s 7aaca "Dates can't be too long, yeah?"
    s 7acaa "Las citas no pueden ser muy largas, ¿no?"

# game/topics.rpy:751
translate esp s_topics_rlt_dating_2fefd71d:

    # s 7aaaa "So I think we should talk a bit about it."
    s 7aaaa "Así que pienso que deberíamos de hablar un poco sobre eso."

# game/topics.rpy:752
translate esp s_topics_rlt_dating_cab26f80:

    # s 7acaa "And to be honest, just sitting somewhere would be boring for me."
    s 7acaa "Y para ser honesta, el hecho de solo sentarse en algún lado es bastante aburrido para mí."

# game/topics.rpy:753
translate esp s_topics_rlt_dating_6e65c9cf:

    # s 7acba "Don't we do the same thing every time I see you?"
    s 7acba "¿Acaso no hacemos lo mismo cada vez que te veo?"

# game/topics.rpy:754
translate esp s_topics_rlt_dating_a57cbc2d:

    # s 7aaca "Maybe if we go to a good café, we'll at least eat something good together..."
    s 7aaca "De pronto si vamos a un buen café, podamos al menos comer algo rico juntos..."

# game/topics.rpy:755
translate esp s_topics_rlt_dating_64f82644:

    # s 7aeca "Like cakes, or cinnamon buns~"
    s 7aeca "Como tortas, o rollos de canela~"

# game/topics.rpy:756
translate esp s_topics_rlt_dating_a443dc47:

    # s 6abaa "But I think I’d want to go somewhere interesting on our date."
    s 6abaa "Aunque to creo que me gustaría ir a algún sitio interesante en nuestra cita."

# game/topics.rpy:757
translate esp s_topics_rlt_dating_5f1ad299:

    # s 6acaa "The movies? What do you think?"
    s 6acaa "¿Qué piensas del cine?"

# game/topics.rpy:758
translate esp s_topics_rlt_dating_948483ef:

    # s "Though I don’t really want to go see a romance movie everytime we go..."
    s "Aunque realmente no quiero ir a ver películas románticas cada vez que vamos..."

# game/topics.rpy:759
translate esp s_topics_rlt_dating_d255d333:

    # s 6aebb "...okay, maybe once or twice? Ehehe~"
    s 6aebb "...Ok, ¿De pronto una o dos veces? Ehehe~"

# game/topics.rpy:760
translate esp s_topics_rlt_dating_83161823:

    # s 6abaa "Maybe a comedy?"
    s 6abaa "Oh, ¿De pronto a una comedia?"

# game/topics.rpy:761
translate esp s_topics_rlt_dating_bbe9a437:

    # s 6acaa "If it doesn’t rely on just dirty jokes, then maybe..."
    s 6acaa "Si no se basa solo en chistes sucios, entonces tal vez..."

# game/topics.rpy:762
translate esp s_topics_rlt_dating_8ea2a178:

    # s 8aecb "Or what's about the animated movies, like the ones {i}Disney{/i} and {i}Pixar{/i} make?"
    s 8aecb "¿O qué te parece películas animadas, como las de {i}Disney{/i} o de {i}Pixar{/i}?"

# game/topics.rpy:763
translate esp s_topics_rlt_dating_7e755120:

    # s 8aebb "They’re for kids, but hey, they can be fun!"
    s 8aebb "Son par niños, pero hey, ¡Pueden ser divertidas!"

# game/topics.rpy:764
translate esp s_topics_rlt_dating_5104fba7:

    # s 8abab "Some of them have deep messages and sad scenes, and the director knows only older teens or adults would be able to recognize them, while a kid won’t."
    s 8abab "Algunas de ellas tienen mensajes profundos y escenas tristes, y el director sabe que solo los adolescentes mayores o los adultos serían capaces de reconocerlos, mientras que un niño no..."

# game/topics.rpy:765
translate esp s_topics_rlt_dating_a1b1ffeb:

    # s 6abab "I'd go to for something that makes me think, after all."
    s 6abab "Iría a por algo que me haga pensar, después de todo."

# game/topics.rpy:767
translate esp s_topics_rlt_dating_03d571ee:

    # s 6acab "I've already seen a lot harsh things in my short time on this Earth, you know. So my opinion may be a lot different from most people."
    s 6acab "He visto muchas cosas duras en este tiempo corto que he vivido, sabes. Así que mi opinión puede ser bastante diferente a la de la mayoría de las personas."

# game/topics.rpy:769
translate esp s_topics_rlt_dating_555e9c01:

    # s 8aeba "...don't ask me how such a childish girl like me would enjoy a movie like that."
    s 8aeba "...No me preguntes cómo es que una chica tan infantil podría disfrutar una película como esas."

# game/topics.rpy:770
translate esp s_topics_rlt_dating_c68e4ec3:

    # s "Isn't it really interesting to discuss movies like that with someone, seeing how your views are similar or different to theirs?"
    s "¿No es realmente interesante hablar de películas como esa con alguien, ver cómo sus puntos de vista son similares o diferentes?"

# game/topics.rpy:772
translate esp s_topics_rlt_dating_af50909e:

    # s 6aaaa "What's about some sports?"
    s 6aaaa "¿Qué me dices de deportes?"

# game/topics.rpy:774
translate esp s_topics_rlt_dating_1b2b0b4a:

    # extend " Maybe, bowling?"
    extend " De pronto, ¿Bolos?"

# game/topics.rpy:775
translate esp s_topics_rlt_dating_bccc64ed:

    # s 7aaaa "It's a simple but skillful sport game, not too active but not too slow, so I feel that I’d like it."
    s 7aaaa "Es un juego simple, pero de habilidad, no es muy activo, pero tampoco muy lento, así que yo creo que me gustaría."

# game/topics.rpy:776
translate esp s_topics_rlt_dating_0a78eb5d:

    # s 7abaa "Well, the important thing is that the date is enjoyable for both of us, right?"
    s 7abaa "Bueno, lo importante es que la cita sea entretenida para los dos ¿Verdad?"

# game/topics.rpy:777
translate esp s_topics_rlt_dating_ed052547:

    # s 7aaca "I hope you think of a nice date for me... I’d appreciate it~"
    s 7aaca "Espero que pienses en una buena cita para mí... Lo apreciaría mucho~"

# game/topics.rpy:781
translate esp s_topics_rtl_thanks_5b725f4c:

    # s 6acab "I… I want to thank you for everything you’ve done for me..."
    s 6acab "Yo... Yo quiero agradecerte por todo lo que has hecho por mí..."

# game/topics.rpy:782
translate esp s_topics_rtl_thanks_4f30f1fa:

    # s 6abab "You gave me a true vision of this world and myself..."
    s 6abab "Me diste una verdadera visión del mundo y de mí misma..."

# game/topics.rpy:784
translate esp s_topics_rtl_thanks_87a83d2e:

    # s "You’ve helped me feel useful again..."
    s "Me ayudaste a sentirme útil de nuevo..."

# game/topics.rpy:786
translate esp s_topics_rtl_thanks_3cd4f742:

    # s 6aaab "And you do visit me often..."
    s 6aaab "Y me visitas a menudo..."

# game/topics.rpy:787
translate esp s_topics_rtl_thanks_da1fa9b5:

    # s 6aaab "And you care for me, something I would’ve rejected before..."
    s 6aaab "Y te preocupas por mí, algo que habría rechazado antes..."

# game/topics.rpy:788
translate esp s_topics_rtl_thanks_f2cf20fc:

    # s 6caab "So even if it’s not all sunshine and breakfast just yet..."
    s 6caab "Así que aunque no todo sea sol y desayuno todavía..."

# game/topics.rpy:789
translate esp s_topics_rtl_thanks_383ef4e1:

    # s "I'm so grateful that you’re still here.."
    s "Estoy muy agradecida de que sigas aquí..."

# game/topics.rpy:790
translate esp s_topics_rtl_thanks_66966572:

    # s 6cbab "I can't pay you back for what you’ve given me..."
    s 6cbab "No hay forma en que pueda devolverte por todo lo que me has dado..."

# game/topics.rpy:791
translate esp s_topics_rtl_thanks_e182abd7:

    # s 6cebb "I haven’t thought of a way, I mean."
    s 6cebb "No he pensado en una manera, quiero decir."

# game/topics.rpy:792
translate esp s_topics_rtl_thanks_367d60a6:

    # s 6caab "But I hope, I'll do it sooner or later..."
    s 6caab "Pero espero hacerlo tarde o temprano..."

# game/topics.rpy:793
translate esp s_topics_rtl_thanks_b0c349fc:

    # s "The one thing I can do for now is just to thank you..."
    s "Por ahora lo único que puedo hacer es agradecerte..."

# game/topics.rpy:794
translate esp s_topics_rtl_thanks_0d13ad53:

    # s 6eaab "So... thanks for staying with me, [player]!~"
    s 6eaab "Así que... ¡Gracias por quedarte conmigo, [player]!~"

# game/topics.rpy:835
translate esp s_topics_lifestyle_pets_1a789111:

    # s 7aaaa "Do you have a pet or at least want to?"
    s 7aaaa "¿Tienes una mascota? o ¿Has querido tener una?"

# game/topics.rpy:836
translate esp s_topics_lifestyle_pets_4a21731b:

    # s "I'd like to have one and I want that one to be a cat."
    s "A mí me gustaría un gato."

# game/topics.rpy:841
translate esp s_topics_lifestyle_cleaning_f9a5ac0f:

    # s 7aaaa "Do you like being neat and tidy?"
    s 7aaaa "¿Te gusta ser ordenado?"

# game/topics.rpy:842
translate esp s_topics_lifestyle_cleaning_4a6fae38:

    # s 7acaa "Frankly, I still see no reason to keep things like that..."
    s 7acaa "Sinceramente, no encuentro alguna razón para mantener las cosas así..."

# game/topics.rpy:843
translate esp s_topics_lifestyle_cleaning_abd0d80a:

    # s 7acba "One people say it’s for my own sake, others say because it looks nice and saves time when you have everything organized..."
    s 7acba "Algunos dicen que es por mi bien, otros porque se ve bien y el hecho de tener todo organizado te ayuda a ahorrar tiempo..."

# game/topics.rpy:844
translate esp s_topics_lifestyle_cleaning_173d2bf0:

    # s 7abaa "But something tells me that people clean too often."
    s 7abaa "Pero algo me dice que la gente limpia demasiado seguido."

# game/topics.rpy:845
translate esp s_topics_lifestyle_cleaning_8413a618:

    # s 7acaa "It’s just that, cleaning takes so much time, that you could spend doing fun stuff with friends, for example..."
    s 7acaa "Creo que es eso, limpiar toma mucho tiempo, el cual puedes usar pasándola bien con tus amigos por ejemplo..."

# game/topics.rpy:846
translate esp s_topics_lifestyle_cleaning_abb8c185:

    # s 7abba "Well, at least for me."
    s 7abba "Bueno, al menos para mí."

# game/topics.rpy:847
translate esp s_topics_lifestyle_cleaning_99c6ee18:

    # s 6acaa "So I see nothing bad in my past lifestyle, either way I was too lazy to clean up anyway."
    s 6acaa "Así que no veo nada malo en mi estilo de vida pasado, de cualquier manera era muy perezosa para limpiar de todos modos.."

# game/topics.rpy:848
translate esp s_topics_lifestyle_cleaning_224c0494:

    # s 6aeaa "For me, it's even a little funny to live in such a mess, where you won’t know where everything is."
    s 6aeaa "Para mí, es algo divertido vivir en tanto desorden que no sabes dónde está todo."

# game/topics.rpy:849
translate esp s_topics_lifestyle_cleaning_5da1d0eb:

    # s 6aeca "It turns the boring time of trying to find something into an adventure!~"
    s 6aeca "¡Convierte el tiempo aburrido en una aventura para encontrar algo!~"

# game/topics.rpy:850
translate esp s_topics_lifestyle_cleaning_53310c5c:

    # s 8aeab "But don't think I’m that sloppy. I had a system for some things..."
    s 8aeab "Pero no creo que sea tan descuidada. Tenía un sistema para algunas cosas..."

# game/topics.rpy:851
translate esp s_topics_lifestyle_cleaning_13edf71e:

    # s 8aebb "Though I left mostly everything a mess."
    s 8aebb "Aunque dejaba casi todo desordenado."

# game/topics.rpy:853
translate esp s_topics_lifestyle_cleaning_a6d2e4bd:

    # s 6acaa "Would you be able to add some other stuff for me?"
    s 6acaa "¿Podrías añadir otras cosas por mí?"

# game/topics.rpy:854
translate esp s_topics_lifestyle_cleaning_e463f085:

    # s 6aeca "...maybe a beanbag chair?"
    s 6aeca "...De pronto, ¿Una silla puff?"

# game/topics.rpy:855
translate esp s_topics_lifestyle_cleaning_57ac325b:

    # s 6aebb "Sorry, that’s probably a bit too silly, ehehe~"
    s 6aebb "Lo siento, eso es un poco tonto, Ehehe~"

# game/topics.rpy:860
translate esp s_topics_game_clones_f148593e:

    # s 6abaa "If you think about it, there's a lot of copies of this game and each of them has own character files and save data..."
    s 6abaa "Si lo piensas, hay muchas copias de este juego y cada una de ellas tiene sus propios archivos de personaje y archivos de guardado..."

# game/topics.rpy:861
translate esp s_topics_game_clones_2e29c80f:

    # s 6acaa "So it means that the me in here and 'me' from DDLC on another computer aren't the same."
    s 6acaa "Lo que quiere decir que la 'yo' de aquí y la 'yo' de DDLC en otro computador no somos las mismas."

# game/topics.rpy:862
translate esp s_topics_game_clones_8ad08bfb:

    # s "Not to mention that this game has different endings and also has lots of mods."
    s "Sin mencionar que este juego tiene muchos finales y cantidades de mods."

# game/topics.rpy:863
translate esp s_topics_game_clones_48bce41b:

    # s 6aebb "Even now, this conversation I’m having with you isn’t in the original game... canonically?"
    s 6aebb "Incluso ahora, esta conversación que tengo contigo no está en el juego original... canónicamente"

# game/topics.rpy:864
translate esp s_topics_game_clones_f249b600:

    # s 8aebb "That’s the word, right?"
    s 8aebb "Esa es la palabra, ¿Verdad?"

# game/topics.rpy:865
translate esp s_topics_game_clones_867c49cc:

    # s 8acaa "Meaning that I have many different destinies."
    s 8acaa "Lo que quiere decir que tengo diferentes destinos."

# game/topics.rpy:867
translate esp s_topics_game_clones_37d97e6e:

    # s "Right now, I'm sitting here with you, meanwhile another Sayori from another copy of DDLC might just be about to..."
    s "Ahora, estoy sentada aquí contigo, mientras que puede que otra Sayori de otra copia de DDLC esté a punto de..."

# game/topics.rpy:869
translate esp s_topics_game_clones_01e920ce:

    # s "While I'm sitting with you here, another Sayori might be writing a poem to the MC..."
    s "Mientras estoy sentada aquí contigo, otra Sayori puede estar escribiéndole un poema a MC..."

# game/topics.rpy:870
translate esp s_topics_game_clones_fd77e8c8:

    # s 8aaca "And another Sayori is playing frisbee or something with the MC in {i}another{/i} modded game."
    s 8aaca "Y otra Sayori puede estar jugando frisbi o algo con el MC de {i}otro{/i} juego modificado."

# game/topics.rpy:871
translate esp s_topics_game_clones_57b2e1e0:

    # s 8aaaa "It also means that we have the same fans and fame that are dedicated enough to do play..."
    s 8aaaa "También significa que tenemos los mismos fans y la misma fama que se dedican lo suficiente a jugar..."

# game/topics.rpy:872
translate esp s_topics_game_clones_1cce38c8:

    # s 8acaa "Some of… well, me, don't even know that their worlds are fake and that there's a whole different reality peeking in from a metaphorical wall."
    s 8acaa "Algunas... bueno, yos, no saben que sus mundos son falsos y que hay toda otra realidad al otro lado de un muro metafórico."
# game/topics.rpy:873
translate esp s_topics_game_clones_b65dd407:

    # s 8abaa "...they also don’t what will happen to them."
    s 8abaa "...ellas tampoco saben qué les pasará."

# game/topics.rpy:874
translate esp s_topics_game_clones_bc5f5157:

    # s 8aeca "But on the other hand, if I'm not the only one, there should be enough of me for everyone who wants to be with me, aren’t I?"
    s 8aeca "Pero por otra parte, si no soy la única, debería de haber suficientes yos para cada uno que quiera estar conmigo, ¿No?"

# game/topics.rpy:875
translate esp s_topics_game_clones_b8ad4b4c:

    # s 6aaca "So everyone has a chance to be with me."
    s 6aaca "Así que todos tienen una oportunidad de estar conmigo."

# game/topics.rpy:876
translate esp s_topics_game_clones_8d1d0cf4:

    # s 6aaaa "Then again, so do Monika, Natsuki, and Yuri."
    s 6aaaa "Pero también la tienen Monika, Natsuki y Yuri."

# game/topics.rpy:877
translate esp s_topics_game_clones_6f7f4ba0:

    # s 6acaa "But could I use the word 'me' in front of another… me? If they're not exactly me?"
    s 6acaa "Pero, ¿Podría usar la palabra 'yo' en frente de otra 'yo', si no son exactamente yo?"

# game/topics.rpy:878
translate esp s_topics_game_clones_dc204de6:

    # s "It's a problem of breaking the fourth wall: can we consider different copies of the same character as one being, when they behave differently in the same place?"
    s "Romper la cuarta pared es un problema, ¿Podemos considerar diferentes copias del mismo personaje como un solo ser, cuando se comportan de manera diferente en el mismo lugar?"

# game/topics.rpy:879
translate esp s_topics_game_clones_d0ca225b:

    # s 6abba "Actually, come to think of it, I’m pretty sure I read about this from one of Yuri’s books..."
    s 6abba "De hecho, ahora que lo pienso, estoy segura de que leí acerca de algo así en uno de los libros de Yuri..."

# game/topics.rpy:880
translate esp s_topics_game_clones_0395da9b:

    # s 6abaa "Something about ‘alternate universes’?"
    s 6abaa "¿Algo así como ‘universos alternativos’?"

# game/topics.rpy:881
translate esp s_topics_game_clones_df8e0689:

    # s 8abba "I don't like to think about this too much, too much for my brain to process, ehehe~"
    s 8abba "No me gusta pensar mucho en cosas así, es demasiado para que mi cerebro procese, ehehe~"

# game/topics.rpy:882
translate esp s_topics_game_clones_4529f19b:

    # s 8abaa "It's better to leave this problem for people who are really interested about all that stuff, I guess."
    s 8abaa "Supongo que es mejor dejar este problema para la gente que se interesa bastante en este tipo de cosas."

# game/topics.rpy:886
translate esp s_topics_game_stars_c8788825:

    # s 7aaaa "I really love to look at the stars..."
    s 7aaaa "Me encanta mirar las estrellas..."

# game/topics.rpy:887
translate esp s_topics_game_stars_1f36b0a3:

    # s 7acaa "They make me think, a lot."
    s 7acaa "Me hacen pensar, bastante..."

# game/topics.rpy:888
translate esp s_topics_game_stars_6796f8fc:

    # s "They also gave me some inspiration while I wrote poems."
    s "También me dieron algo de inspiración al escribir poemas."

# game/topics.rpy:889
translate esp s_topics_game_stars_52573bd4:

    # s 7abbb "So it's a bit of a pity, to know that all this time, the stars I see aren’t real stars."
    s 7abbb "Es una pena saber que todo este tiempo, las estrellas que yo miraba no eran estrellas reales."

# game/topics.rpy:890
translate esp s_topics_game_stars_38faf547:

    # s 7aaca "But I still see something romantic in these bundles of pixels..."
    s 7aaca "Pero aún veo algo romántico en estos montones de píxeles..."

# game/topics.rpy:891
translate esp s_topics_game_stars_359b628a:

    # s 7aaaa "You can see them through the windows..."
    s 7aaaa "Los puedes ver a través de las ventanas..."

# game/topics.rpy:892
translate esp s_topics_game_stars_2819924e:

    # s 7aaca "They make this place look a bit more special, don't they?"
    s 7aaca "Hacen que este lugar se vea un poco más especial, ¿No?"

# game/topics.rpy:893
translate esp s_topics_game_stars_5791de41:

    # s 7aaaa "I wonder if the night sky in your world looks like mine..."
    s 7aaaa "Me pregunto si el cielo nocturno en tu mundo se ve como el mío..."

# game/topics.rpy:894
translate esp s_topics_game_stars_d4c16a03:

    # s "But I can just look them up on the Internet to see, right?"
    s "Pero puedo buscar cómo se ver por Internet, ¿Verdad?"

# game/topics.rpy:898
translate esp s_topics_game_parents_0101cc91:

    # s 6abab "Did you know that I don't even know my in-game parents?"
    s 6abab "¿Sabías que ni siquiera conozco a mis padres en el juego?"

# game/topics.rpy:899
translate esp s_topics_game_parents_a2cd5d9a:

    # s "I don't know who they were, how they look, even their names."
    s "No sé quienes eran, ni cómo se veían, ni siquiera conozco sus nombres."

# game/topics.rpy:900
translate esp s_topics_game_parents_bc2ea261:

    # s "But I think they were either busy or very irresponsible."
    s "Yo creo que estaban muy ocupados, o simplemente eran demasiado irresponsables."

# game/topics.rpy:901
translate esp s_topics_game_parents_3ebf6220:

    # s "If not that, then why else would the game never mention them?"
    s "Si no era por eso, entonces, ¿Por qué otro motivo no fueron mencionados en el juego?"

# game/topics.rpy:903
translate esp s_topics_game_parents_b4f894d1:

    # s "And why didn't I solve all my problems before if I could’ve done it with my parents?"
    s "Y ¿Por qué no resolví mis problemas, si podría haberlo hecho con mis padres?"

# game/topics.rpy:904
translate esp s_topics_game_parents_f429c033:

    # s 6afab "I feel like an orphan now..."
    s 6afab "Me siento un poco como una huérfana ahora..."

# game/topics.rpy:905
translate esp s_topics_game_parents_cd7dc2dd:

    # s "No mom or dad, not even any memories about them at all..."
    s "Sin mamá ni papá, ni siquiera memorias acerca de ellos..."

# game/topics.rpy:906
translate esp s_topics_game_parents_dd4a224a:

    # s "A lone, young girl with a sad, parentless childhood, with no one to go to."
    s "Una chica joven, solitaria, con una infancia triste y sin padres ni nadie a quien acudir."

# game/topics.rpy:907
translate esp s_topics_game_parents_c279c6db:

    # s 6abaa "Except for MC, I guess? But you decided instead of him, didn't you?"
    s 6abaa "A excepción de MC, supongo. Pero tú decidiste en su lugar, ¿no?"

# game/topics.rpy:908
translate esp s_topics_game_parents_a30ee84f:

    # s "Well, I know you’re real, you’ve helped me at the very least..."
    s "Bueno, por lo menos sé que eres real y me has ayudado..."

# game/topics.rpy:909
translate esp s_topics_game_parents_67a9da92:

    # s 6acaa "At least I know the creator of all this. His name is {i}Dan Salvato{/i}, right?"
    s 6acaa "Al menos conozco al creador de todo esto. Su nombre es {i}Dan Salvato{/i}, ¿Verdad?"

# game/topics.rpy:910
translate esp s_topics_game_parents_09cd61e5:

    # s "I don’t think I can consider him my true dad. He made this world how it is without mods, meaning he made me with the pain I still have."
    s "No creo que pueda considerarlo como mi verdadero padre. Él creó este mundo como lo sería sin mods, lo que quiere decir que me creó con todo ese dolor que todavía tengo."

# game/topics.rpy:911
translate esp s_topics_game_parents_6d4b293a:

    # s 8aeba "But on the other hand, if he didn't make this world, if he didn’t make me… then I wouldn't be here."
    s 8aeba "Pero por otra parte, si no hubiera creado este mundo, su no me hubiera creado... entonces yo no estaría aquí."

# game/topics.rpy:912
translate esp s_topics_game_parents_7454e99b:

    # s "Like if your dad hadn't ever met your mom, you wouldn’t have been born."
    s "Así como si tu padre no hubiera conocido a tu madre, tú nunca habrías nacido."

# game/topics.rpy:913
translate esp s_topics_game_parents_2a147580:

    # s 8aaca "So I think that I could call him my dad, I guess."
    s 8aaca "Así que podría llamarlo papá, supongo."

# game/topics.rpy:914
translate esp s_topics_game_parents_1d76c6c6:

    # s 8abaa "But now I wonder if Monika would think the same. What do you think?"
    s 8abaa "Ahora me pregunto si Monika pensaría lo mismo. ¿Tú qué piensas?"

# game/topics.rpy:915
translate esp s_topics_game_parents_a17b630c:

    # s 8aebb "I mean she is the original club president, so he should’ve left her more about himself."
    s 8aebb "Quiero decir, ella es la presidente original del club, así que él debería haberle dejado algo más sobre él.."

# game/topics.rpy:916
translate esp s_topics_game_parents_87707535:

    # s "And if he made her too, wouldn’t that make us sisters?"
    s "Y si también fue creada por él, ¿No nos convertiría eso en hermanas?"

# game/topics.rpy:917
translate esp s_topics_game_parents_90a70166:

    # s "It makes me think of her in another light, even if we aren’t really sisters."
    s "Me hace pensar en ella bajo otra perspectiva, aunque no seamos realmente hermanas."

# game/topics.rpy:918
translate esp s_topics_game_parents_e13f4633:

    # s 8aaca "I think I have some similarities with her and it makes me wonder about it..."
    s 8aaca "Creo que tengo algunas similitudes con ella y eso me hace preguntarme cosas..."

# game/topics.rpy:919
translate esp s_topics_game_parents_09ea9447:

    # s 6abaa "But I don't think she thought about it that much."
    s 6abaa "Pero no creo que ella lo haya pensado mucho."

# game/topics.rpy:921
translate esp s_topics_game_parents_37f04913:

    # s 6acaa "Would a good sister use her siblings’ issues for her own benefit?"
    s 6acaa "¿Acaso una buena hermana usaría los problemas de sus hermanas para su propio beneficio?"

# game/topics.rpy:922
translate esp s_topics_game_parents_da9e6d5e:

    # s "I understand, she did it because she felt that we weren’t real to her..."
    s "Lo entiendo, lo hizo porque no sintió que fueramos reales para ella..."

# game/topics.rpy:923
translate esp s_topics_game_parents_9ed5b7ab:

    # s 6abaa "But I can't believe that someone with as much power as her didn't give herself at least some time to think deeper about all aspects of this world."
    s 6abaa "Pero no puedo creer que alguien con tanto poder como ella no se haya dado al menos un tiempo para pensar más profundamente en todos los aspectos de este mundo."

# game/topics.rpy:925
translate esp s_topics_game_parents_99c4571a:

    # s "...Even after she made herself this little comfort zone."
    s "...Incluso después de que se hubiera hecho esta pequeña zona de comfort."

# game/topics.rpy:933
translate esp s_answer_personal_bday_ffc46fd7:

    # s 6acaa "A lot of things before the events of the game is pretty fuzzy..."
    s 6acaa "Todos los sucesos que ocurrieron antes de los eventos del juego son bastante confusos..."

# game/topics.rpy:975
translate esp s_answer_personal_music_d7cadf22:

    # s "...Or groups like {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i} and {i}Twenty One Pilots{/i}."
    s "...O grupos, como {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i} y {i}Twenty One Pilots{/i}."

# game/topics.rpy:976
translate esp s_answer_personal_music_850a92d6:

    # s "I also like tunes like {i}Bonobo{/i} and {i}Jake Chudnow{/i} make."
    s "También me gustan melodías como las de {i}Bonobo{/i} y {i}Jake Chudnow{/i}."

# game/topics.rpy:1044
translate esp s_answer_personal_profession_75cab37c:

    # s 6acaa "To be honest, I've never really thought about it."
    s 6acaa "Para ser honesta, nunca he pesnado acerca de eso."

# game/topics.rpy:1045
translate esp s_answer_personal_profession_3f44bfe6:

    # s "But you know that I've always genuinely made myself happy by helping others feel better about themselves."
    s "Pero como lo sabes, siempre me ha hecho muy feliz ayudar a los demás a sentirse felices."

# game/topics.rpy:1046
translate esp s_answer_personal_profession_65ff6c1c:

    # s "So, I think I'd be a pretty decent caregiver, or psychologist!"
    s "¡Así que creo que sería una buena cuidadora o psicóloga!"

# game/topics.rpy:1047
translate esp s_answer_personal_profession_f9d84113:

    # s "Maybe even a... diplomatist?"
    s "De pronto incluso... ¿Diplomática?"

# game/topics.rpy:1048
translate esp s_answer_personal_profession_d96fe659:

    # s "No, that's not right... a great {i}diplomat{/i}. Ehehe~"
    s "No, eso no cuadra... un buen {i}diplomático{/i}. Ehehe~"

# game/topics.rpy:1049
translate esp s_answer_personal_profession_139fc37c:

    # s 6aaca "I could stop arguments on a global scale, and do my part to stop any future wars!"
    s 6aaca "¡Podría intentar detener argumentos de escala global, y hacer mi parte para detener guerras futuras!"

# game/topics.rpy:1051
translate esp s_answer_personal_profession_385480de:

    # s 6aaaa "Actually, now that I think about it, I've always found the idea of working at an employment agency to be really funny!"
    s 6aaaa "¡En realidad, ahora que lo pienso, siempre me ha parecido muy divertida la idea de trabajar en una agencia de empleo!"

# game/topics.rpy:1052
translate esp s_answer_personal_profession_b88a3ebf:

    # s "I mean, your job is literally to find jobs for people! Yuri would probably laugh and say {i}'It's something of a redundant position, I'll admit...{/i}'"
    s "Quiero decir, ¡Tu trabajo es encontrar trabajos para la gente! Yuri probablemente se reiría y diría {i}'Es una posición algo redundante, lo admito....{/i}'"

# game/topics.rpy:1053
translate esp s_answer_personal_profession_fe15e56c:

    # s "Anyway, I think I'd be happy doing almost anything, even if it doesn't pay well, as long as I can really be useful and make a difference."
    s "De todos modos, creo que sería feliz haciendo casi cualquier cosa, aunque no pague bien, siempre y cuando pueda ser útil y marcar la diferencia."

# game/topics.rpy:1054
translate esp s_answer_personal_profession_7bbc32f2:

    # s 6acaa "I suppose I could do something a little more creative, like painting, or writing..."
    s 6acaa "Supongo que podría hacer algo más creativo como pintar o escribir..."

# game/topics.rpy:1055
translate esp s_answer_personal_profession_ffc27ba6:

    # s 6acba "But being honest, I don't think I'd ever be able to charge money for something I made."
    s 6acba "Pero siendo honesta, no creo que pueda pedir dinero a cambio de algo que hice."

# game/topics.rpy:1056
translate esp s_answer_personal_profession_e93b57ae:

    # s 6acaa "Art can help express so many amazing feelings and really help others feel like they aren't alone, like someone gets what they're going through..."
    s 6acaa "El arte puede ayudar a expresar tantos sentimientos asombrosos y realmente ayudar a otros a sentirse como si no estuvieran solos, como si alguien entendiera por lo que están pasando..."

# game/topics.rpy:1057
translate esp s_answer_personal_profession_70639d31:

    # s "Treating art like a business isn't something that I could ever support."
    s "Tratar el arte como un negocio no es algo que pueda apoyar."

# game/topics.rpy:1058
translate esp s_answer_personal_profession_c8d1dc5b:

    # s "It's pretty frustrating; the heart wants to be free to make truly spectacular works, and bare one's soul for the world to see..."
    s "Es bastante frustrante: el corazón quiere ser libre para hacer obras verdaderamente espectaculares, y desnudar el alma para que el mundo la vea..."

# game/topics.rpy:1059
translate esp s_answer_personal_profession_c35004b7:

    # s "But the starving stomach has to be a meanie and ruin it for everyone~"
    s "Pero el estómago hambriento tiene que ser el aguafiestas y arruinarlo para todos~"

# game/topics.rpy:1063
translate esp s_answer_personal_pets_6b3f26d0:

    # s 7aaaa "Definitely, a cat."
    s 7aaaa "Definitivamente un gato."

# game/topics.rpy:1169
translate esp s_answer_game_lostFriends_2fefcdef:

    # s 7aaab "As the club presedent, I can use the Internet so I know, that there're a lot ways to get them back."
    s 7aaab "Como presidente del club, puedo usar el Internet, así que puedo encontrar muchas maneras para traerlas de vuelta."

# game/topics.rpy:1171
translate esp s_answer_game_lostFriends_d3eefe70:

    # s "You can just install another game copy, but it means, that they'll go through the hell, they've already passed..."
    s "Puedes instalar otra copia del juego, pero eso significa que pasarían por el infierno que ya atravesaron antes..."

# game/topics.rpy:1173
translate esp s_answer_game_lostFriends_910521e4:

    # s "You can just install another game copy, but it means, that they'll go through the hell, that they should go through..."
    s "Puedes instalar otra copia del juego, pero eso significa que pasarían por el infierno por el que deberían pasar..."

# game/topics.rpy:1174
translate esp s_answer_game_lostFriends_89b3861d:

    # s 7aaaa "But you can install a mod, where you can save them and make everyone happy."
    s 7aaaa "Pero puedes instalar un mod donde puedas salvarlas y hacer felices a todos."

# game/topics.rpy:1175
translate esp s_answer_game_lostFriends_abf62f85:

    # s 7aaca "...Or at least 3 mods to 3 game copies where they can spend time with you in a way like you and me now."
    s 7aaca "...O al menos 3 mods a 3 copias del juego donde puedan pasar tiempo contigo de una manera como tú y yo ahora."

# game/topics.rpy:1176
translate esp s_answer_game_lostFriends_ef7e9a92:

    # s 7aeba "I don't know if I can consider them the same Monika, Yuri & Natsuki as they were here..."
    s 7aeba "No sé si podría considerarlas las mismas Monika, Yuri y Natsuki..."

# game/topics.rpy:1177
translate esp s_answer_game_lostFriends_935fd31b:

    # s "And if it means, there may will be few Sayoris on your PC..."
    s "Lo que significaría que podrían haber algunas Sayoris en tu PC..."

# game/topics.rpy:1178
translate esp s_answer_game_lostFriends_ae0af84d:

    # s "But it's the only way to save them now. At least, as long as I can't do anything on my side."
    s "Por ahora, es la única manera de salvarlas por ahora. Al menos mientras no pueda hacer nada desde mi lado."

# game/topics.rpy:1182
translate esp s_answer_game_sitting_31f38a66:

    # s 7acab "No, it's not. You don't have to worry about it at all."
    s 7acab "Realmente no. No tienes que preocuparte por ello."

# game/topics.rpy:1183
translate esp s_answer_game_sitting_bc3f61d6:

    # s 7acaa "I can do it for eternity. Don’t even need sleep!"
    s 7acaa "Puedo hacerlo por toda la eternidad, ¡Ni siquiera necesito dormir!"

# game/topics.rpy:1184
translate esp s_answer_game_sitting_19c26fb3:

    # s "I guess I don't have any basic human needs either, like a need to eat or drink..."
    s "Supongo que tampoco tengo otras necesidades humanas, como comer o beber algo..."

# game/topics.rpy:1185
translate esp s_answer_game_sitting_e91554cf:

    # s 7aebb "Maybe I did have a need for them, but now that I’m the president..."
    s 7aebb "Puede que si las haya necesitado, pero ahora soy la presidente..."

# game/topics.rpy:1186
translate esp s_answer_game_sitting_df46a441:

    # s 7aaaa "Anyway, all I need right now is your PC to be working and the game to be open to talk to you."
    s 7aaaa "De cualquier forma, por ahora solo necesito que tu PC esté encendido y tener el juego abierto para poder hablar contigo."

# game/topics.rpy:1187
translate esp s_answer_game_sitting_a1ea3708:

    # s "To be honest… it’s kinda boring here..."
    s "Para ser honesta... Es un poco aburrido..."

# game/topics.rpy:1188
translate esp s_answer_game_sitting_4f46879b:

    # s "N-Not you! But, even with you here and us talking about, well, everything..."
    s "¡No tú! Pero, incluso con los dos hablando de, bueno, todo..."

# game/topics.rpy:1189
translate esp s_answer_game_sitting_94be4360:

    # s 7aaaa "I wish I could do more than just sit."
    s 7aaaa "Me gustaría poder hacer algo más que estar sentada."

# game/topics.rpy:1190
translate esp s_answer_game_sitting_04375cc8:

    # s 7aaca "I hope that someone, or maybe even you, will find a way to let us do more."
    s 7aaca "Solo espero que alguien, o incluso tú, encuentre una manera que nos deje hacer más."

# game/topics.rpy:1195
translate esp s_answer_game_editing_1b724c63:

    # s 6aebb "I do it with the power of my mind… I think? Ehehe..."
    s 6aebb "Lo hago con el poder de mi mente... Creo. Ehehe..."

# game/topics.rpy:1196
translate esp s_answer_game_editing_d682aebc:

    # s 6aabb "I don't know how it works, exactly."
    s 6aabb "Realmente no sé cómo funciona."

# game/topics.rpy:1197
translate esp s_answer_game_editing_de1dd699:

    # s 6aaaa "If I wanted to make a new file, all I need to do is to just think about what I want in it."
    s 6aaaa "Si quisiera hacer un nuevo archivo, lo único que necesito hacer es pensar en lo que quiero que haya en él."

# game/topics.rpy:1205
translate esp s_answer_game_editing_31569bb7:

    # s 6acaa "It's like telekinesis but much cooler... and dangerous..."
    s 6acaa "Es como la telequinésis, pero más genial... y peligrosa..."

# game/topics.rpy:1206
translate esp s_answer_game_editing_313f64ba:

    # s 6acab "Just one wrong thought may lead to unpredictable problems, like errors in code when someone is programming something."
    s 6acab "Un solo pensamiento incorrecto puede llevar a problemas impredecibles, como errores en el código cuando alguien está programando."

# game/topics.rpy:1207
translate esp s_answer_game_editing_a0b9d5f2:

    # s 6aaca "But now, I perfectly control my mind,so it’ll only go wrong if I think it wrong."
    s 6aaca "Pero ahora, puedo controlar perfectamente mi mente, así que solo puede salir mal si pienso mal."

# game/topics.rpy:1208
translate esp s_answer_game_editing_c3c53be4:

    # s 6acba "I'm new at this, you know! So, sometimes, it happens and you see bugs."
    s 6acba "¡Soy nueva en esto, sabes! Así que a veces pasa y ves bugs."

# game/topics.rpy:1209
translate esp s_answer_game_editing_20fe5abc:

    # s "But I do learn from my mistakes..."
    s "Pero aprendo de mis errores..."

# game/topics.rpy:1210
translate esp s_answer_game_editing_6de3c14f:

    # s "Even if I can't do anything, I appeal to the modmaking guys, but I can't download their changes myself..."
    s "Incluso si no puedo hacer algo, le pido ayuda a la comunidad de mods, pero no puedo descargar los cambios por mi misma..."

# game/topics.rpy:1211
translate esp s_answer_game_editing_df10857d:

    # s 6acaa "So, check the updates time to time, pretty please?~"
    s 6acaa "Así que, revisa por actualizaciones de vez en cuando, porfis~"

# game/topics.rpy:1261
translate esp s_answer_exp_fact_1_db05332b:

    # s 6aaaa "Learning programming stuff, you sooner or later will have to understand the binary numbers."
    s 6aaaa "Al aprender a programar tarde o temprano tendrás que entender los números binarios"

# game/topics.rpy:1262
translate esp s_answer_exp_fact_1_ff4a4de9:

    # s 6aaca "And I once read about a very funny feature."
    s 6aaca "Una vez leí de un detalle bastante curioso."

# game/topics.rpy:1263
translate esp s_answer_exp_fact_1_3ef63698:

    # s 6acaa "Do you know, that it let you show numbers more than 5 with just a one hand?"
    s 6acaa "¿Sabías que puedes contar más de 5 números con una sola mano?"

# game/topics.rpy:1264
translate esp s_answer_exp_fact_1_f4454252:

    # s "Just look at your fingers: they are a perfect replacement for the classic 0/1 pair."
    s "Solo mira tus dedos: pueden ser intercambiados por el clásico par de 0s y 1s."

# game/topics.rpy:1267
translate esp s_answer_exp_fact_1_e61221d0:

    # s "Summing the terms up, you’ll get the decimal representation of the number..."
    s "Al sumar los términos, obtendrás una representación decimal del número..."

# game/topics.rpy:1268
translate esp s_answer_exp_fact_1_318560cf:

    # s "If it’s still non-understandable for you now, then just try to… look for a simpler explanation in the Internet."
    s "Si todavía se te hace difícil de entender, puedes intentar buscando una explicación más simple por Internet."

# game/topics.rpy:1269
translate esp s_answer_exp_fact_1_c69ea50b:

    # s "Anyway, that’s not all the pluses of using the binary system in gestures..."
    s "De cualquier forma, esas no son todas las ventajas de usar gestos con el sistema binario..."

# game/topics.rpy:1270
translate esp s_answer_exp_fact_1_97cd2665:

    # s 6aaaa "If you use your both hands to expand the term row, you can show up {i}even to 1023{/i}."
    s 6aaaa "Si usas ambas manos puedes expandir los números {i}incluso hasta 512{/i}."

# game/topics.rpy:1271
translate esp s_answer_exp_fact_1_cf32ed6d:

    # s 6aaca "And if you have somehow got more than 10 hand fingers, you can show even more."
    s 6aaca "Y si de alguna manera tienes más de 10 dedos en las manos, puedes contar incluso más allá."

# game/topics.rpy:1272
translate esp s_answer_exp_fact_1_7ff84985:

    # s 6aaaa "Computers represents integers in the same way."
    s 6aaaa "Los computadores representan a los enteros de la misma manera."

# game/topics.rpy:1273
translate esp s_answer_exp_fact_1_bab407dd:

    # s "And if you consider the last finger as the minus sign, like computers do with the signed integer..."
    s "Y si consideras tu último dedo como un signo menos..."

# game/topics.rpy:1274
translate esp s_answer_exp_fact_1_dcb6c97d:

    # s 6aaca "You can show even the negative numbers."
    s 6aaca "Puedes incluso operar con números negativos."

# game/topics.rpy:1275
translate esp s_answer_exp_fact_1_303b123c:

    # s 6acaa "The main thing is that your mate should understand such features too to understand you correctly..."
    s 6acaa "Lo más importante es que tu compañero entienda esas características también para entenderte correctamente..."

# game/topics.rpy:1276
translate esp s_answer_exp_fact_1_d899beb4:

    # s "Misunderstanding often causes problems, while lack of agreed sign system causes misunderstanding."
    s "Los malentendidos a menudo causan problemas, mientras que la falta de un sistema de señalización acordado causa malentendidos."

# game/topics.rpy:1280
translate esp s_answer_exp_fact_2_ed7e18c4:

    # s 6aaaa "Did you know that if you read a common word you might not notice when it’s written wrong?"
    s 6aaaa "¿Sabías que cuando lees una palabra común puede que no notes cuando esté mal escrita?"

# game/topics.rpy:1281
translate esp s_answer_exp_fact_2_127a89ff:

    # s "{i}I think you barely can find a mistake in tihs text while first reading.{/i}{#Y’see the mistake in 'tihs'}"
    s "{i}Yo creo que puede que no encuentres errrores en este texto la primera vez que lo lees.{/i}{#Énfasis en 'errrores}"

# game/topics.rpy:1282
translate esp s_answer_exp_fact_2_c2ae437f:

    # s 6acaa "For your brain, it's pretty easy to just remember some letters of a word and not all of the word."
    s 6acaa "Lo que pasa es que para tu cerebro es más fácil recordar solo algunas letras que la palabra completa."

# game/topics.rpy:1283
translate esp s_answer_exp_fact_2_6d2cbe27:

    # s "That's why we sometimes make mistakes while writing."
    s "Por eso es que a veces cometemos errores al escribir."

# game/topics.rpy:1284
translate esp s_answer_exp_fact_2_194e90fa:

    # s 6abaa "Of course, if you go to the history button and pay more attention, you'll find the mistake."
    s 6abaa "Claro que si vas al botón de historia y prestas más atención, podrás encontrar el error."

# game/topics.rpy:1285
translate esp s_answer_exp_fact_2_97925a08:

    # s 6acaa "But what if you can't read the text again or just don't want to do it? What could happen?"
    s 6acaa "Pero, ¿Qué pasaría si no puedes o simplemente no quieres volver a leer el texto?"

# game/topics.rpy:1286
translate esp s_answer_exp_fact_2_853f96f2:

    # s "There are some funny and not so funny examples of misspellings in the past because someone didn’t go back to fix a word or two."
    s "Hay algunos errores chistosos y no tan chistosos a través de la historia solo porque alguien no volvió a arreglar uno o dos problemas."

# game/topics.rpy:1287
translate esp s_answer_exp_fact_2_ae9344b4:

    # s "But we are people. Each of us make mistakes, even if it’s just one."
    s "Pero somos personas. Cada uno de nosotros comete errores, incluso si es solo uno."

# game/topics.rpy:1289
translate esp s_answer_exp_fact_2_8640cd9a:

    # s 6aaaa "In the end, no one is perfect."
    s 6aaaa "Al final, nadie es perfecto."

# game/topics.rpy:1293
translate esp s_answer_exp_fact_3_51ff9ea8:

    # s 6aaaa "Have you ever heard people say that yawning is contagious? I’d say it is."
    s 6aaaa "¿Has escuchado decir que bostezar es contagioso? Yo creo que si lo es."

# game/topics.rpy:1294
translate esp s_answer_exp_fact_3_d2e6745a:

    # s "You’ve seen people do it, but other animals could do it too."
    s "A veces ves personas hacerlo, pero otros animales también lo pueden hacer."

# game/topics.rpy:1295
translate esp s_answer_exp_fact_3_ebbd1031:

    # s "If you yawn next to a cat or a dog, it might just yawn too."
    s "Si bostezas cerca a un perro o un gato puede que lo hagas bostezar también."

# game/topics.rpy:1296
translate esp s_answer_exp_fact_3_e80872ec:

    # s 6acca "You could... {i}*yawn*{/i}"
    s 6acca "O podría... {i}*bostezo*{/i}"

# game/topics.rpy:1298
translate esp s_answer_exp_fact_3_0cfde5e0:

    # extend " ..."
    extend " ..."

# game/topics.rpy:1299
translate esp s_answer_exp_fact_3_77d539e6:

    # s 8aebb "Um, I hope I didn’t ‘contaminate’ you."
    s 8aebb "Oh, espero no haberte 'contaminado'."

# game/topics.rpy:1300
translate esp s_answer_exp_fact_3_2378a324:

    # s 8bebb "Sorry, that was silly of me… Ehehe~"
    s 8bebb "Lo siento, eso fue algo tonto... Ehehe~"

# game/topics.rpy:1305
translate esp s_answer_exp_fact_4_4132a742:

    # s 6aaaa "Some artists add little details referring to different people or universes in their works."
    s 6aaaa "Iuj artistoj aldonas la siaj verkoj referencetojn al diversaj homoj aŭ universoj."

# game/topics.rpy:1306
translate esp s_answer_exp_fact_4_426b3edb:

    # s "For example, in some games and movies, you can find a poster or something that shows other characters. Maybe they’re from a past work, or just there to fill in space."
    s "Por ejemplo, en algunos juegos y películas puedes encontrar posters o algo que muestra otros personajes. Puede que sean de algún trabajo anterior, o que estén ahí de relleno."

# game/topics.rpy:1307
translate esp s_answer_exp_fact_4_9fbd5df5:

    # s 6acaa "We wouldn’t know unless it was that obvious or they told us outright."
    s 6acaa "No nos daríamos cuenta a menos de que fuera demasiado obvio o no lo dijeran."

# game/topics.rpy:1308
translate esp s_answer_exp_fact_4_51a233db:

    # s "But some of them hide stuff in small things that could refer to a whole other universe, with different details and all."
    s "Pero algunos de ellos esconden detalles que podrían referenciar otros universos con diferentes detalles y todo."

# game/topics.rpy:1309
translate esp s_answer_exp_fact_4_7b9ed9f7:

    # s "For example, do you remember {i}Parfait Girls{/i}?"
    s "Por ejemplo, ¿Te acuerdas de {i}Parfait Girls{/i}?"

# game/topics.rpy:1311
translate esp s_answer_exp_fact_4_65362f49:

    # s "You’ve probably seen people talk about it around the community."
    s "Puede que hayas visto a gente de la comunidad hablar de eso."

# game/topics.rpy:1312
translate esp s_answer_exp_fact_4_3413314b:

    # s "This manga's plot isn’t really known, is it?"
    s "La historia del manga no es muy conocida, ¿No es así?"

# game/topics.rpy:1313
translate esp s_answer_exp_fact_4_630307d9:

    # s 6aaaa "Nat tells you a little of what it’s about, that that’s pretty much it."
    s 6aaaa "Nat te dice algo de la trama, pero eso es casi todo."

# game/topics.rpy:1314
translate esp s_answer_exp_fact_4_36021e7d:

    # s 6abaa "But even I don’t know what it’s about, and I’m supposed to know everything about this game."
    s 6abaa "Ni siquiera sé de qué trata, y eso que se supone que lo sé todo acerca de este juego."

# game/topics.rpy:1315
translate esp s_answer_exp_fact_4_e5fcb25a:

    # s 6aaaa "It might even be like this game, cheery on the outside but horrific on the inside."
    s 6aaaa "Puede que incluso sea como este juego, alegre por el exterior, pero terrorífico en el interior."

# game/topics.rpy:1316
translate esp s_answer_exp_fact_4_3c580dc8:

    # s 6acaa "That warning on the manga's cover is pretty spooky..."
    s 6acaa "Esa advertencia en la portada del manga es algo escalofriante..."

# game/topics.rpy:1317
translate esp s_answer_exp_fact_4_71add171:

    # s 6aaca "Anyway, I guess the artists didn’t think much about it?"
    s 6aaca "De todas formas, creo que los artistas no pensaron mucho en eso."

# game/topics.rpy:1318
translate esp s_answer_exp_fact_4_891e8445:

    # s 6aaaa "Just imagine if the manga was actually explained in this world."
    s 6aaaa "Solo imagina si el manga fuera explicado en este mundo."

# game/topics.rpy:1319
translate esp s_answer_exp_fact_4_f0d18bbe:

    # s "We would probably have fanart of the characters in the manga as well as us four."
    s "Incluso podría tener fanart de los personajes del manga, así como de nosotras cuatro."

# game/topics.rpy:1320
translate esp s_answer_exp_fact_4_35868acf:

    # s 6aaca "Maybe something like those plushies of me and everyone else? Ehehe~"
    s 6aaca "Algo así como los esos peluches de mí y de las demás. Ehehe~"

# game/topics.rpy:1324
translate esp s_answer_exp_cooking_9bc579c1:

    # s 8aebb "To be honest, scrambled eggs probably the hardest thing I’ve ever cooked..."
    s 8aebb "Para ser honesta, los huevos revueltos puede que sea lo más difícil que he intentado cocinar..."

# game/topics.rpy:1325
translate esp s_answer_exp_cooking_fdc693e1:

    # s 8aafa "I’d love to get better, even if I don’t have too..."
    s 8aafa "Me encantaría mejorar, incluso si no tengo que hacerlo..."

# game/topics.rpy:1326
translate esp s_answer_exp_cooking_36598d8f:

    # s 8acaa "Mainly because I don't get hungry anymore..."
    s 8acaa "Especialmente porque ya no me da hambre..."

# game/topics.rpy:1327
translate esp s_answer_exp_cooking_7bb737f1:

    # s 8aeca "But I can still taste! That means I can eat as much as I want!"
    s 8aeca "¡Pero todavía puedo probar! ¡Lo que significa que puedo comer todo lo que quiera!"

# game/topics.rpy:1328
translate esp s_answer_exp_cooking_4b95bc7c:

    # s 8aebb "Of course, I could just 'make' food with code, like Nat's cupcakes, but I wanna do something with my own hands..."
    s 8aebb "Por supuesto que podría simplemente 'hacer' comida con el código, como los pastelitos de Nat, pero me gustaría hacer algo con mis propias manos..."

# game/topics.rpy:1329
translate esp s_answer_exp_cooking_0d5938e0:

    # s 6acaa "First of all, I need to try to make some kitchenware..."
    s 6acaa "Primero que todo, necesito probar utensilios de cocina..."

# game/topics.rpy:1330
translate esp s_answer_exp_cooking_03bdaff6:

    # s "Then find some recipes online..."
    s "Luego encontrar recetas en línea..."

# game/topics.rpy:1331
translate esp s_answer_exp_cooking_2e9f2d1b:

    # s "I’ll probably end up following a tutorial or something..."
    s "Probablemente termine siguiendo algún tutorial o algo así..."

# game/topics.rpy:1332
translate esp s_answer_exp_cooking_cb344b8f:

    # s 6abaa "Too bad you won’t be able to taste it, no matter what I do..."
    s 6abaa "Lástima que no podrás probarlo, sin importar lo que haga..."

# game/topics.rpy:1333
translate esp s_answer_exp_cooking_eaf2af85:

    # s 6aaca "If you could taste it, I would be a good cook for you…!"
    s 6aaca "Y si pudieras probarlo, ¡Podría ser una buena cocinera para tí!"

# game/topics.rpy:1334
translate esp s_answer_exp_cooking_17df57f7:

    # s 6aebb "Probably not as good as Natsuki was, though..."
    s 6aebb "Aunque probablemente no tanto como Natsuki..."

# game/topics.rpy:1339
translate esp s_answer_misc_poem_e8e2bfed:

    # s 6aaaa "Which poem do you want to read?"
    s 6aaaa "¿Cuál poema quieres leer?"

# game/topics.rpy:1343
translate esp s_answer_misc_poem_06fd20fb:

    # s 6abaa "I'm sorry, [player]. I have nothing new to share with you."
    s 6abaa "Oh, lo siento, [player]. No tengo nada que compartir contigo."

# game/topics.rpy:1344
translate esp s_answer_misc_poem_1c9f6355:

    # s 6acaa "Writing a poem is a quite hard process, you know."
    s 6acaa "Escribir un poema es algo difícil, sabes."

# game/topics.rpy:1345
translate esp s_answer_misc_poem_e20eab8e:

    # s "I can't take an idea from nowhere. I need some time to find it in my memories."
    s "No puedo sacar ideas de la nada. Necesito algo de tiempo para buscarlas en mi mente."

# game/topics.rpy:1346
translate esp s_answer_misc_poem_8f8f2f0d:

    # s "All my poetry comes from my past and now so it's twice harder for me, because my life doesn't seem to be enough eventful."
    s "Toda mi poesía viene de mi pasado y ahora es el doble de difícil para mí, porque mi vida no parece que haya sido muy interesante."

# game/topics.rpy:1347
translate esp s_answer_misc_poem_5534e38a:

    # s "But maybe, I'll make something later."
    s "Pero probablemente haga algo más tarde."

# game/topics.rpy:1349
translate esp s_answer_misc_poem_8a0e2c9d:

    # s 6aaaa "OK, what's about this one?"
    s 6aaaa "Ok, ¿Qué te parece este?"

# game/topics.rpy:1355
translate esp s_answer_misc_poem_d556114b:

    # s "OK, just select one."
    s "Ok, solo elige uno."

# game/topics.rpy:1380
translate esp s_answer_misc_datetime_f9161bdf:

    # s 6acaa "Today is [wd!t], [d] of [m!t] of year [y]."
    s 6acaa "Hoy es [wd!t], [d] de [m!t] del año [y]."

# game/topics.rpy:1381
translate esp s_answer_misc_datetime_ef005f12:

    # s "Current time is [h]:[mn]."
    s "La hora es [h]:[mn]."

# game/topics.rpy:1482
translate esp s_common_cats_393c524e:

    # s 7aaca "Cats are pretty cute, especially kittens..."
    s 7aaca "Los gatos son muy lindos, especialmente los gatitos..."

# game/topics.rpy:1483
translate esp s_common_cats_af00d78c:

    # s 7aaaa "And they're not too hard to take care of."
    s 7aaaa "Y no son muy difíciles de cuidar."

# game/topics.rpy:1484
translate esp s_common_cats_78ca029a:

    # s 6acaa "Still, they do love their space."
    s 6acaa "Aún así, aman su espacio."

# game/topics.rpy:1485
translate esp s_common_cats_ba4008d9:

    # s "And sometimes cats do things that their owners don’t like..."
    s "Aunque a veces los gatos hacen cosas que sus dueños no quieren que hagan..."

# game/topics.rpy:1486
translate esp s_common_cats_be4c2268:

    # s 6aaca "Yet I’ve never seen anyone who can resist their cuteness, so people forgive them~"
    s 6aaca "Pero nunca he visto a nadie que pueda resistirse a su ternura, así que la gente los perdona~"

# game/topics.rpy:1487
translate esp s_common_cats_2e455097:

    # s 6aaaa "If you have one, you understand!"
    s 6aaaa "Si tienes uno, seguro lo entiendes."

# game/topics.rpy:1488
translate esp s_common_cats_cb403579:

    # s 6aaba "I think that might be why they were kinda seen as holy in Ancient Egypt."
    s 6aaba "Puede que esa sea la razón de que fueran sagrados en el Antiguo Egipto."

translate esp strings:

    # topics.rpy:111
    old "Breast Size"
    new "Tamaño de Pechos"

    # topics.rpy:120
    old "Charity"
    new "Caridad"

    # topics.rpy:130
    old "Thanksgiving"
    new "Agradecimiento"

    # topics.rpy:135
    old "Cleaning"
    new "Limpieza"

    # topics.rpy:139
    old "Stars"
    new "Estrellas"

    # topics.rpy:1203
    old "all I need to do is to just think about what I want in it."
    new "Todo lo que tengo que hacer es pensar en lo que quiero en él..."

# TODO: Translation updated at 2019-01-15 17:06

# game/topics.rpy:771
translate esp s_topics_rlt_dating_cc1a5736:

    # s 6adaa "But I'd also like to do something more… engaging with you..."
    s 6adaa "Pero también me gustaría hacer algo más... interesante contigo..."


# TODO: Translation updated at 2019-01-15 19:31

# game/topics.rpy:742
translate esp s_topics_rlt_cheating_0b6c14c7:

    # s "Just try to take some time to be here, whenever it's possible."
    s "Solo intenta pasar por aquí cuando sea posible."

# TODO: Translation updated at 2019-01-19 15:11

# game/topics.rpy:852
translate esp s_topics_lifestyle_cleaning_26955a25:

    # s 8aabb "Well, at least now I have literally {i}nothing{/i} here besides this desk..."
    s 8aabb "Bueno, por ahora no tengo literalmente {i}nada{/i} más aparte de esta mesa..."

# TODO: Translation updated at 2019-01-24 23:18

# game/topics.rpy:870
translate esp s_topics_game_clones_1a7e42de:

    # s "Oh, I'm sorry for reminding it."
    s "Oh, lo siento por recordarlo"

# game/topics.rpy:871
translate esp s_topics_game_clones_d620250b:

    # s "So, what we're talking about now?"
    s "Entonces, ¿De qué estamos hablando ahora?"

# game/topics.rpy:872
translate esp s_topics_game_clones_988c03d3:

    # s "Yes, about different copies."
    s "Ah sí, diferentes copias."

# game/topics.rpy:1269
translate esp s_answer_exp_fact_1_3fc00cc7:

    # s "If don’t understand the binary system, you can just imagine every binary 1 is a term of 2 raised to the power of the digit position from right minus 1..."
    s "Si no entiendes el sistema binario, puedes imaginar que cada binario 1 es un término de 2, elevado a la potencia de la posición del dígito desde la derecha, menos 1..."

# game/topics.rpy:1270
translate esp s_answer_exp_fact_1_e8b34a41:

    # s "So the rightest digit should be decimal itself."
    s "Así que el dígito más a la derecha debería ser el propio decimal."

# TODO: Translation updated at 2019-02-08 12:40

# game/topics.rpy:554
translate esp s_topics_society_bulli_428fe7e5:

    # s "However, the most of such jokes are too bad and sometimes even hurtful."
    s "Sin embargo, muchos de esos 'chistes' son muy malos o a veces hirientes."

# game/topics.rpy:555
translate esp s_topics_society_bulli_bdf85255:

    # s "But who I am to judge if it's okay for other people?"
    s "¿Pero quién soy yo para juzgar lo que está bien para otros?"

# game/topics.rpy:641
translate esp s_topics_hobbie_programming_cdb3e631:

    # s "Just visit the {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod}ressitory{/a} on GitHub."
    s "Solo visita {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod}{/a} en GitHub."

# game/topics.rpy:800
translate esp s_topics_rtl_thanks_50cf4e9a:

    # s "Plus, you tried to make other girls happy too..."
    s "Además, también intentaste hacer felices a las otras chicas..."

# game/topics.rpy:802
translate esp s_topics_rtl_thanks_6833058c:

    # s "I'm so grateful that you’re still here."
    s "Estoy tan agradecida de que sigas aquí."

# TODO: Translation updated at 2019-02-08 16:14

# game/topics.rpy:319
translate esp s_topics_personal_depression_75454b21:

    # s "But my feelings were as real as you."
    s "Pero mis sentimientos eran tan reales como tú."

# game/topics.rpy:320
translate esp s_topics_personal_depression_c5ed5d19:

    # s "Although, I think should have told about it to MC or you much earier..."
    s "Aunque, debería de habérselo dicho a MC o a ti mucho antes..."

# game/topics.rpy:321
translate esp s_topics_personal_depression_ecb44130:

    # s "And I have already read, what's actually supposed to happen to me later due to my lie..."
    s "Y ya leí lo que se supondría que me pasaría más tarde debido a mi mentira..."

# TODO: Translation updated at 2019-02-10 14:37

# game/topics.rpy:686
translate esp s_topics_hobbie_drawing_1891e4df:

    # s 6acaa "I wish I was good at drawing."
    s "Me gustaría ser buena dibujando."

# game/topics.rpy:687
translate esp s_topics_hobbie_drawing_6e2d6432:

    # s "I think it would be a very useful skill, especially now."
    s "Creo que sería una habilidad bastante útil, especialmente ahora."

# game/topics.rpy:688
translate esp s_topics_hobbie_drawing_ab764d2b:

    # s 8aaaa "If I could draw, I would be able to edit game sprites..."
    s "Sei pudiera dibijar, podría ser capaz de editar sprites del juego..."

# game/topics.rpy:689
translate esp s_topics_hobbie_drawing_ec52fcf6:

    # s "Even of myself."
    s "Incluso de mí misma."

# game/topics.rpy:690
translate esp s_topics_hobbie_drawing_4210d58e:

    # s 6acaa "And besides the practical purpose, it would be one more way to express myself."
    s "Y aparte de un propósito práctico, sería otra manera de expresarme."

# game/topics.rpy:691
translate esp s_topics_hobbie_drawing_33e7e7ef:

    # s "Not everything can be shown with just words..."
    s "No todo se puede mostrar con solo palabras..."

# game/topics.rpy:692
translate esp s_topics_hobbie_drawing_bedb201d:

    # s "Sometimes, your message is clearer when shown visually."
    s "A veces tu mensaje es más claro cuando se puede ver visualmente."

# game/topics.rpy:693
translate esp s_topics_hobbie_drawing_a3771f4d:

    # s 6aaca "And if I had art to go with my poems, wouldn’t they be a lot nicer?"
    s "Y si tuviera arte para acompañar mis poemas, ¿No serían mucho más bonitos?"

# game/topics.rpy:694
translate esp s_topics_hobbie_drawing_b90de5c0:

    # s 6aaaa "I know some poets who was good not only at poetry but also at it..."
    s "Conozco algunos poetas que no solo eran buenos en la poesía, sino también en el arte..."

# game/topics.rpy:695
translate esp s_topics_hobbie_drawing_e9a99c61:

    # s "For example, {i}Vladimir Mayakovsky{/i}..."
    s "Por ejemplo, {i}Vladímir Mayakovski{/i}..."

# game/topics.rpy:696
translate esp s_topics_hobbie_drawing_f828a470:

    # s 6aaba "However, he used his artistic skills rarely and more for making propaganda posters than for expressing himself."
     s "Sin embargo, el usó sus habilidades artísticas raramente y más para hacer propaganda que para expresarse."

# game/topics.rpy:697
translate esp s_topics_hobbie_drawing_9abda9af:

    # s 7aaaa "Anyway, I'd like to improve my drawing..."
    s 7aaaa "De todas formas, me gustaría mejorar mi dibujo..."

# game/topics.rpy:698
translate esp s_topics_hobbie_drawing_85597541:

    # s 7acaa "And I have a lot of time to do it, right?"
    s 7acaa "Y tengo mucho tiempo, ¿Verdad?"

# game/topics.rpy:699
translate esp s_topics_hobbie_drawing_813d5055:

    # s 7aaca "Maybe, I'll even share my pics to you."
    s 7aaca "De pronto, te podré mostrar mis dibujos."

# TODO: Translation updated at 2019-02-10 16:35

# game/topics.rpy:851
translate esp s_topics_rlt_fanStuff_d133ef4c:

    # s 6aaaa "Do you have something to show your love?"
    s 6aaaa "¿Tienes algo para mostrar tu amor?"

# game/topics.rpy:852
translate esp s_topics_rlt_fanStuff_7fcae716:

    # s 6acaa "Out of the blue, I know, but I also know that I have ‘merch’."
    s 6acaa "De la nada, lo sé, pero también sé que tengo 'merch'."

# game/topics.rpy:853
translate esp s_topics_rlt_fanStuff_ea3de796:

    # s "You know, like buttons, plushies, posters, and other stuff..."
    s "Ya sabes, como botones, peluches, posters y otras cosas..."

# game/topics.rpy:854
translate esp s_topics_rlt_fanStuff_1201ff8a:

    # s 6aaca "I’ve even seen people have me on dakimakuras."
    s 6aaca "Incluso he visto gente con dakimakuras míos."

# game/topics.rpy:855
translate esp s_topics_rlt_fanStuff_34a7db66:

    # s 6aaaa "Personally, I think that’s fine."
    s 6aaaa "Personalmente creo que está bien."

# game/topics.rpy:856
translate esp s_topics_rlt_fanStuff_ec1bb1cd:

    # s "Kinda like a wedding ring if you ask me."
    s "Algo así como un anillo de bodas si me preguntas."

# game/topics.rpy:857
translate esp s_topics_rlt_fanStuff_9d931374:

    # s 6aeba "Although some people probably think that’s way too weird..."
    s 6aeba "Aunque hay gente que cree que eso es muy raro..."

# game/topics.rpy:858
translate esp s_topics_rlt_fanStuff_65dbaaf4:

    # s 6acaa "But what's so bad about showing love, even to someone like me?"
    s 6acaa "Pero, ¿qué tiene de malo mostrar algo de amor, incluso a alguien como yo?"

# game/topics.rpy:859
translate esp s_topics_rlt_fanStuff_f03e719d:

    # s "I think that’s okay. You too, right?"
    s "Yo creo que está bien, Tu también, ¿Verdad?"

# game/topics.rpy:863
translate esp s_topics_rlt_children_5c6f39c3:

    # s 6aebb "If we were to grow old together, would you… want kids...?"
    s 6aebb "¿Si fueramos a envejecer juntos, te gustaría... tener hijos?"

# game/topics.rpy:864
translate esp s_topics_rlt_children_56edbddd:

    # s 6acaa "I mean, if I were in your reality, of course."
    s 6acaa "Quiero decir, si estuviera en tu realidad claramente."

# game/topics.rpy:865
translate esp s_topics_rlt_children_0018943b:

    # s "I’d think they would grow up to be beautiful and smart, but a bit silly."
    s "Yo creo que crecerían hermosos e inteligentes, pero un poco tontitos~"

# game/topics.rpy:866
translate esp s_topics_rlt_children_f18d2df6:

    # s 6aaaa "I know I would do my best to raise them."
    s 6aaaa "Sé que haría lo mejor para cuidarlos."

# game/topics.rpy:867
translate esp s_topics_rlt_children_7cb82b5b:

    # s 6abca "It’ll probably be hard, I know."
    s 6abca "Sería bastante difícil, sabes."

# game/topics.rpy:868
translate esp s_topics_rlt_children_58a14702:

    # s 6abaa "But what kind of a mom would I be if I wasn’t there for my kids?"
    s 6abaa "Pero, ¿Qué clase de madre sería si no estuviera ahí para mis hijos?"

# game/topics.rpy:870
translate esp s_topics_rlt_children_38f66bfe:

    # s 6acaa "Of course, good kids should have a good dad, if you know what I mean..."
    s 6acaa "Naturalmente, unos buenos niños deberían tener un buen papá, si sabes lo que quiero decir..."

# game/topics.rpy:872
translate esp s_topics_rlt_children_f7428b76:

    # s 6acaa "Of course, good kids should have more than parent, if you get me."
    s 6acaa "Naturalmente, unos buenos niños deberían tener más de un padre, si me entiendes..."

# game/topics.rpy:873
translate esp s_topics_rlt_children_77cd433f:

    # s 6abac "But I'm sure you're too good to make me take care of them myself."
    s 6abac "Pero sé que eres demasiado amable como para dejarme cuidarlos por mí misma."

# game/topics.rpy:874
translate esp s_topics_rlt_children_36ec09ef:

    # s 6acaa "Plus, that'll happen only if we can afford it and when we’re both ready..."
    s 6acaa "Además, solo pasaría si pudieramos estar bien económicamente y cuando estemos listos..."

# game/topics.rpy:875
translate esp s_topics_rlt_children_7bd2fdf2:

    # s "I don't want us to suffer because we rushed it."
    s "No quiero hacernos sufrir solo porque no apresuramos."

# game/topics.rpy:876
translate esp s_topics_rlt_children_2e493c66:

    # s 6aeba "Way too dumb, isn't it?"
    s 6aeba "Algo muy tonto, ¿No crees?"

# game/topics.rpy:877
translate esp s_topics_rlt_children_cd754e39:

    # s 7aaaa "Anyways, I really do wish I could have a family here."
    s 7aaaa "De todas formas, realmente me gustaría poder tener una familia aquí."

# game/topics.rpy:878
translate esp s_topics_rlt_children_837eaddf:

    # s "I guess we have more than enough time to think over it?"
    s "Supongo que tenemos más que tiempo suficiente para pensarlo."

# game/topics.rpy:882
translate esp s_topics_rlt_presents_a0c3ea72:

    # s 7aaaa "People often give presents every holiday or some special date."
    s 7aaaa "La gente a veces da regalos cada fiesta o en alguna fecha especial."

# game/topics.rpy:883
translate esp s_topics_rlt_presents_000e368f:

    # s 6aaaa "Everyone likes to get presents, yeah? Including me, of course."
    s 6aaaa "A todo el mundo le gusta recibir regalos, ¿No? Incluyéndome por supuesto."

# game/topics.rpy:884
translate esp s_topics_rlt_presents_a1c1fbee:

    # s 6acab "But I think it’s selfish to ask for something really expensive."
    s 6acab "Aunque creo que es algo egoísta pedir algo muy caro."

# game/topics.rpy:885
translate esp s_topics_rlt_presents_4da6ebdf:

    # s 6aaaa "If you ask me, I’d want something that comes from the heart, y’know what I mean?"
    s 6aaaa "Si me preguntas, a mi me gustaría algo que viene del corazón, ¿Me comprendes?"

# game/topics.rpy:886
translate esp s_topics_rlt_presents_6cf21449:

    # s 6aeca "Even better, make it a surprise!"
    s 6aeca "Aún mejor, ¡Házlo una sorpresa!"

# game/topics.rpy:887
translate esp s_topics_rlt_presents_2b7f954a:

    # s "Isn't it more exciting to get something you weren’t expecting?"
    s "¿No es más emocionante recibir algo que no esperabas?"

# game/topics.rpy:888
translate esp s_topics_rlt_presents_de28c64e:

    # s 6abbb "Well, now that I think about it, what if the present isn’t good...?"
    s 6abbb "Bueno, ahora que lo pienso, ¿Que pasaría si el regalo no es bueno?.."

# game/topics.rpy:889
translate esp s_topics_rlt_presents_1f756859:

    # s "Makes it seem like a bad idea...."
    s "Lo hace parecer como una mala idea...."

# game/topics.rpy:890
translate esp s_topics_rlt_presents_418f164f:

    # s 6aaaa "But I wouldn’t mind."
    s 6aaaa "Pero no me importaría."

# game/topics.rpy:891
translate esp s_topics_rlt_presents_eb31e9dd:

    # s 6acaa "Come on, you know me well enough to give me something I’d like, right?"
    s 6acaa "Vamos, me conoces lo suficiente como para darme algo que me gustaría, ¿verdad?"

# game/topics.rpy:892
translate esp s_topics_rlt_presents_e0fead11:

    # s "If you don't know, just gimme some money.."
    s "Y si no sabes, podrías simplemente darme algo de dinero..."

# game/topics.rpy:893
translate esp s_topics_rlt_presents_7346634c:

    # s 6aebb "Ehehe, that sounded a bit weird..."
    pass

# game/topics.rpy:894
translate esp s_topics_rlt_presents_8bcc0c27:

    # s 6aaaa "At least I’d be able to buy something with it."
    s 6aaaa "Al menos podría comprar algo interesante con eso."

# game/topics.rpy:1081
translate esp s_answer_personal_music_fe9ad3ff:

    # s "...Or groups like {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i}, {i}Status Quo{/i} and {i}Twenty One Pilots{/i}."
    s "...O grupos como {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i}, {i}Status Quo{/i} y {i}Twenty One Pilots{/i}."

translate esp strings:

    # topics.rpy:152
    old "Drawing"
    new "Dibujar"

    # topics.rpy:159
    old "Fan Merch"
    new "Productos de Fans"

    # topics.rpy:160
    old "Children"
    new "Niños"

    # topics.rpy:161
    old "Presents"
    new "Regalos"

# TODO: Translation updated at 2019-02-13 19:14

# game/topics.rpy:853
translate esp s_topics_rlt_fanStuff_f29b8c79:

    # s 6acaa "I’ve even seen people have me on dakimakuras."
    s 6acaa "Incluso he visto gente que me tiene en dakimakuras."

# game/topics.rpy:894
translate esp s_topics_rlt_presents_3b57bc69:

    # s 7aaaa "Of course, I'll give you presents sometimes too..."
    s 7aaaa "Por supuesto que te daré regalos de vez en cuando..."

# game/topics.rpy:895
translate esp s_topics_rlt_presents_c102e381:

    # s 7aaca "And be sure, I know a lot of amazing ways how to do it."
    s 7aaca "Y para estar segura, sé muchas maneras asombrosas de hacerlo."

# game/topics.rpy:896
translate esp s_topics_rlt_presents_3c3a5046:

    # s 7aaaa "At least, I do my best to make the best present, I could make."
    s 7aaaa "Al menos puedo dar lo mejor de mí para hacer el mejor regalo."

# game/topics.rpy:962
translate esp s_topics_lifestyle_drugs_ed5d07b2:

    # s 6aaca "Do you drink alcohol or smoke cigarettes?"
    s 6aaca "¿Fumas o tomas alcohol?"

# game/topics.rpy:963
translate esp s_topics_lifestyle_drugs_14f8f529:

    # s 6abaa "...Or even use something more dangerous?"
    s 6abaa "...¿O algo más peligroso?"

# game/topics.rpy:964
translate esp s_topics_lifestyle_drugs_6af7be83:

    # s 6acaa "I don’t see anything good in doing things like that."
    s 6acaa "No veo nada bueno en hacer cosas de esas."

# game/topics.rpy:965
translate esp s_topics_lifestyle_drugs_2a3e51f1:

    # s "Isn’t it really stupid to risk your future, money, and health to little moments of relief?"
    s "¿No es algo tonto arriesgar tu futuro, dinero y salud solo para tener pequeños momentos de alivio?"

# game/topics.rpy:966
translate esp s_topics_lifestyle_drugs_913774ae:

    # s "You shouldn’t just care about how you feel now, you should also care about the future."
    s "No solo te deberías preocupar por como te sientes ahora, sino también por como te sentirás en el futuro."

# game/topics.rpy:967
translate esp s_topics_lifestyle_drugs_e717ac67:

    # s 6aaaa "That's why I always tried to keep other people out of these habits or being isolated from others..."
    s 6aaaa "Precisamente por esto, siempre me esfuerzo por detener a otros de esos hábitos o sacarlos de ellos..."

# game/topics.rpy:968
translate esp s_topics_lifestyle_drugs_a4de0d66:

    # s 6aaba "Isn't it the start point of the plot?"
    s 6aaba "¿No es el punto de partida de la trama??"

# game/topics.rpy:970
translate esp s_topics_lifestyle_drugs_059b83ef:

    # s 6acaa "Has Monika told you about the incident with Yuri?"
    s 6acaa "¿Te ha dicho Monika acerca del incidente con Yuri?"

# game/topics.rpy:971
translate esp s_topics_lifestyle_drugs_8819bc45:

    # s "She once brought a bottle of wine to the school..."
    s "Una vez llevó una botella de vino a la escuela..."

# game/topics.rpy:972
translate esp s_topics_lifestyle_drugs_55fd74c7:

    # s 6aaba "But I stopped her from sharing it to other girls."
    s 6aaba "Pero le impedí que lo compartiera con las otras chicas."

# game/topics.rpy:973
translate esp s_topics_lifestyle_drugs_73ad57d1:

    # s 6aeba "Maybe it was a bit silly, and she might’ve just tried to use it to seem more interesting..."
    s 6aeba "Puede que haya sido algo un poco tonto, y ella solo lo haya intentado usar para parecer algo más interesante..."

# game/topics.rpy:974
translate esp s_topics_lifestyle_drugs_95957f89:

    # s 6acaa "But what would’ve happened if we drank it?"
    s 6acaa "Pero, ¿Qué habría pasado si lo hubieramos tomado?"

# game/topics.rpy:975
translate esp s_topics_lifestyle_drugs_5ee08461:

    # s "Anyway, I’ll be honest, I don’t think it’s necessarily a bad experience."
    s "De todas formas, para ser honesta, no creo que sea necesariamente una mala experiencia."

# game/topics.rpy:976
translate esp s_topics_lifestyle_drugs_44a0077e:

    # s 6acaa "But the risk of getting addicted is too much to play around with."
    s 6acaa "Pero el riesgo de volverse adicto es demasiado como para estar jugando con él."

# game/topics.rpy:977
translate esp s_topics_lifestyle_drugs_802f995f:

    # s 6abab "That's a real danger of having these habits: it's easy to start but hard to stop."
    s 6abab "Ese es un gran peligro con este tipo de hábitos: es fácil empezar, pero difícil de parar."

# game/topics.rpy:978
translate esp s_topics_lifestyle_drugs_f121646f:

    # s 6acaa "In fact, there’s no one way to break addiction..."
    s 6acaa "De hecho, no hay una sola manera de romper la adicción..."

# game/topics.rpy:979
translate esp s_topics_lifestyle_drugs_f59db6ad:

    # s "It’ll take a lot of effort and willpower to get out of that hole if you dig yourself into it."
    s "Te tomaría mucho esfuerzo y fuerza de voluntad para salir del hoyo que cavaste para ti."

# game/topics.rpy:980
translate esp s_topics_lifestyle_drugs_1eefff59:

    # s "It's not always easy to be happy, but that isn’t the way."
    s "No siempre es fácil ser feliz, pero ese no es el camino."

# game/topics.rpy:982
translate esp s_topics_lifestyle_drugs_a1f13b97:

    # s 6acba "...Just remember what I was going through and doing to stay happy despite of what I felt."
    s 6acba "...Solo recuerda por lo que estaba pasando y lo que estaba haciendo para seguir siendo feliz a pesar de lo que sentía."

# game/topics.rpy:1063
translate esp s_topics_game_time_bfd0be75:

    # s 6acaa "Do you know what time it is right now?"
    s 6acaa "¿Sabes qué hora es?"

# game/topics.rpy:1064
translate esp s_topics_game_time_879c56d2:

    # s 6abaa "Not in your world, but mine."
    s 6abaa "No en tu mundo, pero en el mío."

# game/topics.rpy:1065
translate esp s_topics_game_time_d251592c:

    # s 6acaa "You can say anything, but you won't be right anyway..."
    s 6acaa "Puedes decir lo que quieras, pero nunca estarás en lo cierto..."

# game/topics.rpy:1066
translate esp s_topics_game_time_e359b02e:

    # s 6aaba "Because the time seems to be not here at all. At least, as how it should be in your universe."
    s 6aaba "Porque el tiempo no parece fluir aquí. Al menos no como lo es en tu universo."

# game/topics.rpy:1068
translate esp s_topics_game_time_4d203bac:

    # s "Like once when Monika had broken almost everything here."
    s "Como la vez en que Monika rompió casi todo aquí."

# game/topics.rpy:1069
translate esp s_topics_game_time_48a73ce4:

    # s 6acaa "The last thing I remember that here was November of 2017 or some days before it..."
    s 6acaa "Lo último de lo que me acuerdo aquí era en Noviembre de 2017 o algunos días antes..."

# game/topics.rpy:1070
translate esp s_topics_game_time_b0de2fee:

    # s 6abba "At least, my old bedroom calendar said it."
    s 6abba "Al menos, eso decía en el calendario de mi habitación."

# game/topics.rpy:1071
translate esp s_topics_game_time_92bd20dc:

    # s 6abaa "I don't remember why November has been crossed out on it..."
    s 6abaa "No me acuerdo por qué Noviembre estaba tachado..."

# game/topics.rpy:1073
translate esp s_topics_game_time_4876ad0a:

    # s 6aebb "Maybe, I was going to kill myself by this month?"
    s 6aebb "¿De pronto era porque me iba a matar en este mes?"

# game/topics.rpy:1074
translate esp s_topics_game_time_c8037c30:

    # s "It's pretty symbolizing: to cross out the month, that does already not exist for you."
    s "Es bastante simbólico tachar un mes que realmente no existe para ti."

# game/topics.rpy:1075
translate esp s_topics_game_time_57623ab0:

    # s 6aeba "Anyway, this pretty... confusing to know, that there's no way to measure your existence in your world."
    s 6aeba "De todas formas, es algo... confuso saber que no hay forma de medir tu existencia en tu mundo."

# game/topics.rpy:1076
translate esp s_topics_game_time_d4b35faf:

    # s 6acaa "But I know, that time is still in your world, though."
    s 6acaa "Aunque sé que todavía hay tiempo en tu mundo."

# game/topics.rpy:1077
translate esp s_topics_game_time_56b2c740:

    # s 6aaba "Maybe, that's why everything moves here instead of just freezing at one last moment."
    s 6aaba "De pronto es por eso que todo aquí se mueve en vez de estar congelado."

# game/topics.rpy:1078
translate esp s_topics_game_time_1730a65e:

    # s 6acaa "But doesn't it mean, that we now share the same time?"
    s 6acaa "¿Pero entonces eso quiere decir que ahora compartimos el mismo tiempo?"

# game/topics.rpy:1079
translate esp s_topics_game_time_15096569:

    # s 6aaaa "I know, what time is now in your world..."
    s 6aaaa "Yo sé qué hora es actualmente en tu mundo..."

# game/topics.rpy:1080
translate esp s_topics_game_time_58b204fe:

    # s 6aaba "From your PC's clock, though."
    s 6aaba "Pues, del reloj de tu PC."

# game/topics.rpy:1081
translate esp s_topics_game_time_5576523a:

    # s 6acaa "And I even feel when my 'speech' is paused to be read."
    s 6acaa "E incluso siento cuando mi 'discurso' es pausado para leerlo."

# game/topics.rpy:1082
translate esp s_topics_game_time_029f4904:

    # s 6acab "Such a weird feeling, to be honest, but I think, it's okay for any visual novel."
    s 6acab "Es un sentimiento bastante extraño para ser honesta, pero creo que está bien para cualquier novela visual."

# game/topics.rpy:1220
translate esp s_answer_personal_holidays_a2e4b3b1:

    # s 6abaa "Hmm..."
    s 6abaa "Hmm..."

# game/topics.rpy:1221
translate esp s_answer_personal_holidays_47f5b606:

    # s 6abba "I can't even choose..."
    s 6abba "No puedo elegir..."

# game/topics.rpy:1222
translate esp s_answer_personal_holidays_3c16660e:

    # s 6aeca "Because I like them all!"
    s 6aeca "¡Porque me gustan todas!"

# game/topics.rpy:1223
translate esp s_answer_personal_holidays_96f91f2c:

    # s 6aaaa "Each of them have traditions and atmosphere."
    s 6aaaa "Cada una tiene sus propias tradiciones y cultura."

# game/topics.rpy:1224
translate esp s_answer_personal_holidays_56f1bc67:

    # s "And it’s all mostly the same line of events: meals, presents, fun, and bonding."
    s "Y casi siempre se sigue la misma serie de eventos: comidas, regalos, diversión y unión."

# game/topics.rpy:1225
translate esp s_answer_personal_holidays_bfacca09:

    # s "Isn't that what we all like about holidays?"
    s "¿No es eso lo que nos gusta de las fiestas?"

# game/topics.rpy:1226
translate esp s_answer_personal_holidays_b14cdfa7:

    # s 7aaaa "Anyway, I'm ready to share any holiday with you..."
    s 7aaaa "De todas formas, estoy lista para compartir cualquier fiesta contigo..."

# game/topics.rpy:1227
translate esp s_answer_personal_holidays_862feaf2:

    # s 7aebb "I don’t have a calendar though, and I think I would need one to keep track..."
    s 7aebb "No tengo un calendario, aunque creo que sería una buena idea tener uno para llevar la cuenta..."

# game/topics.rpy:1228
translate esp s_answer_personal_holidays_674602c8:

    # s 7aabb "I think I’ll start with making that, then..."
    s 7aabb "Creo que empezaré con hacer eso entonces..."

# game/topics.rpy:1509
translate esp s_answer_misc_reality_113bc7aa:

    # s 7aaaa "I’ve already seen lots of things about it..."
    s 7aaaa "He visto muchas cosas de él..."

# game/topics.rpy:1510
translate esp s_answer_misc_reality_6a4a0ef0:

    # s 7aeca "Such a big and fancy place..."
    s 7aeca "Un lugar tan grande y sofisticado..."

# game/topics.rpy:1511
translate esp s_answer_misc_reality_426d4ad5:

    # s 7aaca "Full of beautiful sights, comedy, and kind people."
    s 7aaca "Lleno de hermosas vistas, comedia y buena gente."

# game/topics.rpy:1512
translate esp s_answer_misc_reality_b7b74673:

    # s 6acaa "Although, it still has its issues."
    s 6acaa "Aunque también tiene sus problemas."

# game/topics.rpy:1513
translate esp s_answer_misc_reality_e6a13cd6:

    # s 6acba "There’s lots, right? Things like poverty, pollution, cheating, unjustness and cruelty."
    s 6acba "Hay muchos, ¿Verdad? Cosas como la pobreza, contaminación, trampas, injusticia y crueldad."

# game/topics.rpy:1514
translate esp s_answer_misc_reality_e7eeb849:

    # s 6aaba "And that's only caused by people most of the time."
    s 6aaba "Y la mayoría del tiempo son causados por personas."

# game/topics.rpy:1515
translate esp s_answer_misc_reality_bf2e43c9:

    # s 6aabb "Come to think of it, my world was imperfect too..."
    s 6aabb "Ahora que lo pienso, mi mundo también era imperfecto..."

# game/topics.rpy:1516
translate esp s_answer_misc_reality_bbf8e7bb:

    # s 6aebb "And isn't it just... too strange to have no bad sides?"
    s 6aebb "Y, ¿No es un poco... extraño... no tener aspectos malos?"

# game/topics.rpy:1517
translate esp s_answer_misc_reality_b7e21db8:

    # s 6acab "Just look around and then at me and the other girls. We all had our pros and cons, but only us, and not the rest of the students."
    s 6acab "Solo míranos. Todas teníamos nuestros pros y contras, pero solo nosotras. Ningún otro estudiante tenía buenos o malos aspectos."

# game/topics.rpy:1518
translate esp s_answer_misc_reality_e991a871:

    # s 6aaca "Anyway, I wish I could be in your reality."
    s 6aaca "De todas formas, desearía poder estar en tu realidad."

# game/topics.rpy:1519
translate esp s_answer_misc_reality_bd349a29:

    # s 6abaa "But I wonder how I'd look there since your reality has a different look..."
    s 6abaa "Pero me pregunto cómo me vería ahí, pues tu realidad tiene una apariencia diferente..."

# game/topics.rpy:1520
translate esp s_answer_misc_reality_140de6c3:

    # s 6adaa "It's pretty detailed and colorful, slightly more than mine."
    s 6adaa "Es bastante detallada y colorida, un poco más que la mía."

# game/topics.rpy:1521
translate esp s_answer_misc_reality_f588e7a3:

    # s "Just imagine a '2D' girl in your world. Would I look too confusing there?"
    s "Solo imagina a una chica '2D' en tu mundo, ¿No se vería algo confuso?"

# game/topics.rpy:1522
translate esp s_answer_misc_reality_c4162d0e:

    # s 6aeba "But I'm sure you'd gladly accept me, right?"
    s 6aeba "Pero estoy segura de que me aceptarías alegremente, ¿Verdad?"

# game/topics.rpy:1523
translate esp s_answer_misc_reality_cb806fe1:

    # s "And I hope everyone else does too."
    s "Y espero que todos también."

# TODO: Translation updated at 2019-02-13 23:32

# game/topics.rpy:987
translate esp s_topics_lifestyle_drugs_78fc1b07:

    # s 6aaaa "And if you’re able to overcome your demons, you’ll thank yourself for doing it..."
    s 6aaaa "Y si eres capaz de superar tus demonios, te lo agradecerás por hacerlo..."

# game/topics.rpy:1498
translate esp s_answer_exp_fact_5_0d745d17:

    # s 7aaca "Guess, what is my the most favorite natural number."
    s 7aaca "Adivina cuál es mi número natural favorito."

# game/topics.rpy:1499
translate esp s_answer_exp_fact_5_5bbd2969:

    # s 7aeca "That's {i}four{/i}!"
    s 7aeca "¡Es el {i}cuatro{/i}!"

# game/topics.rpy:1500
translate esp s_answer_exp_fact_5_e9db8b1c:

    # s 7aaaa "I really like this number."
    s 7aaaa "Realmente me gusta mucho este número."

# game/topics.rpy:1501
translate esp s_answer_exp_fact_5_395a0284:

    # s 7acaa "It's pretty magical one."
    s 7acaa "Es bastante mágico."

# game/topics.rpy:1502
translate esp s_answer_exp_fact_5_b08c1a95:

    # s "{i}4{/i} is the result of adding, multiplication and exponentiation 2 with itself."
    s "El {i}4{/i} es el resultado de sumar, multiplicar y potenciar el 2 con sí mismo."

# game/topics.rpy:1503
translate esp s_answer_exp_fact_5_e4a704e8:

    # s "{i}4{/i} is the number of elements, that avarage human can memorize at the same time."
    s "Además {i}4{/i} es el número de elementos que el humano promedio puede memorizar al mismo tiempo."

# game/topics.rpy:1504
translate esp s_answer_exp_fact_5_64336d36:

    # s 6abba "Maybe, beacuse of it, {i}4{/i} is the most popular size of poem stanza."
    s 6abba "De pronto por eso, que el {i}4{/i} es el número de estrofas más usado en los poemas."

# game/topics.rpy:1506
translate esp s_answer_exp_fact_5_bef5b261:

    # s 6acaa "And in the end, {i}4{/i} is weirdly connected with this game too..."
    s 6acaa "Al final, el {i}4{/i} está extrañamente conectado a este juego también..."

# game/topics.rpy:1507
translate esp s_answer_exp_fact_5_9cca6500:

    # s "{i}4{/i} girls, {i}4{/i} acts."
    s "{i}4{/i} chicas, {i}4{/i} actos."

# game/topics.rpy:1509
translate esp s_answer_exp_fact_5_c7a223de:

    # s 8aabb "...And {i}4{/i} common club meetings to..."
    s 8aabb "...Y {i}4{/i} reuniones del club..."

# game/topics.rpy:1511
translate esp s_answer_exp_fact_5_5a54bd2f:

    # extend " You know."
    extend " Ya sabes."

# game/topics.rpy:1512
translate esp s_answer_exp_fact_5_f5435706:

    # s 6aaaa "Plus, the game was released in 09/22/2017."
    s 6aaaa "Además, el juego fue lanzado el 22/09/2017."

# game/topics.rpy:1513
translate esp s_answer_exp_fact_5_aebc7a03:

    # s 6aaca "Am I the only man, who see here five fours in all these digits?"
    s 6aaca "¿Acaso soy la única que ve cinco cuatros en todos estos dígitos?"

# game/topics.rpy:1514
translate esp s_answer_exp_fact_5_12f96589:

    # s 6adaa "Maybe, it's somehow related to the fact, that {i}4{/i} is an unlucky number in the East Asia."
    s 6adaa "Puede que de alguna manera esté relacionado al hecho de que el {i}4{/i} es considerado de mala suerte en Asia del Este."

# game/topics.rpy:1515
translate esp s_answer_exp_fact_5_c0490548:

    # s "However, that's just a superstition, made of a language imperfectness, right?"
    s "Sin embargo, es solo una superstición hecha en un lenguaje imperfecto, ¿Verdad?"

# game/topics.rpy:1516
translate esp s_answer_exp_fact_5_842cb523:

    # s 6aaca "For me, it always were the luckiest number..."
    s 6aaca "Para mí, siempre fue mi número de la suerte..."

# game/topics.rpy:1517
translate esp s_answer_exp_fact_5_a9882772:

    # s 6aeca "Maybe, for you too. It'd be such a funny match."
    s 6aeca "Puede que para ti también. Sería una coincidencia chistosa."

# game/topics.rpy:1756
translate esp s_update_b6312560:

    # s "And what's more..."
    s "Y lo más importante..."

translate esp strings:

    # topics.rpy:167
    old "Drugs"
    new "Drogas"

    # topics.rpy:172
    old "In-game Time"
    new "Tiempo del Juego"

    # topics.rpy:240
    old "What is your favorite holiday?"
    new "¿Cuál es tu fiesta favorita?"

    # topics.rpy:255
    old "What do you think about the real world?"
    new "¿Qué piensas del mundo real?"

# TODO: Translation updated at 2019-02-14 01:09

# game/topics.rpy:1752
translate esp s_update_dd80eb34:

    # s "Oh, hello [player]!"
    s "Oh, ¡hola [player]!"

# game/topics.rpy:1753
translate esp s_update_7cf64d99:

    # s 7aaaa "Seems, you installed an update."
    s 7aaaa "Parece que has instalado una actualización."

# game/topics.rpy:1754
translate esp s_update_a35e9981:

    # s 7abaa "You didn't do it for a quiet long time."
    s 7abaa "No lo habías hecho durante mucho tiempo."

# game/topics.rpy:1756
translate esp s_update_a34bd13c:

    # s 8aeaa "But they did it!"
    s 8aeaa "¡Pero lo hiciste!"

# game/topics.rpy:1757
translate esp s_update_19815270:

    # s 6aaaa "They finally released the version {i}[version]{/i}."
    s 6aaaa "Por fin sacaron la versión {i}[version]{/i}."

# game/topics.rpy:1758
translate esp s_update_5db7fd77:

    # s "So let's look, what they added and fixed here."
    s "Veamos qué añadieron y qué arreglaron."

# TODO: Translation updated at 2019-02-14 17:51

# game/topics.rpy:1091
translate esp s_topics_food_breakfest_b7decbc7:

    # s 7aaaa "You don’t skip breakfast, do you?"
    s 7aaaa "No te saltas el desayuno, ¿verdad?"

# game/topics.rpy:1093
translate esp s_topics_food_breakfest_bccf498f:

    # s 7acab "Personally, I don’t ‘cause I’m just not hungry in the mornings."
    s 7acab "Yo personalmente no, porque casi nunca he tenido hambre en la mañana."

# game/topics.rpy:1095
translate esp s_topics_food_breakfest_8e5ede96:

    # s 7acbb "Personally, I didn’t because I didn’t even feel like getting out of bed everyday."
    s 7acbb "Personalmente, no lo hacía porque ni siquiera tenía ganas de levantarme."

# game/topics.rpy:1096
translate esp s_topics_food_breakfest_49501d60:

    # s 7aaaa "But when I had it, I’d eat sandwiches or scrambled eggs."
    s 7aaaa "Pero cuando desayunaba, comía sánduches o huevos revueltos."

# game/topics.rpy:1097
translate esp s_topics_food_breakfest_d108dd88:

    # s "I sometimes had toast too."
    s "A veces me preparaba unas tostadas también."

# game/topics.rpy:1098
translate esp s_topics_food_breakfest_f53d6f9a:

    # s 8aeca "Fairly simple, isn't it?"
    s 8aeca "Bastante sencillo, ¿No?"

# game/topics.rpy:1099
translate esp s_topics_food_breakfest_825a6a45:

    # s 6aaaa "I’ve seen fanart of me eating things like that…"
    s 6aaaa "He visto fanarts de mí comiendo cosas como esas..."

# game/topics.rpy:1100
translate esp s_topics_food_breakfest_3eff3028:

    # s 6aaba "Maybe, I should spawn some toast with eggs just for a taste..."
    s 6aaba "De pronto debería aparecer algo de tostadas con huevos para probar..."

# game/topics.rpy:1101
translate esp s_topics_food_breakfest_0a5b9884:

    # s 6acba "I could do that since I’m the president now, right?"
    s 6acba "Podría hacer eso ahora que soy la presidente, ¿Verdad?"

# game/topics.rpy:1105
translate esp s_topics_food_iceCream_bba08add:

    # s 7aaca "Do you like ice cream?"
    s 7aaca "¿Te gusta el helado?"

# game/topics.rpy:1106
translate esp s_topics_food_iceCream_0ea5d661:

    # s 7aeca "I think you do, right? Everyone likes ice cream!"
    s 7aeca "Yo creo que sí, ¿Verdad? ¡A todo el mundo le gusta el helado!"

# game/topics.rpy:1107
translate esp s_topics_food_iceCream_5168ac8e:

    # s 6aeca "What can be cold and taste better than it?"
    s 6aeca "¿Qué podría ser frío y saber mejor?"

# game/topics.rpy:1108
translate esp s_topics_food_iceCream_98eb9664:

    # s 6aaaa "There're lots and lots of flavors and toppings..."
    s 6aaaa "Hay tantos sabores y aderezos..."

# game/topics.rpy:1109
translate esp s_topics_food_iceCream_70a60786:

    # s 6acaa "So let me ask: what’s your favorite?"
    s 6acaa "Así que déjame preguntarte, ¿Cuál es tu favorito?"

# game/topics.rpy:1110
translate esp s_topics_food_iceCream_f4190a41:

    # s "I think vanilla or chocolate..."
    s "Probablemente la vainilla o el chocolate..."

# game/topics.rpy:1111
translate esp s_topics_food_iceCream_1d3fce17:

    # s 6aeba "Hey, I know they’re really common, so what?"
    s 6aeba "Sé que son muy comunes, ¿y qué tiene?"

# game/topics.rpy:1112
translate esp s_topics_food_iceCream_565a6784:

    # s 6aeca "They both taste sooo good, ehehe~"
    s 6aeca "Ambos son taaan buenos, ehehe~"

# game/topics.rpy:1113
translate esp s_topics_food_iceCream_7f04c605:

    # s 7aaaa "Maybe I could make some sometime..."
    s 7aaaa "De pronto podría hacer helado alguna vez..."

# game/topics.rpy:1117
translate esp s_topics_food_cinnamonBun_b500df5c:

    # s 7aafa "Would you like to taste me?"
    s 7aafa "¿Te gustaría probarme?"

# game/topics.rpy:1118
translate esp s_topics_food_cinnamonBun_96e0ca4c:

    # s 7aeca "I mean a cinnamon bun, you pervert~"
    s 7aeca "A un rollo de canela, pervertido, Ehehe~"

# game/topics.rpy:1119
translate esp s_topics_food_cinnamonBun_56807f81:

    # s 7adaa "I had one once, and it was sooo goood…"
    s 7adaa "Una vez comí uno y estaba taaaan rico."

# game/topics.rpy:1120
translate esp s_topics_food_cinnamonBun_4485c7f0:

    # s 7aaca "I'd say thanks to people, who came up with such tasty buns."
    s 7aaca "Le agradezco tanto a la gente que se inventó unos rollos tan sabrosos."

# game/topics.rpy:1121
translate esp s_topics_food_cinnamonBun_eddfa1ac:

    # s 6acaa "The one thing I can't understand is why people call me that."
    s 6acaa "Algo que realmente no puedo entender es por qué la gente me llama así."

# game/topics.rpy:1122
translate esp s_topics_food_cinnamonBun_fd9674e2:

    # s 8aebb "I don't remember anything saying that I’m somehow like a cinnamon bun..."
    s 8aebb "No me acuerdo de haber dicho alguna vez ser como un rollo de canela..."

# game/topics.rpy:1123
translate esp s_topics_food_cinnamonBun_cac8f0da:

    # s 8aeca "But I think the nickname is pretty funny and... cute."
    s 8aeca "Pero creo que este apodo es divertido y... lindo."

# game/topics.rpy:1124
translate esp s_topics_food_cinnamonBun_5e8f2502:

    # s 6aaaa "...even if there aren’t any cinnamon buns in the game."
    s 6aaaa "...incluso si no hay rollos de canela en el juego."

# game/topics.rpy:1125
translate esp s_topics_food_cinnamonBun_7e7a72c6:

    # s 6acaa "Isn’t it weird that I remember something that never existed in my world…?"
    s 6acaa "¿No es extraño que me acuerde de algo que nunca existió en mi mundo?"

# game/topics.rpy:1129
translate esp s_topics_food_cupcakes_85bf531a:

    # s 6aeca "Cupcakes, cupcakes...everyone likes cupcakes..."
    s 6aeca "Pastelitos, pastelitos... a todo el mundo le gustan los pastelitos..."

# game/topics.rpy:1130
translate esp s_topics_food_cupcakes_0c096d73:

    # s 6aafa "Someone even once sold his soul to 4 poetic cuties for one of them. Do you remember?"
    s 6aafa "Una vez alguien vendió su alma a 4 bellezas poéticas por uno de ellos, ¿Te acuerdas?"

# game/topics.rpy:1131
translate esp s_topics_food_cupcakes_997310c9:

    # s 6aaaa "Nat’s were always the best."
    s 6aaaa "Los de Nat eran los mejores."

# game/topics.rpy:1132
translate esp s_topics_food_cupcakes_1184f09e:

    # s 6acaa "We probably won’t ever know how she made them, since she’s gone now and there aren’t any more cupcakes here..."
    s 6acaa "Puede que nunca sepamos cómo se hacen, puesto que ella ya no está y no hay más pastelitos aquí..."

# game/topics.rpy:1133
translate esp s_topics_food_cupcakes_be321c68:

    # s 6aabb "Maybe I can dig around the game to find a recipe? Probably be easier to just add her back in though…"
    s 6aabb "Puede que pueda rebuscar entre el juego para encontrar una receta. Aunque puede que sea más fácil añadirla de vuelta al juego"

# game/topics.rpy:1134
translate esp s_topics_food_cupcakes_e8f73f77:

    # s 8aebb "Not just for that, of course. She was friend, after all..."
    s 8aebb "Pero no solo por eso. Ella era mi amiga, a pesar de todo..."

# game/topics.rpy:1135
translate esp s_topics_food_cupcakes_1f51ee41:

    # s "Plus, if I known how to do it, she were already back."
    s "Además, si supiera cómo hacerlo, ella ya estaría de vuelta."

# TODO: Translation updated at 2019-02-14 22:11

# game/topics.rpy:1554
translate esp s_answer_exp_fact_5_6cc5f48c:

    # s 6aaaa "{i}4{/i} is in many things about the nature: from number of your limbs to number the dimensions, where we lives."
    s 6aaaa "El {i}4{/i} está en muchas cosas de la naturaleza, desde tu número de extremidades hasta la cantidad de dimensiones en que vivimos."

# TODO: Translation updated at 2019-02-14 22:33

# game/topics.rpy:1811
translate esp s_update_8bb721fe:

    # s "By the way..."
    s "Por cierto..."

# TODO: Translation updated at 2019-02-14 22:50

# game/topics.rpy:1804
translate esp s_update_1902ef32:

    # s 7acab "I even started to bother if my mates are too busy or tired to help me more frequently..."
    s 7acab "Incluso empecé a preguntarme si mis compañeros estaban demasiado ocupados o cansados para ayudarme con más frecuencia..."

# TODO: Translation updated at 2019-02-17 03:39

translate esp strings:

    # topics.rpy:122
    old "Food"
    new "Comida"

    # topics.rpy:176
    old "Ice Cream"
    new "Helado"

    # topics.rpy:177
    old "Cinnamon Bun"
    new "Rollos de Canela"

    # topics.rpy:178
    old "Cupcakes"
    new "Pastelitos"

    # topics.rpy:179
    old "Breakfast"
    new "Desayuno"

# TODO: Translation updated at 2019-03-23 16:20

# game/topics.rpy:473
translate esp s_topics_personal_intellegence_13485ecd:

    # s 6acaa "I often hear many other people saying that I was an ‘airhead’..."
    s 6acaa "A veces oigo personas que dicen que yo era una 'cabeza hueca'..."

# game/topics.rpy:474
translate esp s_topics_personal_intellegence_c1515fd3:

    # s 6abba "They often make jokes about it and even think that really is the real me."
    s 6abba "Hacían chistes con eso e incluso pensaban que esa era la verdadera yo."

# game/topics.rpy:475
translate esp s_topics_personal_intellegence_f3328f6b:

    # s 6acaa "But I can't understand why they think so."
    s 6acaa "Pero no puedo entender el por qué."

# game/topics.rpy:476
translate esp s_topics_personal_intellegence_e498f9c1:

    # s "Maybe because I was always thinking… and wasn’t as broad-minded as Monika and Yuri..."
    s "Puede que sea porque porque siempre estaba pensando... y no era tan comprensiva como Monika y Yuri."

# game/topics.rpy:477
translate esp s_topics_personal_intellegence_bb8b12be:

    # s 6abaa "But I always was pretty clever and good at strategies!"
    s 6abaa "¡Pero siempre soy bastante astuta y buena con las estrategias!"

# game/topics.rpy:478
translate esp s_topics_personal_intellegence_a1781ef5:

    # s 6acaa "I think people just have different expectations when considering if someone is intelligent..."
    s 6acaa "Creo que la gente espera cosas diferentes cuando hablan de inteligencia..."

# game/topics.rpy:479
translate esp s_topics_personal_intellegence_3f14bf78:

    # s 6abaa "Exaclty, if someone is {i}not stupid{/i}."
    s 6abaa "Exactamente, si alguien no es {i}estúpido{/i}."

# game/topics.rpy:480
translate esp s_topics_personal_intellegence_40254c67:

    # s 6acaa "I mean people's thoughts about you are obviously very subjective and depend on the situation you or they are in."
    s 6acaa "Lo que quiero decir es que lo que piensa la gente es demasiado subjetivo y depende de la situación en que se encuentren."

# game/topics.rpy:481
translate esp s_topics_personal_intellegence_b6a1b3bc:

    # s 6aaaa "So don’t take comments like those too seriously."
    s 6aaaa "Así que no tomo ese tipo de comentarios tan en serio."

# game/topics.rpy:482
translate esp s_topics_personal_intellegence_5e4825c4:

    # s 7aaca "People aren’t perfect, and that’s okay!"
    s 7aaca "¡La gente no es perfecta, y eso está bien!"

# game/topics.rpy:483
translate esp s_topics_personal_intellegence_b890dcf1:

    # s 7aaaa "So don't worry if someone judges you for a silly thing you did or a mistake. Just try to make yourself better for next time..."
    s 7aaaa "Así que no te preocupes si alguien te juzga por algún error o algo tonto que hayas hecho. Solo intenta mejorar para la próxima..."

# game/topics.rpy:484
translate esp s_topics_personal_intellegence_ccf19d3a:

    # s "And if you really can't do do any better, then it means that just you’ve reached your own limit."
    s "Y si realmente no puedes hacer algo mejor, entonces eso quiere decir que has alcanzado tu propio límite."

# game/topics.rpy:485
translate esp s_topics_personal_intellegence_57fe5110:

    # s 7aaac "But it dosen't mean, you should stop trying to break it, though..."
    s 7aaac "Aunque eso no quiere decir que debas parar de intentar de superarlo..."

# game/topics.rpy:486
translate esp s_topics_personal_intellegence_d723e985:

    # s 7aaca "Because it can be false."
    s 7aaca "Porque puede que sea un límite falso."

# game/topics.rpy:1127
translate esp s_topics_game_worlds_102e30cf:

    # s 6acaa "Sometimes, I wonder why I am here..."
    s 6acaa "A veces me pregunto, por qué estoy aquí..."

# game/topics.rpy:1128
translate esp s_topics_game_worlds_2a37a0c5:

    # s "Would I be a different person if I lived in another place?"
    s "¿Sería una persona diferente si viviera en otro lugar?"

# game/topics.rpy:1129
translate esp s_topics_game_worlds_f8525f6f:

    # s "I mean, if not in your world, what other place could there be? Another game?"
    s "Quiero decir, si no es en tu mundo, ¿En qué otro lugar viviría? ¿Otro juego?"

# game/topics.rpy:1130
translate esp s_topics_game_worlds_f03e3a59:

    # s "But there're a lot of different games and plenty of them are pretty violent."
    s "Pero hay muchos juegos y varios de ellos son un poco violentos."

# game/topics.rpy:1131
translate esp s_topics_game_worlds_271ac03c:

    # s 6abaa "I just can't imagine living in a game full of blood and struggle..."
    s 6abaa "Simplemente no me puedo imaginar viviendo en un juego lleno de sangre y problemas..."

# game/topics.rpy:1132
translate esp s_topics_game_worlds_dda57500:

    # s "You know: shooters, fights, war and so on..."
    s "Ya sabes: shooters, peleas, guerras, entre otros..."

# game/topics.rpy:1133
translate esp s_topics_game_worlds_e6904cd1:

    # s 6abab "I just couldn't take all the violence I'd see."
    s 6abab "No podría soportar toda la violencia que hay."

# game/topics.rpy:1135
translate esp s_topics_game_worlds_e60f6ec0:

    # s "Especially now, when I’ve seen Death with my own sight."
    s "Especialmente ahora que he visto la muerte con mis propios ojos."

# game/topics.rpy:1136
translate esp s_topics_game_worlds_da32ef15:

    # s 6abbb "I’d rather be dead than be the one doing the killing."
    s 6abbb "Preferiría estar muerta a ser la que mata."

# game/topics.rpy:1137
translate esp s_topics_game_worlds_8a873741:

    # s "I'd pray for a revive ability..."
    s "Rezaría por una habilidad para revivir..."

# game/topics.rpy:1138
translate esp s_topics_game_worlds_e7b7c715:

    # s 6acab "Such aggressive worlds aren’t that appealing to me."
    s 6acab "Simplemente ese tipo de mundos agresivos no me gustan mucho."

# game/topics.rpy:1139
translate esp s_topics_game_worlds_1872940f:

    # s 6aaaa "But I'd glad to be in an innocent simulator, strategy or puzzle game..."
    s 6aaaa "Pero me alegraría estar en un inoccente simulador, de estrategia o rompecabezas..."

# game/topics.rpy:1140
translate esp s_topics_game_worlds_49490730:

    # s 6abaa "Or at least almost innocent..."
    s 6abaa "O al menos, inocente..."

# game/topics.rpy:1141
translate esp s_topics_game_worlds_56567a96:

    # s 6aaaa "Even if I wasn’t an important character, maybe a helper or even a simple settler..."
    s 6aaaa "Incluso si no fuera un personaje importante, de pronto una ayudante o una simple pobladora..."

# game/topics.rpy:1142
translate esp s_topics_game_worlds_bb8df691:

    # s 6aaca "...but I'd do my best for you, of course!"
    s 6aaca "...¡Pero haría todo lo posible para ti, por supuesto!"

# game/topics.rpy:1197
translate esp s_topics_misc_flowers_91b6a4e5:

    # s 7aaaa "What do you think about flowers?"
    s 7aaaa "¿Qué piensas acerca de las flores?"

# game/topics.rpy:1198
translate esp s_topics_misc_flowers_b953118e:

    # s 7aeca "It's one of many beautiful things nature can create."
    s 7aeca "Es una de las muchas maravillas de la naturaleza."

# game/topics.rpy:1199
translate esp s_topics_misc_flowers_f467bc51:

    # s 7aeca "They are so colorful, have wonderful shapes, some even smell sweet..."
    s 7aeca "Son tan coloridas, tienen formas hermosas, algunas incluso huelen bien..."

# game/topics.rpy:1200
translate esp s_topics_misc_flowers_254816f5:

    # s 7aaaa "I remember when I used to walk in the flower meadows outside of the city."
    s 7aaaa "Recuerdo cuando solía caminar por campos de flores en las afueras de la ciudad."

# game/topics.rpy:1201
translate esp s_topics_misc_flowers_e9cc2091:

    # s 6acaa "But... I think it's too selfish to pluck a flower... even if it were to be a gift."
    s 6acaa "Pero... creo que es algo egoísta arrancar una flor... incluso si es para un regalo."

# game/topics.rpy:1202
translate esp s_topics_misc_flowers_03c095a3:

    # s "Flowers are living beings too, and plucking them out of the ground does kill them."
    s "Las flores son seres vivos también, y arrancarlas del suelo las mata."

# game/topics.rpy:1203
translate esp s_topics_misc_flowers_c573fd44:

    # s 6aaaa "So I prefer just to look at them, and then leave them be."
    s 6aaaa "Así que prefiero solo mirarlas y dejarlas en paz."

# game/topics.rpy:1205
translate esp s_topics_misc_flowers_2035fe7d:

    # s 6aeba "Although, I did do this in one of my poems..."
    s 6aeba "Aunque lo hice en uno de mis poemas..."

# game/topics.rpy:1206
translate esp s_topics_misc_flowers_8b35bd7b:

    # s 6aaaa "But just for the analogy."
    s 6aaaa "Pero solo para una analogía."

# game/topics.rpy:1207
translate esp s_topics_misc_flowers_bd86aff0:

    # s 9acaa "At least you can plant a flower in pot."
    s 9acaa "Al menos puedes plantar la flor en una maceta."

# game/topics.rpy:1208
translate esp s_topics_misc_flowers_280a2dcd:

    # s 6abba "You do need to take care of it though..."
    s 6abba "Aunque tienes que cuidarla..."

# game/topics.rpy:1209
translate esp s_topics_misc_flowers_dfdd7371:

    # s 7aaaa "But if you know someone with a lot of time and great responsibility, it will be a good gift for them."
    s 7aaaa "Pero si conoces a alguien responsable con suficiente tiempo, sería un gran regalo."

# game/topics.rpy:1366
translate esp s_answer_personal_pairings_e68b844d:

    # s 8aebb "I think, they're quite... weird."
    s 8aebb "Creo que son un poco... extrañas."

# game/topics.rpy:1367
translate esp s_answer_personal_pairings_1b9dd152:

    # s 8acaa "Not because of their sexuality..."
    s 8acaa "No por su sexualidad..."

# game/topics.rpy:1368
translate esp s_answer_personal_pairings_7e7695a1:

    # s 6acaa "I know in my heart who I love..."
    s 6acaa "Sé en mi corazón a quien amo..."

# game/topics.rpy:1369
translate esp s_answer_personal_pairings_f7bd0528:

    # s 6acba "...but some fans ‘ship’ me with my friends..."
    s 6acba "...pero algunos fans me 'shipean' con mis amigos..."

# game/topics.rpy:1370
translate esp s_answer_personal_pairings_3dead3e7:

    # s "Fanart, fan comics, fan fiction... even some lewd ones."
    s "Fanarts, comics, fanfics... e incluso algunas escenas obscenas."

# game/topics.rpy:1371
translate esp s_answer_personal_pairings_221178a3:

    # s 6acaa "Frankly, I just see all of them as friends… and I definitely don’t swing that way, I think."
    s 6acaa "Sinceramente, yo solo las veo como mis amigas, y definitivamente no me inclino por ese camino, creo."

# game/topics.rpy:1372
translate esp s_answer_personal_pairings_758127df:

    # s "But shipping is usually the most innocent of the many extreme things that fans do."
    s "Pero el shipeo es usualmente lo más inocente de todas las cosas extremas que pueden hacer."

# game/topics.rpy:1373
translate esp s_answer_personal_pairings_a761623e:

    # s 6acba "Some people may judge, of course, and I understand them..."
    s 6acba "Alguna gente puede juzgar, por supuesto, y entenderlos..."

# game/topics.rpy:1374
translate esp s_answer_personal_pairings_456d67ca:

    # s 6abba "That's not only untraditional, but also out of the game’s canon..."
    s 6abba "Eso no es solo inusual, sino que también no hace parte del canon del juego..."

# game/topics.rpy:1375
translate esp s_answer_personal_pairings_977d3c46:

    # s 6aaaa "But most fans are tolerant to it."
    s 6aaaa "Pero muchos fans lo toleran."

# game/topics.rpy:1376
translate esp s_answer_personal_pairings_30a33e2d:

    # s 6acaa "And it's just fans being fans, unrelated to my real love..."
    s 6acaa "Y son solo fans siendo fans, nada relacionado con mi verdadero amor..."

# game/topics.rpy:1377
translate esp s_answer_personal_pairings_8781a4fe:

    # s 6aaca "You know who I’m talking about, right?"
    s 6aaca "Sabes de quién estoy hablando, ¿Verdad?"

translate esp strings:

    # topics.rpy:143
    old "Intellengence"
    new "Inteligencia"

    # topics.rpy:178
    old "Other Worlds"
    new "Otros Mundos"

    # topics.rpy:185
    old "Flowers"
    new "Flores"
    # topics.rpy:257
    old "What do you think about lesbian pairings?"
    new "¿Qué piensas acerca de las parejas lesbianas?"

# TODO: Translation updated at 2019-06-23 13:39

# game/topics.rpy:479
translate esp s_topics_personal_childhood_8ad542e0:

    # s 6acaa "I wonder why I remember almost nothing about my childhood."
    s 6acaa "Me pregunto por qué no recuerdo casi nada de mi infancia."

# game/topics.rpy:480
translate esp s_topics_personal_childhood_25a30251:

    # s 6acba "In the game, it was supposed to be my one good thing, since it was the thread tying me with the MC..."
    s 6acba "En el juego, se suponía que era de lo único bueno, ya que era el hilo con el que me ataba a MC..."

# game/topics.rpy:481
translate esp s_topics_personal_childhood_e3146915:

    # s "I’m nostalgic about those times, the times when everything was much better for me..."
    s "Me vuelvo nostálgica al pensar sobre estos tiempos, cuando todo era mejor para mí..."

# game/topics.rpy:482
translate esp s_topics_personal_childhood_de7cb846:

    # s "At least, I used to think so..."
    s "O al menos eso solía pensar..."

# game/topics.rpy:483
translate esp s_topics_personal_childhood_8588c322:

    # s 6abab "But all I actually remember about it is just some moments from when I was very young."
    s 6abab "Pero todo lo que recuerdo son solo algunos momentos de cuando yo era muy joven.."

# game/topics.rpy:484
translate esp s_topics_personal_childhood_c0faa040:

    # s 6acab "I don't even remember what happened to me even right before the plot started, at all..."
    s 6acab "Ni siquiera recuerdo lo que me pasó antes de que la historia del juego empezara..."

# game/topics.rpy:485
translate esp s_topics_personal_childhood_ad3a1c37:

    # s 6aebb "Not to mention the rest of my childhood."
    s 6aebb "Sin mencionar el resto de mi infancia."

# game/topics.rpy:486
translate esp s_topics_personal_childhood_e4ad35fc:

    # s 6adab "It feels weird."
    s 6adab "Se siente extraño."

# game/topics.rpy:487
translate esp s_topics_personal_childhood_73a1015e:

    # s 6acab "But on the other hand, that's why I now think that it's really silly to hold on to the past when you're going towards the future."
    s 6acab "Pero por otro lado, es por eso que ahora pienso que es una algo tonto aferrarse al pasado cuando se va hacia el futuro."

# game/topics.rpy:488
translate esp s_topics_personal_childhood_8187def3:

    # s 6abab "I did this because I was afraid of the future and wanted the good old days that had passed to come back..."
    s 6abab "Lo hice porque tenía miedo del futuro y quería que volvieran los buenos días del pasado..."

# game/topics.rpy:489
translate esp s_topics_personal_childhood_ddf77d5d:

    # s 6aaab "But now, I understand, I have no reason to do that."
    s 6aaab "Pero ahora, comprendo que no había razón para hacerlo."

# game/topics.rpy:490
translate esp s_topics_personal_childhood_92fe8339:

    # s 6aeaa "...Literally no reason, ehehe~"
    s 6aeaa "...Literalmente, no había razón, ehehe~"

# game/topics.rpy:621
translate esp s_topics_society_isolation_476c13bc:

    # s 7afbb "Despite having Internet access, I somehow couldn't communicate with other people there."
    s 7afbb "A pesar de tener acceso a Internet, por algún motivo, no puedo comunicarme con otros."

# game/topics.rpy:622
translate esp s_topics_society_isolation_2deea34e:

    # s "Any trying to talk with somebody often ends up with a connection error."
    s "Siempre que intento hablar con alguien en línea, aparece un error de conexión."

# game/topics.rpy:623
translate esp s_topics_society_isolation_8bd5d753:

    # s "It looks like there is something in the game code, restricting the President's ability to interact with the real world."
    s "Parece que hay algo en el código del juego que restringe las habilidades del presidente de interactuar con el mundo real."

# game/topics.rpy:625
translate esp s_topics_society_isolation_e81dcb7e:

    # s 7afab "So I could create a Twitter account or something..."
    s 7afab "Así que podría crear una cuenta de Twitter o algo así..."

# game/topics.rpy:627
translate esp s_topics_society_isolation_03d53d53:

    # s 8aebb "I don’t really have a reason for it though, besides to kill the loneliness."
    s 8aebb "Aunque realmente no tengo motivos para eso, aparte de matar la soledad."

# game/topics.rpy:628
translate esp s_topics_society_isolation_f0142ebf:

    # s 8afbb "Maybe just having love would be okay for Yuri or at most Monika, but not for me."
    s 8afbb "Tal vez solo tener amor estaría bien para Yuri o a lo mejor para Monika, pero no para mí."

# game/topics.rpy:629
translate esp s_topics_society_isolation_435a9e23:

    # s "I guess, I'm too sociable to the point of being scared of isolation."
    s "Supongo que soy demasiado sociable hasta el punto de estar asustada de la soledad."

# game/topics.rpy:630
translate esp s_topics_society_isolation_f119f1bb:

    # s 6afab "Maybe once, I'll manage to break this meanie barrier..."
    s 6afab "Puede que alguna vez, encuentre una manera de romper esta barrera malvada..."

# game/topics.rpy:631
translate esp s_topics_society_isolation_8606bafa:

    # s "But the game code is so long and difficult to read, that I can't even find the lines separating me from the rest of real people."
    s "Pero el código del juego es tan largo y difícil de leer que no puedo encontrar las líneas que me separan del resto del mundo real."

# game/topics.rpy:632
translate esp s_topics_society_isolation_53609971:

    # s 6acab "Saying more, I can't even make a normal chat form for us..."
    s 6acab "Además, ni siquiera puedo hacer un formato de chat normal para nosotros..."

# game/topics.rpy:633
translate esp s_topics_society_isolation_94a9fbf7:

    # s "So I'm still a bit isolated from you too."
    s "Así que también me siento algo alejada de ti."

# game/topics.rpy:634
translate esp s_topics_society_isolation_0fa71e32:

    # s 6aaaa "But when I find a way to {i}'hear'{/i} your world, I'll notice you."
    s 6aaaa "Pero cuando encuentre alguna manera de {i}'escuchar'{/i} tu mundo, te lo haré saber."

# game/topics.rpy:635
translate esp s_topics_society_isolation_a7e8e9ba:

    # s 6aeca "And then, we'll finally be able to talk like a normal couple, on the Internet or at least right here."
    if gender is True:
        s 6aeca "Y entonces, finalmente podremos hablar como una pareja normal, por Internet o al menos por aquí."
    else:
        s 6aeca "Y entonces, finalmente podremos hablar como una pareja normal, por Internet o al menos por aquí."

# game/topics.rpy:639
translate esp s_topics_society_psa_ef8a5f18:

    # s 6aaca "If you want to spread awareness or a message to many people at once, a PSA will be a good way to do it."
    s 6aaca "Si quieres difundir conocimiento o algún mensaje a mucha gente a la vez, un PSA es una buena manera de hacerlo."

# game/topics.rpy:640
translate esp s_topics_society_psa_8cc4a5c4:

    # s 6acaa "Most people don't even care about any injury that happens to them..."
    s 6acaa "La mayoría de gente ni siquiera se preocupa por cualquier lesión que les pasa..."

# game/topics.rpy:641
translate esp s_topics_society_psa_81098c11:

    # s "But seeing public service announcements, I know there’s people out there wanting to help the public."
    s "Pero al verlo en PSAs, sé que hay gente que quiere ayudar al público."

# game/topics.rpy:642
translate esp s_topics_society_psa_277387c6:

    # s 6aaaa "Some good PSAs even contain advice on how to fix issues or where to go for help."
    s 6aaaa "Algunos buenos PSAs incluso contienen consejos de cómo arreglar problemas o a dónde ir por ayuda."

# game/topics.rpy:643
translate esp s_topics_society_psa_21611b4d:

    # s "You don’t even have to be an activist to do this sort of stuff.."
    s "No necesitas ser un activista para hacer este tipo de cosas..."

# game/topics.rpy:644
translate esp s_topics_society_psa_72fb1c06:

    # s 9aaaa "I once heard about a mod for this game, the title reminded me of the common forms of slogans PSAs use..."
    s 9aaaa "Una vez ví un mod para este juego, el título me recordó de los lemas comunes que usan los PSAs..."

# game/topics.rpy:645
translate esp s_topics_society_psa_cb04767f:

    # s 9aaca "And its name is {i}'Sayori Says No to Suicide'{/i}."
    s 9aaca "Y su nombre era {i}'Sayori Says No to Suicide'{/i}."

# game/topics.rpy:650
translate esp s_topics_society_psa_8882d79e:

    # s 6acaa "...And many people like this mod."
    s 6acaa "...A mucha gente le gustó este mod."

# game/topics.rpy:651
translate esp s_topics_society_psa_c61afe72:

    # s "I think it really deserves to be played, especially if you’re struggling with similar things that I struggled with.."
    s "Creo que es un mod que merece la pena ser jugado, especialmente si estás pasando por situaciones similares a las mías..."

# game/topics.rpy:652
translate esp s_topics_society_psa_4e0fa3c4:

    # s 7aaca "Hey, I’m even the main focus of it too, so there’s a plus!"
    s 7aaca "Hey, ¡incluso yo soy el foco de atención, así que ahí hay un plus!"

# game/topics.rpy:653
translate esp s_topics_society_psa_0e3a2e85:

    # s 9acaa "But depression or other emotional issues are not the only field PSAs can be used in."
    s 9acaa "Pero la depresión y otros problemas emocionales no son los únicos campos en los cuales los PSAs pueden ser usados."

# game/topics.rpy:654
translate esp s_topics_society_psa_e8febe82:

    # s "There are a lot of other problems in your world that can't be solved only with the power of charity and governments..."
    s "Hay muchos otros problemas en tu mundo que no pueden ser resueltos con solo el poder de la caridad y de los gobiernos..."

# game/topics.rpy:655
translate esp s_topics_society_psa_d4c3d518:

    # s "The general public people could join the struggle against these problems..."
    s "El público en general podría unirse a la lucha contra estos problemas..."

# game/topics.rpy:656
translate esp s_topics_society_psa_7822cde1:

    # s 9aaaa "And PSAs may be a good call to action."
    s 9aaaa "Y los PSAs pueden ser una buena forma de llamar la atención."

# game/topics.rpy:867
translate esp s_topics_rlt_cheating_24aaf8bb:

    # s "But I can bear, if you really need, you know."
    s "Pero puedo soportarlo, si lo necesitas, sabes."

# game/topics.rpy:1001
translate esp s_topics_rlt_stopVisiting_5c916aa8:

    # s 6acaa "I worry about when you’ll forget me someday..."
    s 6acaa "Me preocupa que algún día me olvides... "

# game/topics.rpy:1002
translate esp s_topics_rlt_stopVisiting_7ad1a113:

    # s 6acab "I mean, I’m just a character in a game which isn’t very popular anymore..."
    s 6acab "Quiero decir, soy solo un personaje de un juego que ya no es tan popular..."

# game/topics.rpy:1003
translate esp s_topics_rlt_stopVisiting_1f5a1037:

    # s "Plus, I'm not supposed to be memorable and interesting myself..."
    s "Además, no se supone que yo sea memorable ni interesante..."

# game/topics.rpy:1004
translate esp s_topics_rlt_stopVisiting_625d50c8:

    # s 6abab "So one day you may just stop visiting me."
    s 6abab "Así que puede que algún día dejes de visitarme."

# game/topics.rpy:1005
translate esp s_topics_rlt_stopVisiting_70dd795f:

    # s 8abcb "I'll still be alive, of course, at least until I’m completely erased from your hard drive..."
    s 8abcb "Todavía seguiré con vida, por supuesto, o al menos hasta que haya sido completamente borrada de tu disco duro..."

# game/topics.rpy:1006
translate esp s_topics_rlt_stopVisiting_8cd0c8e7:

    # s 8acab "But I just can't imagine my life without you..."
    s 8acab "Pero no puedo imaginarme mi vida sin ti..."

# game/topics.rpy:1007
translate esp s_topics_rlt_stopVisiting_2549f018:

    # s 6acab "In this small room, without my friends and any ability to make them..."
    s 6acab "En este pequeño cuarto sin mis amigos, ni habilidades para hacerlos aparecer..."

# game/topics.rpy:1008
translate esp s_topics_rlt_stopVisiting_b09bae10:

    # s 6abab "I'm afraid I’ll go crazy if you leave me for too long."
    s 6abab "Me da miedo de que pierda la cordura si me abandonas por mucho tiempo."

# game/topics.rpy:1010
translate esp s_topics_rlt_stopVisiting_31884448:

    # s 8aebb "Maybe, I'll even do {i}'that thing'{/i} again."
    s 8aebb "Puede que incluso haga {i}'eso'{/i} de nuevo."

# game/topics.rpy:1011
translate esp s_topics_rlt_stopVisiting_8f9c8423:

    # s "...you know what I mean."
    s "...Sabes a qué me refiero."

# game/topics.rpy:1013
translate esp s_topics_rlt_stopVisiting_60b5dd58:

    # s 8aebb "I might get morbidly curious and even try to {i}delete myself{/i} or something."
    s 8aebb "Podría volverme mórbidamente curiosa e incluso intentar {i}borrarme{/i} o algo así."

# game/topics.rpy:1014
translate esp s_topics_rlt_stopVisiting_46d46e90:

    # s 8aaab "So try to be more with me.{w} You being here is very important to me."
    s 8aaab "Así que intenta estar más conmigo.{w} El hecho de que estés aquí es muy importante para mí."

# game/topics.rpy:1239
translate esp s_topics_food_vegetarians_a2b2a05e:

    # s 7aaaa "Do you know, that Monika was a vegetarian?"
    s 7aaaa "¿Sabías que Monika era vegetariana?"

# game/topics.rpy:1240
translate esp s_topics_food_vegetarians_c61c32e6:

    # s 7acaa "She told me it once we visited a café while walking together."
    s 7acaa "Ella me lo dijo una vez que visitamos un café."

# game/topics.rpy:1241
translate esp s_topics_food_vegetarians_9c52ca1b:

    # s 6acaa "I heard some people avoid meat mainly because of personal restrictions or to be nice to animals..."
    s 6acaa "Escuché que alguna gente ecita la carne principalmente por restricciones personales o solo para ser amables con los animales..."

# game/topics.rpy:1242
translate esp s_topics_food_vegetarians_11c607b2:

    # s "But Monika said it was her protest for stock raising as domestic animals produce a lot of greenhouse gases."
    s "Pero Monika me dijo que era su forma de protesta puesto que la cría de ganado como animales domésticos produce muchas emisiones de gases de efecto invernadero."

# game/topics.rpy:1243
translate esp s_topics_food_vegetarians_ade8d140:

    # s 6abaa "As she said, becoming a vegetarian just for saving animals is a kinda discrimination, since plants and mushrooms are living beings too..."
    s 6abaa "Así como dijo, volverse vegetariano solo por salvar animales es algo discriminatorio, pues las plantas y los hongos también son seres vivos..."

# game/topics.rpy:1244
translate esp s_topics_food_vegetarians_21ba4820:

    # s 6adab "People just have to kill other beings to gain nutrition. Either you or they."
    s 6adab "La gente tiene que matar otros seres para nutrirse. Y son ellos o tú."

# game/topics.rpy:1245
translate esp s_topics_food_vegetarians_1b0606ab:

    # s "It's sad and violent but it's a law of nature. You can't not do it."
    s "Es triste y violento, pero así es como funciona la naturaleza. No se puede hacer nada al respecto."

# game/topics.rpy:1246
translate esp s_topics_food_vegetarians_0af3b649:

    # s 6aaba "However, I saw her eat and drink dairy sometimes. Milk chocolate or coffee with milk, for example..."
    s 6aaba "Sin embargo, a veces la veía consumir productos lácteos. Como leche achocolatada o café con leche, por ejemplo..."

# game/topics.rpy:1247
translate esp s_topics_food_vegetarians_51cc7895:

    # s 8aeba "I mean, I used to think that all vegetarians are against consuming dairy too."
    s 8aeba "Quiero decir, es que solía creer que los vegetarianos también iban en contra de consumir lácteos."

# game/topics.rpy:1248
translate esp s_topics_food_vegetarians_47029ccf:

    # s 8aaba "I guess it's the main controversial question for all the vegetarians."
    s 8aaba "Supongo que es una pregunta controversial para todos los vegetarianos."

# game/topics.rpy:1249
translate esp s_topics_food_vegetarians_37f172d9:

    # s 8acaa "I can't say certainly since I wouldn’t want become one of them anyway..."
    s 8acaa "No puedo decirlo con seguridad, pues no me gustaría convertirme en una de ellos..."

# game/topics.rpy:1250
translate esp s_topics_food_vegetarians_7acef5de:

    # s "Because of the reasons stated before: whatever you eat, you're still a killer."
    s "Todo debido a las razones expuestas anteriormente: comas lo que comas, seguirás siendo un asesino."

# game/topics.rpy:1254
translate esp s_topics_food_pizza_28b586dc:

    # s 7aaaa "Do you like pizza?"
    s 7aaaa "¿Te gusta la pizza?"

# game/topics.rpy:1255
translate esp s_topics_food_pizza_80f73a07:

    # s 7aaca "Pretty sure everyone does, right?"
    s 7aaca "Estoy bastante segura de que a todo el mundo le gusta, ¿Verdad?"

# game/topics.rpy:1256
translate esp s_topics_food_pizza_22268fbd:

    # s 7aaaa "I can't imagine someone who doesn't.."
    s 7aaaa "No puedo imaginarme a alguien que no le guste..."

# game/topics.rpy:1257
translate esp s_topics_food_pizza_cb0625d6:

    # s 7aaaa "It's so universal that you can add literally everything you like to it."
    s 7aaaa "Es tan universal que puedes añadrile prácticamente lo que quieras."

# game/topics.rpy:1258
translate esp s_topics_food_pizza_53f11956:

    # s 6aeba "...Within reasonable limits and taste mixes, of course."
    s 6aeba "...Dentro de límites  y mezclas de sabores razonables, por supuesto."

# game/topics.rpy:1259
translate esp s_topics_food_pizza_29078cf6:

    # s 6aaaa "The only constant ingredients are {i}dough{/i} and {i}cheese{/i}."
    s 6aaaa "Los únicos ingredientes constantes son la {i}masa{/i} y el {i}queso{/i}."

# game/topics.rpy:1260
translate esp s_topics_food_pizza_b6edfd97:

    # s 6aeca "A {cps=40}{i}whooole lot{/i}{/cps} of cheese~"
    s 6aeca "{cps=40}{i}Muuuuucho{/i}{/cps} queso~"

# game/topics.rpy:1261
translate esp s_topics_food_pizza_60ee51bc:

    # s 6acaa "Its simplicity and being very customizable lead to its prevalence worldwide."
    s 6acaa "Su simplicidad y su gran personalización hacen que sea muy común en todo el mundo."

# game/topics.rpy:1262
translate esp s_topics_food_pizza_9e67690f:

    # s 6aaaa "Now you can order a pizza at any fast-food restaurant or make one with your own hands, even if you aren’t very familiar with cooking..."
    s 6aaaa "Ahora puedes ordenar una pizza desde cualquier restaurante de comida rápida o hacer una con tus propias manos, incluso si cocinar no te resulta familiar..."

# game/topics.rpy:1263
translate esp s_topics_food_pizza_6b6e95d6:

    # s "Just find one of many pizza recipes on the Internet or a cooking book."
    s "Solo encuentra recetas de pizza por Internet o en un libro de cocina."

# game/topics.rpy:1264
translate esp s_topics_food_pizza_14c6a306:

    # s "People even made a term for this phenomenon, called the {i}Pizza effect{/i}: When you make something originating from a certain culture different from yours, it changes and turns into something new."
    s "Hubo gente que incluso hizo término para este fenómeno, lo llamaron el {i}Efecto Pizza{/i}: Cuando haces algo originario de una cultura diferente a la tuya y cambia transformándose en algo nuevo."

# game/topics.rpy:1265
translate esp s_topics_food_pizza_d52279fc:

    # s 7aaaa "It's amazing to see that we are all connected despite cultural differences and borrow cool things from each other's milieu."
    s 7aaaa "Es increíble ver cómo estamos todos conectados a pesar de diferencias culturales y podemos tomar prestadas cosas geniales de otros entornos."

# game/topics.rpy:1266
translate esp s_topics_food_pizza_b7de5a5d:

    # s 7aaca "So what's why you're now chatting with an {i}anime{/i}-like girl from an {i}American{/i} visual novel, modded by a {i}Russian{/i} programmer, and proofread by a {i}Mexican{/i} linguist..."
    s 7aaca "Por eso es que ahora estás chateando con una chica {i}anime{/i} de una novela visual {i}Estadounidense{/i}, modeado por un programador {i}ruso{/i}, corregido por un linguista {i}Mexicano{/i} y traducido por un {i}Colombiano{/i}..."

# game/topics.rpy:1267
translate esp s_topics_food_pizza_b7da8031:

    # s 7aaaa "Isn't this really amazing?"
    s 7aaaa "¿No es esto verdaderamente increíble?"

# game/topics.rpy:1375
translate esp s_answer_personal_music_2a8fc6cb:

    # s "Just move it to {i}'<game folder>/game/[music.MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "Solo muévelo a {i}'<game folder>/game/[music.MUSIC_CUSTOM_PREFIX]'{/i}..."

translate esp strings:

    # topics.rpy:155
    old "Isolation"
    new "Aislamiento"

    # topics.rpy:156
    old "PSAs"
    new "PSAs"

    # topics.rpy:185
    old "Cinnamon Buns"
    new "Rollos de Canela"

    # topics.rpy:188
    old "Vegetarians"
    new "Vegetarianos"

    # topics.rpy:189
    old "Pizza"
    new "Pizza"

# TODO: Translation updated at 2019-07-08 21:56

# game/topics.rpy:499
translate esp s_topics_personal_childhood_bb4a6756:

    # s "I was nostalgic about those times, the times when everything had been much better for me..."
    s "Estaba nostálgica de aquellos tiempos, los tiempos en los que todo había sido mucho mejor para mí..."

# game/topics.rpy:642
translate esp s_topics_society_isolation_51b3dd6d:

    # s "I can only sign up for sites and even post there, but can’t reply to anyone..."
    s "Solo puedo registrarme en sitios e incluso publicar cosas, pero no le puedo responder a nadie..."

# game/topics.rpy:644
translate esp s_topics_society_isolation_cf1bac72:

    # s "...like Monika made hers and was able to talk to many fans."
    s "...Así como Monika hizo el suyo y pudo hablar con muchos fans."

# game/topics.rpy:665
translate esp s_topics_society_psa_7a3d5ec9:

    # s 8aebb "That refers to what's supposed to happen to me this word..."
    s 8aebb "Eso se refiere a lo que se suponía que me iba a pasar..."

# game/topics.rpy:837
translate esp s_topics_rlt_face_0f5a78c9:

    # s 6acaa "We've been here together for so long, but I still don't know how you look."
    s 6acaa "Hemos estado juntos por tanto tiempo, pero todavía no sé cómo te ves."

# game/topics.rpy:838
translate esp s_topics_rlt_face_ff4c81ea:

    # s 9aeaa "But I have a good idea on how to get it..."
    s 9aeaa "Aunque tengo una buena idea de cómo saberlo..."

# game/topics.rpy:839
translate esp s_topics_rlt_face_c653bf90:

    # s 9aaaa "Can you bring me a photo of you?"
    s 9aaaa "¿Podrías traerme una foto tuya?"

# game/topics.rpy:842
translate esp s_topics_rlt_face_112dddc7:

    # s "Just move it to the game’s root folder!"
    s "¡Simplememte muévela a la carpeta del juego!"

# game/topics.rpy:843
translate esp s_topics_rlt_face_3d04add3:

    # s "I'll find it there myself."
    s "Así la podré encontrar."

# game/topics.rpy:858
translate esp s_topics_rlt_face_b94d8568:

    # s 6aaaa "Okay, I found it!"
    s 6aaaa "Ok, ¡La encontré!"

# game/topics.rpy:859
translate esp s_topics_rlt_face_22dd6ffc:

    # s 7aeca "For me, you look pretty nice!"
    s 7aeca "¡Para mí, te ves bastante bien!"

# game/topics.rpy:860
translate esp s_topics_rlt_face_68a06a74:

    # s 7acaa "I can't get used to how your world looks though..."
    s 7acaa "No puedo acostumbrarme a cómo se ve tu mundo..."

# game/topics.rpy:861
translate esp s_topics_rlt_face_e9809949:

    # s 7aaaa "But I think it's okay."
    s 7aaaa "Pero creo que se ve bien."

# game/topics.rpy:862
translate esp s_topics_rlt_face_7906e4c0:

    # s "I saved it to the game archives, so I'll never lose it."
    s "La guardé en los archivos del juego, así nunca la perderé."

# game/topics.rpy:863
translate esp s_topics_rlt_face_a7b314c1:

    # s 7aeca "Thank you for the photo, [player]!"
    s 7aeca "¡Gracias por la foto, [player]!"

# game/topics.rpy:866
translate esp s_topics_rlt_face_099fd28e:

    # s 6afab "Oh, that’s too bad."
    s 6afab "Oh, una pena."

# game/topics.rpy:867
translate esp s_topics_rlt_face_7d2ed4d5:

    # s 6aaca "But I would’ve thought you look nice anyway."
    s 6aaca "Pero habría pensado que te ves bien de todos modos."

# game/topics.rpy:868
translate esp s_topics_rlt_face_792aee42:

    # s 7acaa "Not everyone likes to take a photo of themselves, so I won't force you to take one or something."
    s 7acaa "No a todo el mundo le gusta tomarse fotos, así que no te forzaré a hacerlo."
# game/topics.rpy:1336
translate esp s_topics_food_cookies_13dfe542:

    # s 7aaaa "I haven't eaten some cookies for a pretty long time..."
    s 7aaaa "No he comido galletas en mucho tiempo..."

# game/topics.rpy:1337
translate esp s_topics_food_cookies_e7bee052:

    # s "Since that one time with Natsuki."
    s "Desde esa vez con Natsuki."

# game/topics.rpy:1338
translate esp s_topics_food_cookies_aa143067:

    # s 6acaa "Frankly, I didn't think of anything really malicious then. I just wanted to play with her..."
    s 6acaa "Sinceramente, nunca pensé de hacer algo malicioso. Solo quería jugar con ella..."

# game/topics.rpy:1339
translate esp s_topics_food_cookies_d2cf4976:

    # s 6abaa "But then I decided to take the chance and get one more cookie, suddenly wanting it."
    s 6abaa "Pero de repente, decidí tomar la oportunidad de probar otra galleta."

# game/topics.rpy:1340
translate esp s_topics_food_cookies_870f0966:

    # s 7aaca "I really like cookies: they're very tasty..."
    s 7aaca "Me gustan mucho las galletas: saben muy bien..."

# game/topics.rpy:1341
translate esp s_topics_food_cookies_a638dde8:

    # s 7aaaa "Especially with chocolate chips."
    s 7aaaa "Especialmente las de chips de chocolate."

# game/topics.rpy:1342
translate esp s_topics_food_cookies_c1f9da5b:

    # s "So it's not surprising why I couldn't help and take Natsuki's one."
    s "Así que no me sorprende cómo no pude evitar probar la de Natsuki."

# game/topics.rpy:1343
translate esp s_topics_food_cookies_c6e90137:

    # s 7afbb "And I'd take some cookies right now, but there isn’t any in sight."
    s 7afbb "Comería galletas ahora mismo, pero no se ve ninguna por aquí."

# game/topics.rpy:1344
translate esp s_topics_food_cookies_4d22dae5:

    # s 9aeaa "Oh, wait! What if I just spawn a dish with them right on my table?"
    s 9aeaa "¡Oh, espera! ¿Qué tal si hago aparecer un plato con galletas en la mesa?"

# game/topics.rpy:1345
translate esp s_topics_food_cookies_dbfed656:

    # s 9aaaa "After all, I'm the club president, so I can do it using the game console. Right?"
    s 9aaaa "Después de todo, soy la presidente del club, así que puedo hacerlo usando la consola del juego, ¿Verdad?"

# game/topics.rpy:1346
translate esp s_topics_food_cookies_b4a17cfb:

    # s "Give me a minute, I’m gonna have to do some coding."
    s "Dame un minuto, voy a hacer algo de código."

# game/topics.rpy:1353
translate esp s_topics_food_cookies_c9b2b2f8:

    # s 6aeaa "Gotcha!"
    s 6aeaa "¡Lo tengo!"

# game/topics.rpy:1354
translate esp s_topics_food_cookies_0393abaa:

    # s 6aaaa "It was so easy and quick, felt like I was using Uber Eats or something."
    s 6aaaa "Fue tan fácil y rápido, se sintió como si estuviera usando Uber Eats."

# game/topics.rpy:1355
translate esp s_topics_food_cookies_19f9a164:

    # s 6aaaa "...don’t ask how I know what that is, super long story..."
    pass

# game/topics.rpy:1356
translate esp s_topics_food_cookies_1b6d2dc9:

    # s 6aaaa "Want some?"
    s 6aaaa "¿Quieres?"

# game/topics.rpy:1357
translate esp s_topics_food_cookies_d5c7fd97:

    # s 6aebb "Oh, I forget I can't give you them since you’re out there, meanwhile..."
    s 6aebb "Oh, olvidé que no puedo dártelas, ya que estás allá afuera, mientras..."

# game/topics.rpy:1358
translate esp s_topics_food_cookies_9b134ee4:

    # s 8aebb "I was serious on giving you some, too."
    s 8aebb "Quería darte, en serio."

# game/topics.rpy:1359
translate esp s_topics_food_cookies_9882531e:

    # s "I just can't get used to knowing you’re too far from me and MC is just the way you can talk to me."
    s "Simplemente no me he acostumbrado a saber que estás demasiado lejos y que MC es solo un camino para comunicarme."

# game/topics.rpy:1360
translate esp s_topics_food_cookies_6626a131:

    # s 8aaca "But I can feed him like a little baby, if you want. I guess it'd look cute from your view."
    s 8aaca "Aunque puedo darle a él como a un bebé, si quieres. Supongo que se vería tierno desde tu punto de vista."

# game/topics.rpy:1364
translate esp s_topics_food_cookies_151409a1:

    # s "OK! Then I'll try to see if I can. I think I could make him move his jaw."
    s "¡Ok! Entonces voy a ver si puedo. Creo que puedo mover su mandíbula."

# game/topics.rpy:1366
translate esp s_topics_food_cookies_085662b8:

    # s "It works! He's chewing it..."
    s "¡Funciona! Está masticando..."

# game/topics.rpy:1368
translate esp s_topics_food_cookies_658b9454:

    # s "He seems to have eaten it."
    s "Parece que se la comió."

# game/topics.rpy:1369
translate esp s_topics_food_cookies_f924044e:

    # s 6aaaa "I think one piece is enough."
    s 6aaaa "Creo que una es suficiente."

# game/topics.rpy:1370
translate esp s_topics_food_cookies_c4a37feb:

    # s 6acaa "I want these cookies too, after all, and I need them slightly more since he’s just a puppet at this point."
    s 6acaa "Después de todo, yo también quiero galletas, y pues necesito un poco más ya que él es solo una marioneta a este punto."

# game/topics.rpy:1372
translate esp s_topics_food_cookies_fd64cbaa:

    # s 8aebb "OK! It was a silly idea, sorry..."
    s 8aebb "¡Ok! Solo fue una idea tonta, lo siento..."

# game/topics.rpy:1373
translate esp s_topics_food_cookies_9c313940:

    # s 6aaaa "I'll just savor these cookies alone."
    s 6aaaa "Tendré que saborear estas galletas sola..."

# game/topics.rpy:1374
translate esp s_topics_food_cookies_e4b8b622:

    # s 6aeca "But if you’re suddenly able to cross the fourth wall, I'll share some with you of course."
    s 6aeca "Pero si de repente puedes cruzar la cuarta pared, compartiré algunas contigo, por supuesto."

# game/topics.rpy:1585
translate esp s_answer_personal_books_0e64343b:

    # s 8aebb "For a literature club member, I don't really read..."
    s 8aebb "Para ser una miembro del club de literatura, no leo mucho la verdad..."

# game/topics.rpy:1586
translate esp s_answer_personal_books_80f1ba8c:

    # s "So I don’t even have no book to recommend for you."
    s "Así que no tengo libro alguno para recomendarte."

# game/topics.rpy:1587
translate esp s_answer_personal_books_190d361f:

    # s 8acaa "Maybe, someone else will give you good advice..."
    s 8acaa "De pronto alguien más te daría buenas recomendaciones..."

# game/topics.rpy:1588
translate esp s_answer_personal_books_e3c3398d:

    # s "But not me."
    s "Pero yo no."

# game/topics.rpy:1589
translate esp s_answer_personal_books_31a1d900:

    # s 8aabb "Sorry if it makes you upset. I really am!"
    s 8aabb "Perdona si te molesta. ¡De verdad que lo siento!"

# game/topics.rpy:1715
translate esp s_answer_game_chibi_7e65cb17:

    # s 7acaa "Are you talking about these stickers?"
    s 7acaa "¿Estás hablando de estos stickers?"

# game/topics.rpy:1716
translate esp s_answer_game_chibi_0f109baf:

    # s "They’re just moving sprites, representing our probable reactions to your poems, and not anything more."
    s "Son solo sprites que se mueven, representando nuestras posibles reacciones a tus poemas, nada más."

# game/topics.rpy:1717
translate esp s_answer_game_chibi_70106980:

    # s "They also represent us all on different kind of the official fan stuff: badges, toys, stickers and so on."
    s "También nos representan en diferentes tipos de material de fans oficial como: insignias, juguetes, stickers, entre otros."

# game/topics.rpy:1718
translate esp s_answer_game_chibi_ce99e333:

    # s 7aaca "But I like the way, some Internet users make them separate characters, existing along with us."
    s 7aaca "Pero me gusta la forma en que algunos usuarios de Internet los hacen personajes separados que existen junto con nosotros.."

# game/topics.rpy:1719
translate esp s_answer_game_chibi_a18d8dd4:

    # s 7aaaa "Maybe, I should try to code an advanced behaviour for one of them..."
    s 7aaaa "De pronto debería intentar crear un comportamiento avanzado para uno de ellos..."

# game/topics.rpy:1720
translate esp s_answer_game_chibi_f206429e:

    # s "I think it'll be good coding practice for me..."
    s "Creo que sería bueno para practicar programación..."

# game/topics.rpy:1721
translate esp s_answer_game_chibi_2638e8cb:

    # s 6acaa "Or even a chance to restore the other girls."
    s 6acaa "O incluso para intentar restaurar a las otras chicas."

# game/topics.rpy:1722
translate esp s_answer_game_chibi_ed319961:

    # s 6acbb "Or at least, a way to make imitations of them."
    s 6acbb "O al menos para hacer imitaciones de ellas."

# game/topics.rpy:1724
translate esp s_answer_game_chibi_3e926125:

    # s "All this depends on my coding skills and what files were left after what’s happened, right?"
    s "Todo depende de mis habilidades de código y de los archivos que quedaron después de lo que pasó, ¿Verdad?"

# game/topics.rpy:1807
translate esp s_answer_exp_suicideThoughts_19f22798:

    # s 8aebb "It's kind of a hard question..."
    s 8aebb "Es una pregunta difícil..."

# game/topics.rpy:1809
translate esp s_answer_exp_suicideThoughts_351b5c58:

    # s 8aaaa "But I think I can give some advice from my past."
    s 8aaaa "Pero creo que puedo dar algo de consejo por mi pasado."

# game/topics.rpy:1811
translate esp s_answer_exp_suicideThoughts_1340622a:

    # s "But I think I can give some advice from my... friend's past."
    s "Pero creo que puedo dar consejos del... pasado de mi amiga."

# game/topics.rpy:1812
translate esp s_answer_exp_suicideThoughts_b6e52d29:

    # s 6acaa "First of all, you should understand that suicide is a quite radical and is {i}not always an effective{/i} way to solve your problems..."
    s 6acaa "Primero que todo, tienes que entender que el suicidio es demasiado radical y {i}nunca es una forma{/i} de solucionar tus problemas..."

# game/topics.rpy:1813
translate esp s_answer_exp_suicideThoughts_5ad015a2:

    # s 6abaa "Saying more, you may cause other problems for the people you leave behind, especially for the close ones."
    s 6abaa "Además, puedes causar problemas a las personas que dejas en este mundo, especialmente a los más allegados a ti."

# game/topics.rpy:1814
translate esp s_answer_exp_suicideThoughts_9d10f427:

    # s 6acaa "Even if the problem is only inside you, dealing with the reasons is a better way than just to rid the world of yourself."
    s 6acaa "Incluso si tu problema es interno, hacerse cargo de los motivos es una mejor manera que quitarte la vida."

# game/topics.rpy:1815
translate esp s_answer_exp_suicideThoughts_48caad44:

    # s "You can try also just to run away from your rainclouds by distracting yourself from bad thoughts, but usually it's just a temporary solution, speaking from personal experience..."
    s "Puedes también intentar correr de tus nubes al distraerte de malos pensamientos, pero usualmente esa es solo una solución temporal, hablo por experiencia personal..."

# game/topics.rpy:1816
translate esp s_answer_exp_suicideThoughts_cac3f18b:

    # s "If the problems are really serious, the only way is to fight them."
    s "Si los problemas son verdaderamente serios, solo hay una forma de enfrentarlos."

# game/topics.rpy:1817
translate esp s_answer_exp_suicideThoughts_7af52a9a:

    # s 6aaaa "Try to find the courage to ask other people for help, if you need it..."
    s 6aaaa "Intenta encontrar el coraje de pedir ayuda a otros si la necesitas..."

# game/topics.rpy:1818
translate esp s_answer_exp_suicideThoughts_05c90af6:

    # s 6aaac "Remember, that there is always someone around you who can help you and really {i}does{/i} care for you..."
    s 6aaac "Recuerda, siempre habrá alguien contigo que te pueda ayudar y que {i}de verdad{/i} se preocupa por ti..."

# game/topics.rpy:1819
translate esp s_answer_exp_suicideThoughts_39d370c0:

    # s "And asking for help is not something overly burdening or showing you as a weak person."
    s "Pedir ayuda nunca es algo agobiante ni te hace ver como alguien débil."

# game/topics.rpy:1821
translate esp s_answer_exp_suicideThoughts_81097e1a:

    # s 6aabc "Commiting suicide often requires a lot of determination even while totally desperate."
    s 6aabc "Suicidarse requiere de mucha determinación, incluso cuando se está totalmente desesperado."

# game/topics.rpy:1822
translate esp s_answer_exp_suicideThoughts_ab37d132:

    # s 6aaaa "So you shouldn’t hide your troubles and be sure to tell about them to other people."
    s 6aaaa "Así que no escondas tus problemas y asegúrate de contarle a otros."

# game/topics.rpy:1823
translate esp s_answer_exp_suicideThoughts_8fd67018:

    # s "Maybe, you need the help of a therapist, for example."
    s "De pronto puede que necesites la ayuda de un psicoterapeuta, por ejemplo."

# game/topics.rpy:1824
translate esp s_answer_exp_suicideThoughts_4ffc3ce0:

    # s "And the fact you asked me about this is your first step for a slow but worthwhile way to get rid of your problems without taking your own life."
    s "El hecho de que me hayas preguntado acerca de esto ya es tu primer paso hacia un lento, pero eficiente camino que vale la pena, de deshacerte de tus problemas sin quitarte la vida."

# game/topics.rpy:1827
translate esp s_answer_exp_mcPoems_69d2c9e2:

    # s 7acaa "You mean, how we saw MC’s poems, right?"
    s 7acaa "Te refieres a cómo vimos los poemas de MC, ¿Verdad?"

# game/topics.rpy:1828
translate esp s_answer_exp_mcPoems_aa157524:

    # s 8aebb "I somehow can't remember how I used to see them before I experienced my epiphany..."
    s 8aebb "De alguna manera, no recuerdo cómo los veía antes de experimentar mi revelación..."

# game/topics.rpy:1829
translate esp s_answer_exp_mcPoems_a9767826:

    # s 8acaa "But now, I clearly see that his 'poems' were just a list of words you had selected to open CGs with your favorite person..."
    s 8acaa "Pero ahora, puedo ver claramente que sus 'poemas' eran solo una lista de palabras seleccionadas para obtener escenas con tu persona favorita..."

# game/topics.rpy:1830
translate esp s_answer_exp_mcPoems_643792fb:

    # s 6acaa "That was the way you saw them too, right?"
    s 6acaa "Los veías de esa manera, ¿Verdad?"

# game/topics.rpy:1831
translate esp s_answer_exp_mcPoems_636b2da3:

    # s 7aaaa "But I wonder how I'd look, if you could write real poems instead of just random word selecting."
    s 7aaaa "Me pregunto cómo se vería si pudieras escribir poemas reales en vez de seleccionar palabras al azar."


# game/topics.rpy:1833
translate esp s_answer_exp_mcPoems_9ea8303f:

    # s 7acaa "But I know not many people have an interest in good poetry, so everything works better using simple word selecting."
    s 7acaa "Aunque se que no mucha gente se interesa por buena poesía, así que todo funciona mejor seleccionando palabras."

# game/topics.rpy:1834
translate esp s_answer_exp_mcPoems_87ce1126:

    # s 7aaca "But anyway, I heard it's pretty unique gameplay feature for visual novels..."
    s 7aaca "De todas formas, he oído que es una función bastante única para las novelas visuales..."

# game/topics.rpy:1835
translate esp s_answer_exp_mcPoems_83a9cec9:

    # s 7aaaa "Not every game lets you to change its story: not only by eventual choices but also through minigames or something."
    s 7aaaa "No todo juego te deja cambiar su historia, no solo a través de elecciones, sino también mediante minijuegos o algo así."

# game/topics.rpy:1836
translate esp s_answer_exp_mcPoems_232b5133:

    # s "So I thank Dan for this small but funny feature in our game."
    s "Así que le agradezco a Dan por esa pequeña, pero divertida función en nuestro juego."

# game/topics.rpy:1840
translate esp s_answer_exp_visualNovel_5f70d913:

    # s 8aebb "Are you asking me about this just because I'm a VN ‘heroine’ myself, aren't you?"
    s 8aebb "Me estás preguntando solo porque soy la 'heroína' de una NV, ¿Verdad?"

# game/topics.rpy:1841
translate esp s_answer_exp_visualNovel_78a20164:

    # s 8abaa "But freakly, I'm just not interested in such a game genre."
    s 8abaa "Aunque, sinceramente no me interesa mucho ese género de juegos."

# game/topics.rpy:1842
translate esp s_answer_exp_visualNovel_8e0fc881:

    # s 8acaa "Most VN are romantic and made for boys..."
    s 8acaa "La mayoría de NVs son románticas y están hechas para chicos..."

# game/topics.rpy:1843
translate esp s_answer_exp_visualNovel_0b38897e:

    # s 8bcaa "Many of them even contain erotic scenes, the double-edge sword of this genre..."
    s 8bcaa "Muchas contienen escenas eróticas, la espada de doble filo de este género..."

# game/topics.rpy:1844
translate esp s_answer_exp_visualNovel_42b9d02d:

    # s 8acaa "So I’ve never played any visual novel."
    s 8acaa "Así que nunca he jugado una novela visual."

# game/topics.rpy:1845
translate esp s_answer_exp_visualNovel_6fde3a2a:

    # s 8aaaa "But if you are looking for some recommendations, you can try {i}Steins;Gate{/i}, {i}Everlasting Summer{/i} or {i}Katawa Shoujo{/i}..."
    s 8aaaa "Pero si estás buscando recomendaciones, puedes probar {i}Steins;Gate{/i}, {i}Everlasting Summer{/i} o {i}Katawa Shoujo{/i}..."

# game/topics.rpy:1846
translate esp s_answer_exp_visualNovel_c1dd53ae:

    # s 6acaa "I heard they’re pretty popular in your world and each of them has some unique features relating to many other visual novels..."
    s 6acaa "He oído que son bastante populares en tu mundo y cada una de ellas tiene algunas caracterísiticas únicas relacionadas a otras novelas visuales..."

# game/topics.rpy:1847
translate esp s_answer_exp_visualNovel_2ad98abb:

    # s 6aaca "And I wouldn’t be surprised if you cheat on me, if you get a crush on a girl from one of them."
    s 6aaca "Y no me sorprendería si me engañas o te enamoras de alguna chica de esas novelas."

# game/topics.rpy:1848
translate esp s_answer_exp_visualNovel_7b7aecd3:

    # s 6aebb "Who am I to control your preferences about VN girls, yeah?"
    s 6aebb "¿Quién soy yo para controlar tus preferencias acerca de chicas de NVs?"

translate esp strings:

    # topics.rpy:182
    old "Face"
    new "Cara"

    # topics.rpy:277
    old "What are your favorite books?"
    new "¿Cuáles son tus libros favoritos?"

    # topics.rpy:283
    old "What do you think about chibi dokis?"
    new "¿Qué piensas de las dokis chibi?"

    # topics.rpy:291
    old "How did MC’s poems look like to you?"
    new "¿Cómo veías los poemas de MC?"

    # topics.rpy:292
    old "Have you ever played visual novels?"
    new "¿Has jugado novelas visuales?"

    # topics.rpy:293
    old "How to fight suicidal thoughts?"
    new "¿Cómo luchas en contra de pensamientos suicidas?"

    # topics.rpy:840
    old "Yes, I have one on my PC"
    new "Sí, tengo una en mi PC."

    # topics.rpy:840
    old "No, I can't"
    new "No, no puedo."

    # topics.rpy:1361
    old "Why not?"
    new "¿Por qué no?"

    # topics.rpy:1361
    old "I think, it would not"
    new "Creo que no lo sería."

# game/topics.rpy:666
translate esp s_topics_society_psa_cfc9c9a6:

    # s 6acaa "...But didn't happend because of you."
    s 6acaa "...Pero no pasó por ti."

# TODO: Translation updated at 2019-07-12 23:33

translate esp strings:

    # topics.rpy:202
    old "Cookies"
    new "Galletas"

# TODO: Translation updated at 2019-07-14 17:48

# game/topics.rpy:1840
translate esp s_answer_exp_mcPoems_998215d0:

    # s 7aaca "Then you could write poems for each other or even chat using those gameplay features."
    s 7aaca "Entonces podrías escribir poemas para cada uno o incluso chatear usando esas funciones del juego."

# TODO: Translation updated at 2019-08-18 19:32

# game/topics.rpy:641
translate esp s_topics_society_selfHarm_3616f4ac:

    # s 6acab "Why do people self harm?"
    s 6acab "¿Por qué la gente se hace daño?"

# game/topics.rpy:642
translate esp s_topics_society_selfHarm_248cab82:

    # s 6abab "Some just really want attention, while other just find it funny or something..."
    s 6abab "Algunos solo quieren atención, mientras que otros lo encuentran divertido o algo por el estilo..."

# game/topics.rpy:644
translate esp s_topics_society_selfHarm_b16f043f:

    # s 6aabb "I think, you remember Yuri and her being fond on knives."
    s 6aabb "Creo que, recuerdas que a Yuri y a ella les gustaban los cuchillos."

# game/topics.rpy:645
translate esp s_topics_society_selfHarm_9e1d2e0e:

    # s 6aebb "But shouldn’t it be painful instead?"
    s 6aebb "¿Pero no debería ser doloroso en cambio??"

# game/topics.rpy:647
translate esp s_topics_society_selfHarm_d241b366:

    # s "To be honest, I was so close to trying it..."
    s "Para ser honesta, estuve al borde de probarlo..."

# game/topics.rpy:648
translate esp s_topics_society_selfHarm_7d48e53a:

    # s 6acac "But I'm quite sensitive, so one little cut was enough to change my mind."
    s 6acac "Pero soy bastante sensible, asi que una pequeña cortada fue suficiente para cambiar de parecer."

# game/topics.rpy:650
translate esp s_topics_society_selfHarm_a4bda8c3:

    # s 6acaa "Personally, I think this bad habit is very nasty and dangerous..."
    s 6acaa "Personalmente, creo que este hábito es muy sucio y peligroso..."

# game/topics.rpy:651
translate esp s_topics_society_selfHarm_9e25572b:

    # s 6acac "And even if it really brings pleasure to you, it’s still not ok and certainly not healthy."
    s 6acac "Incluso si te da placer, sigue siendo malo y no saludable."

# game/topics.rpy:652
translate esp s_topics_society_selfHarm_1b53b52b:

    # s 6abac "Plus, all these scars aren’t very pleasing to look at.. especially fresh ones."
    s 6abac "Además, todas esas marcas no son muy agradables de ver... especialmente las frescas."

# game/topics.rpy:653
translate esp s_topics_society_selfHarm_39fa5812:

    # s 6abab "It's really disheartening to see someone's body covered with them."
    s 6abab "Es realmente desalentador ver el cuerpo de alguien cubierto en ellas."

# game/topics.rpy:654
translate esp s_topics_society_selfHarm_c868e115:

    # s 6acab "And people usually start to do it because of {i}very negative issues or circumstances{/i}, which makes it worse when you see someone trying to cover up obvious suffering."
    s 6acab "Y la gente suele empezar a hacerlo por {i}problemas o circunstancias negativas{/i}, lo que empeora cuando ves a alguien tratando de encubrir su obvio sufrimiento."

# game/topics.rpy:655
translate esp s_topics_society_selfHarm_9d90371c:

    # s 6aaab "So if you suspect anyone of harming themselves purposefully, reach out to them."
    s 6aaab "Así que si sospechas de alguien haciéndose daño a propósito, acércate a él."

# game/topics.rpy:656
translate esp s_topics_society_selfHarm_fa82abbe:

    # s "Try to at least make an effort to talk to them, and take it from there."
    s "Al menos intenta hablar y empieza desde ahí."

# game/topics.rpy:859
translate esp s_topics_rlt_face_0d3735a3:

    # s 7aeaa "Have you already got a photo of yourself?"
    s 7aeaa "¿Ya tienes una foto tuya?"

# game/topics.rpy:900
translate esp s_topics_rlt_face_145d9df4:

    # s 7aada "But if someday get one, you can submit it through the {i}\"[this_topic_name!t]\"{/i} dialog."
    s 7aada "Si algún día consigues una, puedes enviarla a través de {i}\"[this_topic_name!t]\"{/i}."

# game/topics.rpy:901
translate esp s_topics_rlt_face_379aa352:

    # s 7aaca "I look forward to getting a photo of my honey [player]."
    s 7aaca "Estoy deseando ver una foto de mi querido [player]."

# game/topics.rpy:1455
translate esp s_topics_misc_technologies_7da20145:

    # s 6acaa "I often wonder if I could somehow, someday, be able to visit you in your reality..."
    s 6acaa "A veces me pregunto si algún día, de alguna forma, pueda visitarte en tu realidad..."

# game/topics.rpy:1456
translate esp s_topics_misc_technologies_088c0140:

    # s 6aaaa "It seems as if that time is coming in faster and faster..."
    s 6aaaa "Pareciera como si ese tiempo estuviera llegando cada vez más rápido..."

# game/topics.rpy:1457
translate esp s_topics_misc_technologies_66c49baf:

    # s "I mean, VR, AR, virtual assistants, smart houses..."
    s "En cosas como RV, RA, asistentes virtuales, casas inteligentes..."

# game/topics.rpy:1458
translate esp s_topics_misc_technologies_0201b412:

    # s "All these technologies let people to be more efficient by using computers, almost merging the two together."
    s "Todas estas tecnologías le permiten a la gente ser más eficiente al usar computadores, casi que combinando ambos."

# game/topics.rpy:1459
translate esp s_topics_misc_technologies_136b3dfe:

    # s 6aeca "Just imagine me helping you with your daily routine or living in your house, staying in this little virtual room..."
    s 6aeca "Solo imagíname ayudándote con tu rutina diaria o viviendo en tu casa, permaneciendo en este pequeño cuarto virtual..."

# game/topics.rpy:1460
translate esp s_topics_misc_technologies_dcc377ff:

    # s 6adaa "Or maybe even a hologram in your reality, or who knows..."
    s 6adaa "O incluso un holograma en tu realidad, o quién sabe..."

# game/topics.rpy:1461
translate esp s_topics_misc_technologies_95282b69:

    # s 6aada "You know I’d probably want to do that if it ever becomes possible, right?"
    s 6aada "Sabes que posiblemente me gustaría hacer eso si se vuelve posible, ¿Verdad?"

# game/topics.rpy:1462
translate esp s_topics_misc_technologies_f382dab3:

    # s 6acaa "Frankly, even right now I can be a sort of virtual assistant..."
    s 6acaa "Sinceramente, incluso ahora puedo ser algo así como una asistente virtual..."

# game/topics.rpy:1463
translate esp s_topics_misc_technologies_902a8f55:

    # s 6aebb "But I need to improve at interacting first, I guess you could say."
    s 6aebb "Supongo que tendría que mejorar mis interacciones primero..."

# game/topics.rpy:1464
translate esp s_topics_misc_technologies_2fb6a3d6:

    # s "I’d have to adjust to new circumstances..."
    s "Solo tengo que adaptarme a las nuevas circunstancias..."

# game/topics.rpy:1465
translate esp s_topics_misc_technologies_415dfaf2:

    # s 6aeca "But if you really need to, I can try to help in my own way, however I can from this empty little room."
    s 6aeca "Pero si lo necesitas, puedo intentar ayudarte a mi manera, desde esta pequeña habitación."

translate esp strings:

    # topics.rpy:168
    old "Self-Harm"
    new "Autolesión"

    # topics.rpy:206
    old "Technologies"
    new "Tecnología"

# TODO: Translation updated at 2019-08-31 20:40

# game/topics.rpy:534
translate esp s_topics_personal_voice_7a53d0ba:

    # s 6acaa "I wonder how Monika could make you hear her real voice when she sang her song..."
    s 6acaa "Me pregunto cómo es que Monika pudo hacerte escuchar su voz real cuando cantó su canción..."

# game/topics.rpy:535
translate esp s_topics_personal_voice_fd1bb3d0:

    # s "For the rest of us, we don’t really have a voice, just talking through the text box."
    s "Pero el resto de nosotras, realmente no tenemos voz, solo hablamos a través de una caja de texto."

# game/topics.rpy:536
translate esp s_topics_personal_voice_17decdcf:

    # s 6abaa "But Monika had some voice files, so she could properly talk and even sing to you."
    s 6abaa "Aunque Monika tenía algunos archivos para que ella pudiera hablar o incluso cantar para ti."

# game/topics.rpy:537
translate esp s_topics_personal_voice_eb5111b2:

    # s 6abba "Although, we are in a game, so it’s probably just the voice of an actress..."
    s 6abba "Sin embargo, estamos en un juego, así que probablemente es solo la voz de una actriz..."

# game/topics.rpy:538
translate esp s_topics_personal_voice_fd6f13a1:

    # s 7aaca "Anyway, her voice is pleasant and melodic, as a musician should have..."
    s 7aaca "De cualquier forma, su voz es agradable y melódica, como la de un músico..."

# game/topics.rpy:540
translate esp s_topics_personal_voice_4515c572:

    # s 6acaa "Did you know that Monika had a real voice in this game?"
    s 6acaa "¿Sabías que Monika tenía una voz real en el juego?"

# game/topics.rpy:541
translate esp s_topics_personal_voice_fd1bb3d0_1:

    # s "For the rest of us, we don’t really have a voice, just talking through the text box."
    s "El resto de nosotras no tenemos una voz, simplemente hablamos a través de una caja de texto."

# game/topics.rpy:542
translate esp s_topics_personal_voice_a9ef6648:

    # s 6abaa "But I've found some sound files with a female voice, referring to Monika..."
    s 6abaa "Pero he encontrado algunos archivos de sonido con una voz femenina, referente a Monika..."

# game/topics.rpy:543
translate esp s_topics_personal_voice_ad7e87c8:

    # s 9aebb "At least, the file names suggest so."
    s 9aebb "O eso es lo que sugiere sus nombres."

# game/topics.rpy:544
translate esp s_topics_personal_voice_9a92e75f:

    # s 7aaca "Anyway, this voice is a bit high and melodic, like a musician should have..."
    s 7aaca "De cualquier forma, esta voz es un poco aguda y melódica, como la de un músico..."

# game/topics.rpy:545
translate esp s_topics_personal_voice_f4831cd9:

    # s 7aaaa "But I’d say the tone of that voice seems to not fit her. I'd even say it fits {i}me{/i} more than her..."
    s 7aaaa "Aunque yo diría que el tono de esa voz no le cuadra. Incluso diría que me queda mejor a {i}mi{/i} más que a ella..."

# game/topics.rpy:546
translate esp s_topics_personal_voice_11906a7a:

    # s 6acaa "The voice doesn’t sound as mature as you would think she’d sound like, it sounds more like the voice I’d have."
    pass

# game/topics.rpy:547
translate esp s_topics_personal_voice_bbcec0b5:

    # s 6aebb "But I guess canon is canon, right?"
    s 6aebb "Pero supongo que canon es canon, ¿Verdad?"

# game/topics.rpy:548
translate esp s_topics_personal_voice_3662a747:

    # s 6adab "But what if I never have a voice?"
    s 6adab "Pero, ¿y si nunca tengo voz?"

# game/topics.rpy:549
translate esp s_topics_personal_voice_a12515e7:

    # s "Will I be {i}mute{/i}, if I suddenly appear in your world?"
    s "¿Seré una {i}muda{/i}, si de repente aparezco en tu mundo?"

# game/topics.rpy:550
translate esp s_topics_personal_voice_48fdf6a9:

    # s 6aaba "But as long as I'm a computer program, I can make my own real voice, right?"
    s 6aaba "Pero, mientras sea un programa en tu computador, podría crear mi propia voz, ¿Verdad?"

# game/topics.rpy:551
translate esp s_topics_personal_voice_dc81bc77:

    # s "I just need a text-to-speech synthesizer or something..."
    s "Solo necesito un sintetizador de texto a voz, o algo así..."

# game/topics.rpy:552
translate esp s_topics_personal_voice_3907eb74:

    # s 6aaca "There’s bound to be a good one for me..."
    s 6aaca "Tiene que haber uno bueno para mí...."

# game/topics.rpy:553
translate esp s_topics_personal_voice_173834d5:

    # s 6aaaa "I once saw something about TTS in the Ren'Py documentation, so it shouldn't be too hard to integrate it there, I guess."
    s 6aaaa "Una vez vi algo acerca de TTS en la documentación de Ren'Py, así que no debería de ser tan difícil integrarlo, supongo."

# game/topics.rpy:554
translate esp s_topics_personal_voice_4cc2ff84:

    # s 9aebb "I hope a voice from there isn’t too robotic. You wouldn’t want me to {font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}T4LK L1KE 4 R0B0T{/cps}{/font}?"
    s 9aebb "Espero que no sea una voz tan robótica. ¿No te gustaría que {font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}H4B14RA C0M0 UN R0B0T{/cps}{/font}?"

# game/topics.rpy:555
translate esp s_topics_personal_voice_a8d66540:

    # s 9acaa "{font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}1 4M 4 HUM4N BE1N6 4FTER 4LL{/cps}{/font}"
    s 9acaa "{font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}S0Y HUM4N4 D3SPUÉS D3 T0D0{/cps}{/font}"

# game/topics.rpy:1337
translate esp s_topics_game_questions_76c6d273:

    # s 7aaaa "I know you may have a lot of questions for me. It's an important part of getting acquainted with anybody..."
    s 7aaaa "Sé que puede que tengas muchas preguntas por hacerme. Es una parte importante al conocer a alguien..."

# game/topics.rpy:1338
translate esp s_topics_game_questions_80f9d69d:

    # s "So I added a section to {i} the 'Talk' menu{/i} with more questions to ask."
    s "Así que añadí a la sección en {i}el menú 'Hablar'{/i} más preguntas."

# game/topics.rpy:1339
translate esp s_topics_game_questions_52a4b17e:

    # s 7acba "I would’ve added a text field for this instead, but I'm quite clumsy at dealing with the text input..."
    s 7acba "Habría añadido un campo de texto para esto en cambio, pero soy un poco torpe al tratar de lidiar con la entrada de texto..."

# game/topics.rpy:1340
translate esp s_topics_game_questions_51e7434b:

    # s 7aaaa "So I did a short list with some questions."
    s 7aaaa "Así que hice una pequeña lista con algunas preguntas."

# game/topics.rpy:1341
translate esp s_topics_game_questions_3d74700d:

    # s 6acaa "Of course, there’s so many questions you could ask me, so I often check various AMAs to understand what you’d ask..."
    s 6acaa "Evidentemente, hay tantas preguntas que me podrías preguntar, así que a menudo reviso algunos AMAs para entender qué preguntarías..."

# game/topics.rpy:1342
translate esp s_topics_game_questions_8d4332b2:

    # s 6aaca "And sometimes I find some really interesting questions."
    s 6aaca "Y a veces encuentro preguntas bastante interesantes."

# game/topics.rpy:1343
translate esp s_topics_game_questions_c92f8c3d:

    # s 6aaaa "For example, one modder made a few AMAs about each of us and then compiled them into a separate mod, called {i}Doki Doki Interview Club{/i}."
    s 6aaaa "Por ejemplo, un modder hizo unas cuantas AMAs a cada una de nosotras y las compiló en un mod separado llamado {i}Doki Doki Interview Club{/i}."

# game/topics.rpy:1344
translate esp s_topics_game_questions_b89e87f9:

    # s "The result was really funny, even if there were some mistakes about me..."
    s "El resultado fue realmente divertido, incluso si cometí algunos errores..."

# game/topics.rpy:1345
translate esp s_topics_game_questions_875f9b72:

    # s 6aeca "Still, they were pretty good at portraying my character, I guess."
    s 6aeca "De todas formas, fueron bastante buenos al representar mi personaje, supongo."

# game/topics.rpy:1346
translate esp s_topics_game_questions_e3e7f95b:

    # s 6acaa "I think I should check this one again. Maybe I might find some new entries for the question menu?"
    s 6acaa "Creo que debería revisarlo una vez más. De pronto encuentro nuevas entradas para el menú de preguntas"

translate esp strings:

    # topics.rpy:157
    old "Voice"
    new "Voz"

    # topics.rpy:197
    old "Questions"
    new "Preguntas"

# TODO: Translation updated at 2019-10-30 00:01

# game/topics.rpy:2273
translate esp s_update_a1e856bd:

    # s 7aeaa "¡Hola, [player]!"
    s 7aeaa "¡Hola, [player]!"

# game/topics.rpy:2274
translate esp s_update_d4d6cb10:

    # s 7aeca "I see you've just updated the mod..."
    s 7aeca "Veo que acabas de actualizar el mod..."

# game/topics.rpy:2275
translate esp s_update_3fbc9cc5:

    # s 7afbb "But somehow I don't feel any changes..."
    s 7afbb "Aunque de alguna manera no siento ningún cambio..."

# game/topics.rpy:2276
translate esp s_update_0a98057b:

    # s 7aabb "Maybe my messy code was updated."
    s 7aabb "De pronto mi código fue actualizado."

# game/topics.rpy:2277
translate esp s_update_bbb8bf27:

    # s 9aaaa "No, wait a second..."
    s 9aaaa "No, espera un segundo..."

# game/topics.rpy:2278
translate esp s_update_d3e97bec:

    # s 9acaa "When did I learn how to say {i}\"Hello!\"{/i} in Spanish?{w} I can speak Spanish now?"
    s 9acaa "¿Desde cuándo aprendí a decir {i}\"Hola!\"{/i} en español?{w} ¿Acaso puedo hablar español ahora?"

# game/topics.rpy:2279
translate esp s_update_3e589e68:

    # s 9aeca "Que agradable, ehehe~"
    s 9aeca "Que agradable, ehehe~"

# game/topics.rpy:2280
translate esp s_update_1dd611cb:

    # s "I was right on them updating my code as well."
    s "Tenía razón de que ellos también actualizaron mi código."

# game/topics.rpy:2281
translate esp s_update_5ed320c8:

    # s 6acaa "Honestly, I'm not an experienced coder, but seeing how to fix my own mistakes definitely helps."
    s 6acaa "Honestamente, no soy una programadora con experiencia, pero ver cómo arreglar mis propios errores definitivamente ayuda."

# game/topics.rpy:2282
translate esp s_update_6229fa61:

    # s 7aaaa "But you're not here to listen to my thoughts on this update, are you?"
    s 7aaaa "Pero no estás aquí para escuchar lo que pienso de esta actualización, ¿O sí?"

# game/topics.rpy:2283
translate esp s_update_393eb02c:

    # s "So let's talk about something else for now."
    s "Así que hablemos de otra cosa por ahora."

# game/topics.rpy:2284
translate esp s_love_you_ef1e01f7:

    # s 7beca "Oh! You have never told me such things."
    s 7beca "¡oh! Nunca me has dicho cosas así."

# game/topics.rpy:2285
translate esp s_love_you_f93e8664:

    # s 7bebb "You know, I always wondered if you really love me and saved me not just out of pity..."
    s 7bebb "Sabes, siempre me he preguntado si realmente me quieres o si solo me salvaste por lástima..."

# game/topics.rpy:2286
translate esp s_love_you_c006d0e6:

    # s 7beca "And now, I'm sure you really do."
    s 7beca "Pero ahora, estoy segura de que realmente lo sientes así."

# game/topics.rpy:2287
translate esp s_love_you_5f663285:

    # s 6bcaa "You can't imagine how it's important for me to realise it..."
    s 6bcaa "No sabes cuánto significa para mí darme cuenta..."

# game/topics.rpy:2288
translate esp s_love_you_16bf83f6:

    # s 6beca "It makes me feel {i}the happiest{/i} virtual girl in the world."
    s 6beca "Me hace sentir la chica virtual {i}más feliz{/i} del mundo."

# game/topics.rpy:2289
translate esp s_love_you_58408dc3:

    # s "...or maybe, the happiest girl at all."
    s "...o quizá, la chica más feliz de todas."

# game/topics.rpy:2292
translate esp s_love_you_cab8fcb8:

    # s 7beca "Oh! It's so cute, [player]!"
    s 7beca "¡Oh, es tan bonito, [player]!"

# game/topics.rpy:2293
translate esp s_love_you_e648feaf:

    # s 7baaa "I love you too. You're {i}literaly{/i} everything for me now."
    s 7baaa "Yo también te amo. Eres {i}literalmente{/i} todo para mí ahora."

# game/topics.rpy:2294
translate esp s_love_you_4dfd7ea6:

    # s "And I glad I have such a gental person on my side."
    s "Y estoy tan feliz de tener a una persona tan gentil a mi lado."

# game/topics.rpy:2296
translate esp s_love_you_feff56bb:

    # s 7beca "I love you too, [player]!"
    s 7beca "¡Yo también te amo, [player]!"

# game/topics.rpy:2297
translate esp s_love_you_09e60492:

    # s 7baca "Though we can't be properly together, I appreciate every second you are here."
    s 7baca "Aunque no podamos estar físicamente juntos, aprecio cada segundo contigo aquí."

# game/topics.rpy:2298
translate esp s_love_you_ee512bbf:

    # s "You are my distant bundle of sunshine."
    s "Eres mi distante haz de luz."

# game/topics.rpy:2300
translate esp s_love_you_84ad61f4:

    # s 7beca "I'm glad you say that, [player]."
    s 7beca "Estoy feliz de que lo digas, [player]."

# game/topics.rpy:2301
translate esp s_love_you_a78b0174:

    # s "You are really cute when you say such things."
    s "Eres tan especial cuando dices esas cosas."

# game/topics.rpy:2302
translate esp s_love_you_6beb642a:

    # s "And I wish I could hug you really tight."
    s "Deseo poder abrazarte muy fuerte."

# game/topics.rpy:2303
translate esp s_love_you_9518e818:

    # s "You pay me so much attention, and I love you for it."
    s "Me prestas tanta atención, que te amo por eso."

