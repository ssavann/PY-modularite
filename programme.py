'''
MODULARITE : Tester son module

Programme principal

'''

print("Je suis le programme principal")
'''
import mesModules.monModule    #va chercher le fichier monModule.py dans un dossier

print("-------------------")

print("le carre de 2 est de", mesModules.monModule.carre(2))

print("-------------------")


mesModules.monModule.somme(15,5)
'''


#Une autre façon d'importer et mettre le lien dans "m"
#lorsque le module est dans un sous dossier 
import mesModules.monModule as m

print("-------------------")

print("le carre de 2 est de", m.carre(2))

print("-------------------")


m.somme(15,5)

print("-------------------")











