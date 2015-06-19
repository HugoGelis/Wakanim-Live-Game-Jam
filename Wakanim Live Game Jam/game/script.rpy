# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image Wakalive moche = "wakalive.png"
image bg cheum = "fond.png"

# Déclarez les personnages utilisés dans le jeu.
define Wakalive = Character('Hugo', color="#e81ae1")

# Le jeu commence ici
label start:
    scene bg cheum
    show Wakalive moche

    Wakalive "Faisons-nous plutôt une romance avec des monstres géants ? Ou plutôt un jeu de community management de combat ?"

    "Public" "Nous allons répondre !"
    
menu:
    "On aime les monstres !":
        jump kaiju
        
    "On aime pas les trolls !":
        jump troll
        
label kaiju:
    "Public" "Allez, on va séduire des kaiju !"
    
    Wakalive "Mais c'est une super idée !"

return
    
label troll:
    "Public" "Bouh les trolls ils sont trop méchants !"
    
    Wakalive "D'accord, d'accord, prenez vos perches, ça va barder !"

    return