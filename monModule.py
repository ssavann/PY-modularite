'''
Module de calcul mathématique
Doctype     Documenter le programme
'''

def carre(x):
    return x * x

def somme(x,y):
    print(f"la somme de {x} + {y} est de {x + y}")
    


#va être exécuter au niveau du module, mais pas du programme
if __name__ == "__main__":
    somme(15,3)