#Images
image wakalive = "images/logowakalive.png"
image titre ="images/titre.png"
image bg endoftheworld = "images/endoftheworld.png"
image bg route = "images/route.png"
image bg classe = "images/classe.png"
image bg cour = "images/cour.png"
image magical = "images/magical.png"
image mecha = "images/mecha.png"
image troll ="images/troll.png"
image prof = "images/prof.png"

#Personnages
define JP = Character('[player_name]', color="#e2c756")
define Magical = Character('Manaka', color="#f2bdc7")
define Mecha = Character('Motoko', color="#7698b3")
define Troll = Character('Troll péon', color="#8e4759")
define Prof = Character('Monsieur Marcel', color="#554866")

#Splashscreen
label splashscreen:
    scene white
    with Pause(0.5)
    
    show wakalive with dissolve
    with Pause(2)
    
    scene white with dissolve
    with Pause(0.5)
    
    play sound renpy.random.choice(["sounds/titrefr.ogg", "sounds/titreen.ogg", "sounds/titrejp.ogg"])
    return

#Script
label start:

    #Variables
    $ magical_love = "False"
    $ mecha_love = "False"
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    stop sound
    play music "sounds/intro.ogg"
    scene bg endoftheworld with dissolve
    
    "En 2255, la Terre est menacée par l'armée du Roi des Trolls.{p}Le nouvel allié de l'humanité dans cette épreuve est des plus surprenants...{p}Personne n'aurait cru qu'après avoir détruit nos villes, mangé nos soldats et atomisé nos vies, ils se dresseraient maintenant face à nos ennemis...{p}Pour nous protéger..."
    
    "...{p}Les kaiju.{p}{cps=0}{i}(Sans \"s\" parce que les mots japonais sont invariables, tudieu.){/i}{/cps}"
    
    "Ces monstres géants, terreurs de la nature sorties du fond des temps pour venir nous rappeler nos erreurs à coup de pattes dans les grands rues...{p}Ils sont maintenant nos camarades. Godzilla, Gamera et même Mothra font partie des nôtres.{p}Plus destructeurs que des tsunamis, leur fureur se déchaînera sur nos ennemis...{p}Mais seulement après l'heure du thé et des gâteaux."
    
    stop music fadeout 1.0
    play sound "sounds/jingle.ogg"
    scene bg route with wipeleft
    
    "Moi, je ne suis qu'un simple lycéen. Aujourd'hui, comme tous les jours, je vais en cours en faisant attention de ne pas me prendre les pieds dans les débris d'immeubles et les carcasses putréfiées."
    
    play sound "sounds/choc.ogg"
    "Aieee !" with sshake
    
    play sound "sounds/choc.ogg"
    "Abbah !" with sshake
    
    play music "sounds/baston.ogg"
    show troll with easeinleft
    
    Troll "Haha ! Je suis un vilain troll et je vais t'attaquer ! Accroche toi à ton amour propre parce que je vais te faire des remarques très désobligeantes dont tu te souviendras même aux cabinets !"
    
    "!!!{p}Mon popotin est déjà tout endolori de la chute surprise provoquée par ce malotru, comment vais-je me sortir ce ce traquenard ?!"
    
    Troll "C'est le plan de notre Roi Tsundere ! En attaquant ta virilité et ton estime de soi, je vais te transformer en cliché de mauvais soujo manga ! Tu ne seras que doute et te vautreras dans les clichés éculés d'une romance aliénante et avilissante !"
    
    show troll at left with ease
    show magical at right with easeinright
    
    Magical "Halte là, gredin ! Par le pouvoir de la tarte tropézienne, je ne te laisserai pas salir la dignité de ce monde !"
    
    "150 mètres de magie et de dentelles se dressent désormais entre moi et mon agresseur."
    
    Troll "Damnation ! Une magical kaiju girl ! Mais ce n'est qu'un contre-temps ! Je vais me débarasser d'elle d'un revers de remarque irrévérencieuse !"
    
    Magical "Nenni, vilain ! Car je suis {b}Manaka du Corbeau{/b} ! ★~❤"

    Troll "Enfer ! C'est la plus puissante des magical kaiju girls ! Que vais-je pouvoir faire mis à part trembler des genoux en {cps=21}chargeaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANT !{/cps}"
    
    hide troll with easeoutright
    play sound "sounds/sprotch.ogg"
    "SPROTCH" with sshake
    
    "Le troll ne court qu'à sa perte lorsqu'il attaque le plat du pied de Manaka la magical kaiju girl. Il ne reste alors de l'immonde personnage qu'un petit tas de paillettes."
    
    stop music fadeout 1.0
    play music "sounds/magical.ogg" fadein 1.0
    show magical at center with ease
    
    "Manaka se tourne alors vers moi."
    
    Magical "Ouf, tu es sain et sauf. Comment vas-tu ?"
    
    "Face à tant de grâce et de gentillesse, je ne sais répondre.{p}Cette magnifique créature m'a sauvé des griffes métaphoriques de l'immonde monstre."
    
    Magical "Oh, mon pauvre, tu as l'air bien secoué. Peux-tu au moins me dire quel est ton nom ?"
    
    $ player_name = renpy.input("(Mince, je ne me rappelle pas mon prénom ! Ma chute m'a rendu amnésique !){p}{cps=0}{i}(Entrez votre sobriquet juste en dessous.){/i}{/cps}", default="Jean-Pierre")
    $ player_name = player_name.strip()
    $ player_name = "Jean-Pierre"
    
    JP "J... Je m'appelle {b}[player_name]{/b}."
    
    Magical "Enchantée de faire ta connaissance... Oh, mais j'ai oublié de me présenter !"
    
    "Un pas à gauche, trois pas à droite, une pirouette et des étincelles..."
    
    Magical "Je suis {b}Manaka du Corbeau{/b} ! ~★ Je suis une magical kaiju girl et je veux sauver tous les humains des méchants trolls ! ❤"
        
    JP "Heu... Heureux de faire ta connaissance..."
    
    "Elle est beaucoup trop classe. Je ne peux contenir mon embrassement : je rougis et piétine nerveusement."
    
    Magical "Mais ! Cet uniforme ! Tu vas au lycée Jean Kirito toi aussi ?"
    
    JP "Oui. Ah, mais c'est toi qui est en Terminale L 4 !"
    
    "Le {b}lycée Jean Kirito{/b} est un établissement mixte où se rendent autant les humains que les kaiju.{p}Il s'agit d'un symbole de notre unité par l'éducation commune et le partage de valeurs saines comme l'histoire, les mathématiques et la bagarre de rue."
    
    Magical "Kyah~★ ! Suis-je donc si peu discrète ? Mais quelle joie de croiser un camarade sur le chemin de l'école !"
    
    Magical "Cependant, ce chemin n'est pas très sûr... Veux-tu que je t'accompagne jusqu'au lycée ? Tout seul, tu pourrais croiser d'autres manants..."
    
