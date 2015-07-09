# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image logo = "images/logowakalive.png"
image Wakalive moche = "images/wakalive.png"
image bg cheum = "images/fond.png"

# Déclarez les personnages utilisés dans le jeu.
define JP = Character('Jean-Pierre', color="#e81ae1")
define Magical = Character('Magical Kaiju', color="#e81ae1")

label spashscreen:
    show logo
    with pause(2)
    return

# Le jeu commence ici
label start:
    "En 2255, la Terre est menacée par l'armée du Roi des Trolls.{p}Le nouvel allié de l'humanité dans cette épreuve est des plus surprenants...{p}Personne n'aurait cru qu'après avoir détruit nos villes, mangé nos soldats et atomisé nos vies, ils se dresseraient maintenant face à nos ennemis...{p}Pour nous protéger..."
    
    "...{p}Les kaiju."
    
    scene bg cheum
    show Wakalive moche
    
    "Ces monstres géants, terreurs de la nature sorties du fond des temps pour venir nous rappeler nos erreurs à coup de pattes dans les grands rues...{p}Ils sont maintenant nos camarades.{p}Plus destructeurs que des tsunamis, leur fureur se déchaînera sur nos ennemis...{p}Mais seulement après l'heure du thé et des gâteaux."
    
    "Moi, je ne suis qu'un simple lycéen. Aujourd'hui, comme tous les jours, je vais en cours en faisant attention de ne pas me prendre les pieds dans les débris d'immeubles et les carcasses putréfiées."
    
    #show une scène boum
    
    "Ouch !" with vpunch
    
    "Aieee !" with hpunch
    
    #show troll grunt
    
    "Troll péon" "Haha ! Je suis un vilain troll et je vais t'attaquer ! Accroche toi à ton amour propre parce que je vais te faire des remarques très désobligeantes dont tu te souviendras même aux cabinets !"
    
    "!!!"
    
    "C'est le plan de notre Roi Tsundere ! En attaquant ta virilité et ton estime de soi, je vais te transformer en cliché de mauvais soujo manga ! Tu ne seras que doute et te vautreras dans les clichés éculés d'une romance aliénante et avilissante !"
    
    Magical "lalala"
    
    "magical kaiju arrive"
    
    "comment s'appelle"
    
    $ player_name = renpy.input("Comment que j'm'appelle déjà ?")
    $ player_name = player_name.strip()
    $ player_name = "Jean-Pierre"
    
    "Meu m'apel %(player_name)s."
    
    "aller avec magical kaiju ou faire sa tsundere... est-il contaminé ?"

menu:
    "Le kaiju magical girl !":
        jump magicalgirl
    "Le mecha kaiju !":
        jump mecha
    "Le kaiju tsundere !":
        jump tsundere
    "Le kaiju troll !":
        jump troll
    
label magicalgirl:
    "Notre héros (héroïne) est attaqué(e) par les trolls ! Il(elle) se fait martyriser tous les jours au lycée. Un jour, le kaiju magical girl arrive et le (la) réconforte(a). C'est le début d'une belle histoire..."
    return
    
label tsundere:
    "J... j'ai pas détruit la ville parce que je t'aime..."
    return
    
label mecha:
    "Bip Bip Boum Boum."
    return
    
label troll:
    "Je suis un troll mais pas comme les méchants ! Je ne suis pas un infiltré !"
    return