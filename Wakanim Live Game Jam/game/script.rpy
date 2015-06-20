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

    Wakalive "Mais quel monstre géant allons-nous séduire ?"
    
    "2255 des kaiju combattent le roi des troll. ce roi n'est autre que Tsundere un jeune troll héritier du trône qui veut transformer le monde en shojo manga"
    
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