menu:
    Magical "Veux-tu que je t'accompagne jusqu'au lycée ?"
    "Assurément !":
        jump yep
    "N... Non, je peux très bien me débrouiller tout seul.":
        jump nope
        
label yep:
    Magical "Super !{p}Oh, il est déjà si tard ! Vite, hâtons nous pour ne pas être en retard en cours !"
    
    $ magical_love = "True"
    
    stop music fadeout 1.0
    
    jump highschool

label nope:
    
    Magical "Oh... D'accord... Bien... À plus tard peut-être..."
    
    stop music fadeout 1.0
    hide magical with easeoutleft
    
    JP "(Damnation ! Cette réponse que j'ai donné ! C'est une réplique digne d'une tsundere ! Ce maudit troll aurait-il réussit à me décontenancer ?)"
    
    "Je marche seul jusqu'au lycée, en me rongeant sang et ongles."

    jump highschool
    
label highschool:
    
    play music "sounds/mecha.ogg" fadein 1.0
    play sound "sounds/jingle.ogg"
    scene bg classe with wipeleft
    
    "Ce matin, nous avons cours de technologie avec Monsieur Marcel."
    
    
    "La classe" "BROUHAHA. BROUHAHA."
    
    show prof with easeinright
    
    Prof "Au travail, bande de moules ! Pour le TP d'aujourd'hui, on va plancher sur une arme pour se défendre contre les trolls.{p}Rappelez-vous, le second amendement existe uniquement pour {b}votre{/b} sécurité !"
    
    hide prof with easeoutleft
    
    "Nous nous mettons au travail derechef. Je fais équipe avec Jean-Claude, Jean-Paul et Jeanne-Michelle...{p}Mais dois rapidement travailler seul lorsqu'une mauvaise manipulation de la pile nucléaire irradie mes trois camarades."
    
    show prof with easeinleft
    
    Prof "Mais c'est du beau boulot ça dis donc [player_name] !"
    
    JP "Merci m'sieur. Je n'en suis pas peu fier ! Un mech kaiju, ça c'est un beau TP !"
    
    Prof "Eh bien il va être temps de l'allumer, ce maudit bestiau."
    
    "Je m'exécute et pèse sur le piton."
    
    play sound "sounds/choc.ogg"
    "Rise and shine!" with sshake
    
    Prof "Non pas le plafond enfin !{p}AH NON PAS LA TÊTE !" with sshake
    
    play sound "sounds/choc.ogg"
    hide prof with easeoutbottom
    show mecha with easeinbottom
    
    "Le mecha kaiju se dresse de toute sa hauteur, défonçant le toit de la salle de TP (pourtant prévue pour accueillir humains et kaiju) au passage. Quel désastre !"
    
    Mecha "Mais quelle camelote ce truc, c'est fait en carton ou quoi ?"
    
    "Le mecha a parlé.{p}Ou plutôt, il a attaqué en réponse à l'agression du bâtiment trop petit.{p}Pour combattre des monstres - les trolls - nous créons des monstres.{p}Ce mecha kaiju est équipé des mêmes armes que nos ennemis : un canon à insultes photoniques, une batterie de missiles à susceptibilité chercheuse et même un rayon rageur.{p}Face à une telle machine de terreur, les trolls adverses n'ont aucune chance."
    
    Mecha "Oh, c'est vous, Maître."
    
    "Le mecha kaiju m'a remarqué. Il sait déjà que c'est moi qui l'ai construit car j'ai effacé de sa mémoire les profils de mes autres camarades qui m'ont lâchement abandonné en cours de TP pour cause de bubons atomiques... Pff... Bande de nazes."
    
    Mecha "Maître, qui suis-je ?"
    
    JP "(Est-il en train de se poser des questions existentielles dès maintenant ou bien... Oh !){p}C'est ton nom que tu demandes, est-ce bien ça ?"
    
    Mecha "Oui, Maître."
    
    JP "C'est...{p}Écrit juste au dessus de ta boîte de dialogue. Tu devrais le savoir pourtant, c'est toi qui a brisé le quatrième mur, {b}Motoko{/b} !"
    
    Mecha "Mes excuses, Maître. Voyez-vous, moi, je n'essaie pas de compenser la mort de mes parents en essayant de devenir un playboy millionnaire, aussi génial qu'il est talentueux."
    
    "J'ai un mouvement de recul instinctif face à tant de vilénie. Le malotru a osé me viser de ses armes de troll anti-troll !" with sshake
    
    play sound "sounds/choc.ogg"
    JP "(Damned, le félon a touché juste avec son insulte ! Me voilà fort marri !)" with sshake
    
    JP "Ce... C'est... Même pas vrai ! D'abord !" with sshake
    
    Mecha "Oh mince, je crois que je vous ai blessé. Veuillez m'excuser, Maître."
    
    play sound "sounds/choc.ogg"
    "D'un revers de queue, Motoko balaie un bâtiment situé un peu plus loin.{p}C'est (c'était) l'hôpital des adultes, de tous ceux qui survivent à peine à la post-apocalypse parce qu'ils ne sont plus de fringuants lycéens." with sshake
    
    Mecha "Oh, l'hôpital des adultes est détruit ! Désormais, personne dans le lycée ne pourra être plus heureux que vous car tous vos camarades sont désormais orphelins...{p}M... Mais...{p}Que ce soit bien clair entre nous...{p}J... Je...{p}Je fais pas ça parce que je vous apprécie !"
    
