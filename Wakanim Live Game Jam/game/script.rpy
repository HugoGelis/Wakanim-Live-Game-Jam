# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image wakalive = "images/logowakalive.png"
image bg endoftheworld = "images/endoftheworld.png"
image bg route = "images/route.png"
image bg classe = "images/classe.png"
image bg cour = "images/cour.png"
image magical = "images/magical.png"
image troll ="images/troll.png"

# Déclarez les personnages utilisés dans le jeu.
define JP = Character('[player_name]', color="#17c9aa")
define Magical = Character('Manaka', color="#e81ae1")
define Mecha = Character('Motoko', color="#8c8181")
define Troll = Character('Troll péon', color="#57ac5f")

label splashscreen:
    scene white
    with Pause(0.5)
    
    show wakalive with dissolve
    with Pause(2)
    
    scene white with dissolve
    with Pause(0.5)
    return

# Le jeu commence ici
label start:

# Posons les variables ici
    $ magical_love = "False"
    $ mecha_love = "False"
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

    scene bg endoftheworld
    
    "En 2255, la Terre est menacée par l'armée du Roi des Trolls.{p}Le nouvel allié de l'humanité dans cette épreuve est des plus surprenants...{p}Personne n'aurait cru qu'après avoir détruit nos villes, mangé nos soldats et atomisé nos vies, ils se dresseraient maintenant face à nos ennemis...{p}Pour nous protéger..."
    
    "...{p}Les kaiju.{p}{cps=0}(Sans \"s\" parce que les mots japonais sont invariables, tudieu.){/cps}"
    
    "Ces monstres géants, terreurs de la nature sorties du fond des temps pour venir nous rappeler nos erreurs à coup de pattes dans les grands rues...{p}Ils sont maintenant nos camarades. Godzilla, Gamera et même Mothra font partie des nôtres.{p}Plus destructeurs que des tsunamis, leur fureur se déchaînera sur nos ennemis...{p}Mais seulement après l'heure du thé et des gâteaux."
    
    scene bg route with dissolve
    
    "Moi, je ne suis qu'un simple lycéen. Aujourd'hui, comme tous les jours, je vais en cours en faisant attention de ne pas me prendre les pieds dans les débris d'immeubles et les carcasses putréfiées."
    
    "Aieee !" with sshake
    
    "Abbah !" with sshake
    
    show troll with easeinbottom
    
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
    
    hide troll with dissolve
    
    "SPROTCH" with sshake
    
    show magical at center with move
    
    "Le troll ne court qu'à sa perte lorsqu'il attaque le plat du pied de Manaka la magical kaiju girl. Il ne reste alors de l'immonde personnage qu'un petit tas de paillettes."
    
    "Manaka se tourne alors vers moi."
    
    Magical "Ouf, tu es sain et sauf. Comment vas-tu ?"
    
    "Face à tant de grâce et de gentillesse, je ne sais répondre.{p}Cette magnifique créature m'a sauvé des griffes métaphoriques de l'immonde monstre."
    
    Magical "Oh, mon pauvre, tu as l'air bien secoué. Peux-tu au moins me dire quel est ton nom ?"
    
    $ player_name = renpy.input("(Mince, je ne me rappelle pas mon prénom ! Ma chute m'a rendu amnésique !){p}{cps=0}{i}(Tape ton sobriquet juste en dessous, il n'y a pas de petite boîte de dialogue jolie pour ça malheureusement. Mais tu peux en faire une en récupérant {a=https://github.com/HugoGelis/Wakanim-Live-Game-Jam}le code source du jeu{/a} !){/i}{/cps}")
    $ player_name = player_name.strip()
    $ player_name = "Jean-Pierre"
    
    JP "J... Je m'appelle {b}[player_name]{/b}."
    
    Magical "Enchantée de faire ta connaissance... Oh, mais j'ai oublié de me présenter !"
    
    "Un pas à gauche, trois pas à droite, une pirouette et des étincelles."
    
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
    jump highschool

label nope:

    hide magical
    
    JP "(Damnation ! Cette réponse que j'ai donné ! C'est une réplique digne d'une tsundere ! Ce maudit troll aurait-il réussit à me décontenancer ?)"
    
    "Je marche seul jusqu'au lycée, en me rongeant sang et ongles."

    jump highschool
    
label highschool:

    scene bg classe with dissolve
    
    "Ce matin, nous avons cours de technologie avec Monsieur Marcel."
    
    "La classe" "BROUHAHA. BROUHAHA."
    
    "Monsieur Marcel" "Au travail, bande de moules ! Pour le TP d'aujourd'hui, on va plancher sur une arme pour se défendre contre les trolls.{p}Rappelez-vous, le second amendement existe uniquement pour {b}votre{/b} sécurité !"
    
    "Nous nous mettons au travail derechef. Je fais équipe avec Jean-Claude, Jean-Paul et Jeanne-Michelle...{p}Mais dois rapidement travailler seul lorsqu'une mauvaise manipulation de la pile nucléaire irradie mes trois camarades."
    
    "Monsieur Marcel" "Mais c'est du beau boulot ça dis donc [player_name] !"
    
    JP "Merci m'sieur. Je n'en suis pas peu fier ! Un mech kaiju, ça c'est un beau TP !"
    
    "Monsieur Marcel" "Eh bien il va être temps de l'allumer, ce maudit bestiau."
    
    "Je m'exécute et pèse sur le piton."
    
    "Rise and shine!" with sshake
    
    "Monsieur Marcel" "Non pas le plafond enfin !" with sshake
    
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
    
    "J'ai un mouvement de recul instinctif face à tant de vilénie. Le malotru a osé me viser de ses armes de troll anti-troll !"
    
    JP "(Damned, le félon a touché juste avec son insulte ! Me voilà fort marri !)"
    
    JP "Ce... C'est... Même pas vrai ! D'abord !"
    
    Mecha "Oh mince, je crois que je vous ai blessé. Veuillez m'excuser, Maître."
    
    "D'un revers de queue, Motoko balaie un bâtiment situé un peu plus loin.{p}C'est (c'était) l'hôpital des adultes, de tous ceux qui survivent à peine à la post-apocalypse parce qu'ils ne sont plus de fringuants lycéens."
    
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
    
    JP "(Ce n'est même pas une insulte. A-t-il baissé les armes ? Je commence à l'apprécier...)"
    
    jump lunch

