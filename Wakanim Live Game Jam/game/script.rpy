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
    
    "2255 des magical-kaiju combattent le roi des troll. ce roi n'est autre que Tsundere un jeune troll  héritier du trône qui n'avait que pour projet de crée un shojo manga  en s'inspirant de kaiju mécas"
    
menu:
    "Le kaiju magical girl !":
        jump magicalgirl
        
    "Le mecha kaiju !":
        jump mecha
        
    "Le kaiju tsundere !":
        jump tsundere
        
label magicalgirl:
    " il était une fois, un joli petit kaiju tout triste parce qu'il se faisait martyriser par de méchants trolls mais un jour un kaiju Magicalgirl arriva et le réconforta, ce fut le début d'une jolie romance"

return
    
label tsundere:
    
    "J... j'ai pas détruit la ville parce que je t'aime..."
    
    return
    
label mecha:
    
    "Bip Bip Boum Boum."
    
    return