menu:
    Mecha "J... Je n'ai pas fait ça pour vous, Maître..."
    "Quelle pudeur, c'est admirable !":
        jump ouais
    "Mais, tu te fous de moi !":
        jump nan
        
label ouais:
    $ mecha_love = "True"
    
    JP "Même si tu ne l'avoues pas, j'apprécie ton geste. Il faut beaucoup de courage pour tuer autant de gens {cps=24}- qui plus est des innocents et des malades -{/cps} tout ça rien que pour le bonheur d'une seule personne."
    
    "Les joues du mecha chauffent à blanc. C'est sûrement comme ça que les machines rougissent."
    
    Mecha "I... Idiot* !{p}{i}*N.D.T. : ça veut dire « Baka ».{/i}"
    
    stop music fadeout 1.0
    hide mecha with easeoutright
    
    JP "(Ce n'est même pas une insulte. A-t-il baissé les armes ? Je commence à l'apprécier...)"
    
    jump lunch

label nan:
    JP "Non seulement tu trolles, mais en plus tu n'es qu'une sale tsundere !" with sshake
    
    JP "Assume tes actions au lieu de te cacher derrière un stéréotype éculé !" with sshake
    
    JP "Tu ne vaux pas mieux que ces trolls contre lesquels tu es censé te battre !" with sshake
    
    play sound "sounds/choc.ogg"
    Mecha "I... Idiot* !{p}{i}*N.D.T. : ça veut dire « Baka ».{/i}" with sshake
    
    stop music fadeout 1.0
    hide mecha with easeoutright
    
    jump lunch

