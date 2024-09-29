
import random

# 1 : Je pose la question à l'utilisateur
question = int(input("Combien de caractères voulez-vous dans votre mot de passe ? "))

# 2 : Je définis différentes catégories de caractères
lettres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nombres = '0123456789'
symboles = '!#$%&()*+'

# 3 : J'aoute toutes les catégories ensemble
ensemble_des_caracteres=lettres+nombres+symboles


# 4 : J'assure qu'il y a au moins chaque type de catégorie dans le mot de passe
mot_de_passe = [
    random.choice(lettres),
    random.choice(nombres),
    random.choice(symboles)
]

# 5 : Je remplis le reste du mot de passe avec des caractères aléatoire
for n in range(question - 3):
    mot_de_passe.append(random.choice(ensemble_des_caracteres))

# 6 :  Je mélange l'ordre des caractères
random.shuffle(mot_de_passe)

# 7 : Je transforme mon mot de passe en chaîne de caractère
mot_de_passe_final = ''.join(mot_de_passe)

# 8 : J'affiche le mot de passe dans le terminal
print("Votre mot de passe généré est :", mot_de_passe_final)