label nan:
    JP "Non seulement tu trolles, mais en plus tu n'es qu'une sale tsundere !" with sshake
    
    JP "Assume tes actions au lieu de te cacher derrière un stéréotype éculé !" with sshake
    
    JP "Tu ne vaux pas mieux que ces trolls contre lesquels tu es censé te battre !" with sshake
    
    Mecha "I... Idiot* !{p}{i}*N.D.T. : ça veut dire « Baka ».{/i}"
    
    jump lunch

label lunch:

    scene bg cour
    with dissolve

    "Après ce cours de techno qui ne fut pas de tout repos arrive enfin l'heure du déjeuner."
    
    JP "(Enfin un peu de tranquillité...)"
    
    "BOUM BOUM PAN PAN WIZZZZZ BIP BADABANG" with sshake
    
    JP "Qu'est-ce que c'est que ce vacarme ?!"
    
    "BADABANG PAM BOUM BOUM PATAPRO" with sshake
    
    "De l'autre côté de la cour du lycée se déroule un combat de titans. Deux kaiju se castagnent tandis qu'à leur pied, quelques élèves humains s'échangent des barres ChocoTipTop® en guise de paris."
    
    JP "Mais, je connais ces titans !"
    
    show magical at right with dissolve
    
    JP "Manaka ! Motoko ! Qu'est-ce que vous faites ?"
    
    "La magical kaiju girl rencontrée ce matin et le mecha kaiju construit la même demi-journée s'échangent des mandales sans courtoisie aucune !{p}Je m'égosille pour les interpeler mais peine à me faire entendre."
    
    Magical "Par le pouvoir de la tarte tropézienne ! Vil troll, je vais te punir !"
    
    Mecha "Mais enfin, il y a méprise ! Je ne suis pas un troll !"
    
    Magical "Ton vocabulaire est pourtant aussi disgracieux que celui de ces êtres répugnants ! Tu es des leurs, et subiras alors mon courroux !"
    
    Mecha "Je trolle mais pour le bien de tous ! Il s'agit d'une arme que je ne veux pas employer sur vous ! Mais si vous m'y obligez..."
    
    JP "{b}CESSEZ !{/b}{p}Vous vous enguirlandez pour des prunes !" with sshake
    
    "Enfin les deux kaiju entendent la voix de la raison - la mienne - et tournent la tête en ma direction."
    
    #réécrire d'ici
    
    Magical "[player_name] ! Tu as raison ! Notre bataille est stérile !"
    
    Mecha "Maître, vous détenez la vérité."
    
    Magical "Mais il va te falloir choisir..."
    
    Mecha "Qui de moi ou elle préférez-vous ?"
    
menu:
    JP "Mon cœur est tiraillé... Qui vais-je choisir ?"
    "Manaka la magical kaiju girl..." if magical_love == "True":
        jump magicalend
    "Motoko le mecha kaiju..." if mecha_love == "True":
        jump mechaend
    "Je préfère partir plutôt que de voir ça plutôt que d'être aveugle.":
        jump badend
    
label magicalend:
    
    "En vrai, les mechas, c'est trop nul et rien ne vaut le pouvoir magique de la tarte tropézienne."
    
    jump generique

label mechaend:
    
    hide magical
    
    "La technologie c'est l'avenir ! On va remplacer toutes les magical girls par des mechas et botter le popotin de l'apocalypse des monstres avec d'autres monstres !"
    
    jump generique
    
label badend:
    
    hide magical
    
    JP "Ah mais... Je suis tout seul en fait."
    
    JP "C'est nul."
    
    JP "Je m'ennuie déjà."
    
    JP "Ça serait chouette si je pouvais recommencer... Ou même réécrire toute l'histoire..."
    
    JP "Si seulement j'avais de quoi changer le code de cette réalité en open source..."
    
    jump generique
    
label generique:
    scene wakalive

    "Ce jeu a été réalisé dans le cadre d'une initiative de Wakanim Live pour montrer que tout le monde peut faire des jeux vidéo.{p}Qu'ils soit simples, stupides ou moches, c'est pas si dur de créer des trucs.{p}Alors prenez-vos dix doigts, ceux de vos copains et faisez des machins !"
    
    "Coupable : {a=https://twitter.com/hugo_gelis}Hugo Gelis{/a}{p}Page du projet sur GitHub : {a=https://github.com/HugoGelis/Wakanim-Live-Game-Jam}https://github.com/HugoGelis/Wakanim-Live-Game-Jam{/a}{p}Merci à Ben, Seiko Ralie, Joystickman et Marc-Antoine pour les bonnes idées lancées pendant le {a=https://www.youtube.com/watch?v=h9oPsSUe_ng}Wakanim Live #3{/a} !{p}Merci également à Raphaël et Astrid, les {i}partners in crime{/i} !"
    
    "Merci d'avoir testé ce petit jeu, et à la prochaine sur {a=http://www.wakanim.tv/}Wakanim.TV{a} !"
    
    "#bagarre{p}★~FIN~★"
    return