label lunch:
    
    play sound "sounds/jingle.ogg"
    scene bg cour with wipeleft

    "Après ce cours de techno qui n'a pas été de tout repos arrive enfin l'heure du déjeuner."
    
    JP "(Enfin un peu de tranquillité...)"
    
    play sound "sounds/choc.ogg"
    "BOUM BOUM PAN PAN WIZZZZZ BIP BADABANG" with sshake
    
    JP "Qu'est-ce que c'est que ce vacarme ?!"
    
    play music "sounds/baston.ogg"
    play sound "sounds/choc.ogg"
    "BADABANG PAM BOUM BOUM PATAPRO" with sshake
    
    "De l'autre côté de la cour du lycée se déroule un combat de titans. Deux kaiju se castagnent tandis qu'à leur pied, quelques élèves humains s'échangent des barres ChocoTipTop® en guise de paris."
    
    JP "Mais, je connais ces titans !"
    
    show magical at right with easeinleft
    
    show mecha at left with easeinright
    
    JP "Manaka ! Motoko ! Qu'est-ce que vous faites ?"
    
    "La magical kaiju girl rencontrée ce matin et le mecha kaiju construit la même demi-journée s'échangent des mandales sans courtoisie aucune !{p}Je m'égosille pour les interpeler mais peine à me faire entendre."
    
    Magical "Par le pouvoir de la tarte tropézienne ! Vil troll, je vais te punir !"
    
    Mecha "Mais enfin, il y a méprise ! Je ne suis pas un troll !"
    
    Magical "Ton vocabulaire est pourtant aussi disgracieux que celui de ces êtres répugnants ! Tu es des leurs, et subiras alors mon courroux !"
    
    Mecha "Je trolle mais pour le bien de tous ! Il s'agit d'une arme que je ne veux pas employer sur vous ! Mais vous m'obligez à riposter..."
    
    play sound "sounds/choc.ogg"
    JP "{b}CESSEZ !{/b}{p}Vous vous enguirlandez pour des prunes !" with sshake
    
    "Enfin les deux kaiju entendent la voix de la raison - la mienne - et tournent la tête en ma direction."
    
    Magical "[player_name] ?!"
    
    Mecha "Maître ?! Oh, maître, excusez-moi pour cet incident."
    
    Magical "Incident ?! Mais quelle façon de parler !{p}Ne l'écoute pas [player_name] ! Il essaie de t'embobiner ! Sous ses dehors de métal lustré, ce kaiju est un troll !"
    
    Mecha "Et sous ses atours de magical girl, elle est en fait une kaiju !" with sshake
    
    Magical "Voilà, qu'est-ce que je disais ? Ça recommence : il ne peut pas ouvrir son clapet sans caler de pique grossière !"
    
    Mecha "C'est du taillé sur mesure, avec les compliments de la maison. Voyez, je suis spécialisé dans le service de premier ordre très chère demoiselle."
    
    Magical "La plaisanterie a assez duré ! En garde !"
    
    "Les deux kaiju se font face, prêts à s'écharper, mais ma voix, alors fluette et tremblante, les sort de leur transe meurtrière."
    
    JP "Je refuse de vous voir vous chicaner de la sorte...{p}Parce que...{p}Je vous apprécie tous les deux."
    
    stop music fadeout 1.0
    
    Magical "Oh !"
    
    Mecha "Ah !"
    
    Mecha "Mais... Il y en a forcément un que vous...{cps=21}a... a-i-a-a-a-a-a-a-a...{/cps}"
    
    "Motoko tremble et rougit. Serait-il en train de bugger ?"
    
    Magical "Que tu... aimes plus que l'autre.{p}N'est-ce pas [player_name] ?"
    
    Mecha "O... Oui ! C'est bien ça ! Dites-nous, maître !"
    
