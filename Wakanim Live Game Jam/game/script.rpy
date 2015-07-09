# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image logo wakalive = "images/logowakalive.png"
image Wakalive moche = "images/wakalive.png"
image bg cheum = "images/fond.png"

# Déclarez les personnages utilisés dans le jeu.
define JP = Character('[player_name]', color="#17c9aa")
define Magical = Character('Manaka', color="#e81ae1")
define Mecha = Character('Marcel', color="#8c8181")

label spashscreen:
    show logo wakalive
    with Pause(2)
    return

# Le jeu commence ici
label start:

# Posons les variables ici
    $ magical_love = "False"
    $ mecha_love = "False"

    "En 2255, la Terre est menacée par l'armée du Roi des Trolls.{p}Le nouvel allié de l'humanité dans cette épreuve est des plus surprenants...{p}Personne n'aurait cru qu'après avoir détruit nos villes, mangé nos soldats et atomisé nos vies, ils se dresseraient maintenant face à nos ennemis...{p}Pour nous protéger..."
    
    "...{p}Les kaiju.{p}(Sans \"s\" parce que les mots japonais sont invariables, tudieu.)"
    
    "Ces monstres géants, terreurs de la nature sorties du fond des temps pour venir nous rappeler nos erreurs à coup de pattes dans les grands rues...{p}Ils sont maintenant nos camarades. Godzilla, Gamera et même Mothra font partie des nôtres.{p}Plus destructeurs que des tsunamis, leur fureur se déchaînera sur nos ennemis...{p}Mais seulement après l'heure du thé et des gâteaux."
    
    #transition
    
    "Moi, je ne suis qu'un simple lycéen. Aujourd'hui, comme tous les jours, je vais en cours en faisant attention de ne pas me prendre les pieds dans les débris d'immeubles et les carcasses putréfiées."
    
    #show une scène boum
    
    "Ouch !" with vpunch
    
    "Aieee !" with hpunch
    
    #show troll grunt
    
    "Troll péon" "Haha ! Je suis un vilain troll et je vais t'attaquer ! Accroche toi à ton amour propre parce que je vais te faire des remarques très désobligeantes dont tu te souviendras même aux cabinets !"
    
    "!!!{p}Mon popotin est déjà tout endolori de la chute surprise provoquée par ce malotru, comment vais-je me sortir ce ce traquenard ?!"
    
    "Troll péon" "C'est le plan de notre Roi Tsundere ! En attaquant ta virilité et ton estime de soi, je vais te transformer en cliché de mauvais soujo manga ! Tu ne seras que doute et te vautreras dans les clichés éculés d'une romance aliénante et avilissante !"
    
    Magical "Halte là, gredin ! Par le pouvoir de la tarte tropézienne, je ne te laisserai pas salir la dignité de ce monde !"
    
    "150 mètres de magie et de dentelles se dressent désormais entre moi et mon agresseur."
    
    "Troll Péon" "Damnation ! Une magical kaiju girl ! Mais ce n'est qu'un contre-temps ! Je vais me débarasser d'elle d'un revers de remarque irrévérencieuse !"
    
    Magical "Nenni, vilain ! Car je suis {b}Manaka du Corbeau{/b} ! ★~❤"

    "Troll Péon" "Enfer ! C'est la plus puissante des magical kaiju girls ! Que vais-je pouvoir faire mis à part trembler des genoux en {cps=10}chargeaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANT !{/cps}"
    
    "SPROTCH" with vpunch
    
    "Le troll ne court qu'à sa perte lorsqu'il attaque le plat du pied de Manaka la magical kaiju girl. Il ne reste alors de l'immonde personnage qu'un petit tas de paillettes."
    
    "Manaka se tourna alors vers moi."
    
    Magical "Ouf, tu es sain et sauf. Comment vas-tu ?"
    
    "Face à tant de grâce et de gentillesse, je ne sais répondre.{p}Cette magnifique créature m'a sauvé des griffes métaphoriques de l'immonde monstre."
    
    Magical "Oh, mon pauvre, tu as l'air bien secoué. Peux-tu au moins me dire quel est ton nom ?"
    
    $ player_name = renpy.input("(Mince, je ne me rappelle pas mon prénom ! Ma chute m'a rendu amnésique !){p}{i}(Tape ton sobriquet juste en dessous, il n'y a pas de petite boîte de dialogue jolie pour ça malheureusement. Mais tu peux en faire une en récupérant {a=https://github.com/HugoGelis/Wakanim-Live-Game-Jam}le code source du jeu{/a} !){/i}")
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
    "Assurément":
        jump yep
    "N... Non, je peux très bien me débrouiller tout seul. ":
        jump nope
        
label yep:
    Magical "Super !{p}Oh, il est déjà si tard ! Vite, hâtons nous pour ne pas être en retard en cours !"
    $ magical_love = "True"
    jump highschool

label nope:
    JP "(Damnation ! Cette réponse ! C'est une réplique digne d'une tsundere ! Ce maudit troll aurait-il réussit à me décontenancer ?)"
    
    "Je marche seul jusqu'au lycée, en me rongeant sang et ongles."

    jump highschool
    
label highschool:
    "Ce matin, nous avons cours de technologie avec Monsieur Marcel."
    
    "La classe" "BROUHAHA. BROUHAHA."
    
    Mecha ""

    "présente une arme pour se défendre contre les kaiju"
    "J... j'ai pas détruit la ville parce que je t'aime..."
    "Je suis un troll mais pas comme les méchants ! Je ne suis pas un infiltré !"
    
    
menu:
    Mecha "Bip Bip Boum Boum."
    "amour":
        jump ouais
    "damnation":
        jump nan
        
label ouais:
$ mecha_love = "True"

label nan:

    jump lunch

label lunch:
    "youpi banane"
menu:
    JP "c'est l'heure du choix"
    "l'un" if magical_love == "True":
        jump magicalend
    "l'autre" if mecha_love == "True":
        jump mechaend
    "solitude":
        jump badend
    
label magicalend:
    "kapoué ?"
    jump generique

label mechaend:
    "kapoué !"
    jump generique
    
label badend:
    "kapoué"
    jump generique
    

    
label generique:
    "Bravo, t'as gagné !"
    
    "Ce jeu a été réalisé dans le cadre d'une initiative de Wakanim Live pour montrer que tout le monde peut faire des jeux vidéo. Qu'ils soit simples, stupides ou moches, c'est pas si dur d'en faire."