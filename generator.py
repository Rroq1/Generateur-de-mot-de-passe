import random
from tkinter import *

# 1 : Création de la fenêtre Tkinter
fenetre = Tk()
fenetre.title("Générateur de mot de passe")
fenetre.minsize(500, 300)

# 2 : Titre
titre = Label(fenetre, text="Combien de caractères voulez-vous dans votre mot de passe ?")
titre.pack()

# 3 : Champ pour entrer la longueur du mot de passe
expression = StringVar()
entree = Entry(fenetre, textvariable=expression, width=30)
entree.pack(pady=10)

# 4 : Le label pour afficher le mot de passe généré
resultat = StringVar()
sortie = Entry(fenetre, textvariable=resultat, width=40)
sortie.pack()

# 5 : Fonction pour générer le mot de passe utilisant la première version du générateur
def generer_mot_de_passe():
    try:
        longueur = int(expression.get())
        
        lettres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nombres = '0123456789'
        symboles = '!#$%&()*+'
        
        ensemble_des_caracteres = lettres + nombres + symboles
        
        mot_de_passe = [
            random.choice(lettres),
            random.choice(nombres),
            random.choice(symboles)
        ]

        for _ in range(longueur - 3):
            mot_de_passe.append(random.choice(ensemble_des_caracteres))

        random.shuffle(mot_de_passe)

        mot_de_passe_final = ''.join(mot_de_passe)
        resultat.set(mot_de_passe_final)
    except ValueError:
        resultat.set("Veuillez entrer un nombre valide.")

bouton = Button(fenetre, text="Générer", command=generer_mot_de_passe)
bouton.pack(pady=10)

fenetre.mainloop()