menu:
    JP "Mon cœur est tiraillé... Qui vais-je choisir ?"
    "Manaka la magical kaiju girl est l'élue de mon cœur." if magical_love == "True":
        jump magicalend
    "Motoko le mecha kaiju est sans conteste mon préféré." if mecha_love == "True":
        jump mechaend
    "Je préfère partir plutôt que de voir ça plutôt que d'être aveugle.":
        jump badend
    
label magicalend:
    
    JP "Motoko... Je suis désolé mais Manaka m'a ouvert les yeux...{p}En vrai, les mechas, c'est trop nul et rien ne vaut le pouvoir magique de la tarte tropézienne."
    
    play sound "sounds/choc.ogg"
    Mecha "...{p}...{p}{b}B... {i}BAKA{/i} !{/b}" with sshake
    
    hide mecha with easeoutright
    
    "Je m'apprête à rattraper Motoko, le mecha que j'ai blessé en son for intérieur, mais Manaka pose sa patte sur mon épaule."
    
    play music "sounds/goodend.ogg"
    show magical at center with ease
    
    Magical "Laisse-donc. Tu as fait ce qu'il fallait. Tu as été honnête avec toi-même et avec lui."
    
    JP "Oui... Tu as raison."
    
    Magical "Quoiqu'il en soit... Je suis heureuse que tu aies fait ton choix car je... je t'a..."
    
    JP "Chut... Ne dis rien..."
    
    "Et, de la manière la plus romantique qui soit, je lui prends la main.{p}Notre avenir est désormais scellé d'amour, de magie, de génocide de trolls et de tarte tropézienne."
    
    jump generique

