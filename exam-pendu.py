import random
import os
import time
 
def choisir_mot(niveau):
    niveaux = {
        "1": ["pomme", "table", "rivet", "livre", "roule","actif","agile","bacon"],
        "2": ["liquide", "cuisine", "matinee", "bananes", "nouveau"],
        "3": ["television", "universite", "champignon", "electrique", "conference"]
    }
    return random.choice(niveaux[niveau])
 
reset = "\033[0m"
underline = "\033[4m"
italic = "\033[3m"
yellow = "\033[1;33m"
light_red = "\033[1;31m"
cyan = "\033[0;36m"
light_green = "\033[1;32m"
red = "\033[0;31m"
light_white = "\033[1;37m"
purple = "\033[0;35m"
brown = "\033[0;33m"
green = "\033[0;32m"
 
os.system('cls')
print(""" _____         _                 _          _
|_   _|__  ___| |__  _ __   ___ | |__   ___| |
  | |/ _ \\/ __| '_ \\| '_ \\ / _ \\| '_ \\ / _ \\ |
  | |  __/ (__| | | | | | | (_) | |_) |  __/ |
  |_|\\___|\\___|_| |_|_| |_|\\___/|_.__/ \\___|_|""")
time.sleep(1)
os.system('cls')
 
print("""            
       
     
                        ET                
     
     
      """)
time.sleep(1)
os.system('cls')
 
print("""               __                  ____          
        ____ _/ /___ _____        / __/_  ______
       / __ `/ / __ `/ __ \  __  / /_/ / / / __ \\
      / /_/ / / /_/ / /_/ / __  / __/ /_/ / / / /
      \__,_/_/\__, /\____/     /_/  \__,_/_/ /_/
             /____/        
""")
 
time.sleep(1)
os.system('cls')
 
print("""            
       
     
                VOUS PRESENTE                                  
     
     
      """)
 
time.sleep(1)
os.system('cls')
 
print(yellow+"+---------------------------------+"+reset)
print(yellow+underline+"|"+reset,light_red+underline+italic+"       LE JEU DU PENDU!        "+reset, yellow+underline+"|"+reset)
print(yellow+"+---------------------------------+"+reset)
print("")
time.sleep(2)
niveaux_reussis = {"1": 0, "2": 0, "3": 0}

def pendu():

    rejouer = 'o'  
    while rejouer.lower() == 'o':

        for niveau in niveaux_reussis:
            reussis = niveaux_reussis[niveau]
            print(f"\nDifficulté {niveau}: {reussis} niveaux réussis\n")

        print(yellow+"+---------------------------------+"+reset)
        print(yellow+"|"+reset,cyan+"     Niveaux de difficulté :"+reset,yellow+"   |"+reset)
        print(yellow+"+---------------------------------+"+reset)
        print(yellow+"|"+reset,light_white+"1"+reset,yellow+"|"+reset,light_white+"  Facile  "+reset,yellow+"   |"+reset,light_white+"5 lettres"+reset,yellow+"  |"+reset)
        print(yellow+"|"+reset,light_green+"2"+reset,yellow+"|"+reset,light_green+"  Moyen  "+reset,yellow+"    |"+reset,light_green+"7 lettres "+reset,yellow+" |"+reset)
        print(yellow+"|"+reset,red+"3"+reset,yellow+"|"+reset,red+"  Difficile  "+reset,yellow+"|"+reset,red+"10 lettres"+reset,yellow+" |"+reset)
        print(yellow+"+---------------------------------+\n"+reset)  
        niveau = input(purple+("Sélectionnez un niveau (1/2/3) : ")+reset)
       
        while niveau not in ["1", "2", "3"]:
            print(red+("Niveau inconnu. Veuillez saisir 1, 2 ou 3 svp")+reset)
            niveau = input(purple+("Sélectionnez un niveau (1/2/3) : ")+reset)
           
        mot_solution = choisir_mot(niveau)
        tentatives = 7
        affichage = "_" * len(mot_solution)
        lettres_trouvees = ""
        lettres_erronees = set()
   
        while tentatives >= 0:
            print(light_green+("\nMot à deviner :")+reset, affichage)
            print(light_white+("\nTentatives restantes :")+reset, tentatives)
            print(light_red+("\nLettres incorrectes :")+reset, ", ".join(lettres_erronees))
 
            if tentatives == 0:
                print(f"\nle mot recherché était : {mot_solution}")
                print(brown+"""
 ==========Y=
 ||/       |  
 ||        0  
 ||       /|\\
 ||       / \\  
/||              
=============="""+reset)
                print(red+("\n    * Fin de la partie *    ")+reset)
                break
 
            match tentatives:
                case 1:
                    print(brown+"""
 ||/       |  
 ||        0  
 ||       /|\\
 ||       / \\  
/||              
=============="""+reset)
                case 2:
                    print(brown+"""
 
 ||        0  
 ||       /|\\
 ||       / \\  
/||              
=============="""+reset)
                case 3:
                    print(brown+"""
 
 
 ||       /|\\
 ||       / \\  
/||              
=============="""+reset)
                case 4:
                    print(brown+"""
 
 
 
 ||       / \\  
/||              
=============="""+reset)
                case 5:
                    print(brown+"""
 
 
 
 
/||              
=============="""+reset)
                case 6:
                    print(brown+"""
                   
 
 
 
                   
=============="""+reset)
 
            proposition = input(cyan+("\nProposez une lettre : ")+reset)[0:1].lower()
 
            if not proposition.isascii() or not proposition.islower() or len(proposition) != 1:
                print(red+("Entrée invalide.")+reset)
                continue
 
            if proposition in lettres_erronees:
                print(f"Vous avez déjà proposé la lettre '{proposition}'.")
            elif proposition in mot_solution:
                lettres_trouvees = lettres_trouvees + proposition
                print(cyan+("\n-> Bien joué! On continue comme ca!!")+reset)
               
            else:
                lettres_erronees.add(proposition)
                tentatives -= 1
                print(red+("\n -> Raté! on persévère! :) \n")+reset)
                   
            affichage = ""
            for lettre in mot_solution:
                if lettre in lettres_trouvees:
                    affichage += lettre
                else:
                    affichage += "_"
                   
            if "_" not in affichage:
                print("\n>>> Gagné! <<<")
                niveaux_reussis[niveau] += 1
                break
       
        rejouer = input(green+("\n Voulez-vous rejouer ? (o/n) : ")+reset)
        os.system('cls')
        while rejouer != "o" and rejouer != "n":
            os.system('cls')
            print(red+("entrée invalide.")+reset)
            rejouer = input(green+("\n Voulez-vous rejouer ? (o/n) : \n")+reset)
           
    if rejouer.lower() == 'n':
        os.system('cls')
        print(light_white+("\n Merci d'avoir joué! :-) ")+reset)
        time.sleep(1)
        print(light_white+("\n A la prochaine!")+reset)
        time.sleep(1)
        print(purple+("\n(Pour plus d'infos sur les prochaines sorties de jeu, rejoignez-nous sur"+reset),(italic+underline+purple+"https://algo-fun.org)\n")+reset)
       
pendu()