label mechaend:
    
    JP "Manaka... Je suis désolé mais... La technologie, c'est l'avenir. C'est pour ça que... Je préfère Motoko.{p}Les magical girl, c'est du passé. Tu dois ouvrir les yeux : on va toutes les remplacer par des mechas. Il faut te mettre à la page."
    
    play sound "sounds/choc.ogg"
    Magical "Mais... C'est horrible ce que tu dis ! Je te déteste !" with sshake
    
    hide magical with easeoutleft
    
    "Et la magical kaiju girl s'en fut."
    
    play music "sounds/goodend.ogg"
    show mecha at center with ease
    
    Mecha "Vous n'avez vraiment aucun tact, Maître. Mais... C'est... Ce qui fait... Votre charme..."
    
    JP "..."
    
    Mecha "Mais ! Ne vous méprenez pas ! Je ne dis pas ça parce que..."
    
    JP "Allons, tu peux tomber les masques, les boucliers et les lances. Tu sais bien que je vois clair dans ton jeu."
    
    "Motoko, sur la défensive, recule d'un pas et s'apprête à répliquer. Je ne lui en laisse pas le temps, découvrant un large sourire et éclatant d'un rire chaleureux et bon."
    
    JP "Si cela te gène, parlons plutôt de botter le popotin de l'apocalypse des monstres avec des monstres dans ton genre !"
    
    "Les yeux tout humides d'huile, Motoko me saute alors dessus et atterrit dans mes bras."
    
    Mecha "Baka !"
    
    jump generique
    
label badend:
    
    JP "C'est du chantage affectif de bas étage. Jamais je n'aurai cru aucun de vous deux capable d'une telle bassesse."
    
    JP "Hors de ma vue ! Sur le champ ! Et que je ne vous reprenne plus à vous chamailler de la sorte ! Vauriens !"
    
    hide magical mecha with dissolve
    
    play music "sounds/badend.ogg"
    JP "Ah mais...{p}Je suis tout seul en fait."
    
    JP "C'est nul."
    
    JP "Je m'ennuie déjà."
    
    JP "Ça serait chouette si je pouvais recommencer... Ou même réécrire toute l'histoire..."
    
    jump generique
    
label generique:
    
    stop music fadeout 1.0
    scene titre with dissolve

    "{cps=0}Ce jeu a été réalisé dans le cadre d'une initiative de {a=https://www.youtube.com/channel/UCxn60qFxv4Xzh6dlqlVTwYg}Wakanim Live{/a} pour montrer que tout le monde peut faire des jeux vidéo.{p}Qu'ils soit simples, stupides ou moches, c'est pas si dur de créer des trucs.{p}Alors prenez-vos dix doigts, ceux de vos copains et faisez des machins !{/cps}"
    
    "{cps=0}{i}Kawaii★Kaiju Love❤Love{/i} est un jeu de {a=https://twitter.com/hugo_gelis}Hugo Gelis{/a} disponible en {a=https://github.com/HugoGelis/Wakanim-Live-Game-Jam}open source{/a}.{p}Merci à Ben, Seiko Ralie, Joystickman et Marc-Antoine pour les bonnes idées lancées pendant le {a=https://www.youtube.com/watch?v=h9oPsSUe_ng}Wakanim Live #3{/a} !{p}Et surtout merci aux meilleurs {i}partners in crime{/i} : {a=https://twitter.com/RaphaelBuniet}Raphaël{/a} et Astrid !{/cps}"
    
    "{cps=0}{b}Crédits{/b}{p}Explosions : {a=http://www.navy.mil/view_image.asp?id=2227}l'armée américaine{/a}{p}Musique : {a=http://www.rickymakesmusic.com/}Ricky Rangel Jr.{/a}{p}Inspiration divine : l'épisode 4 d'Excel Saga{p}Jeu réalisé avec {a=http://www.renpy.org/}Ren'py{/a}, {a=https://notepad-plus-plus.org/}Notepad++{/a}, {a=http://www.gimp.org/}Gimp{/a}, {a=http://audacityteam.org/}Audacity{/a} et {a=https://github.com/}Github{/a}.{/cps}"
    
    "{cps=0}Merci d'avoir testé ce petit jeu, et à la prochaine !{p}#bagarre{p}★~FIN~★{/cps}"
    jump splashscreen