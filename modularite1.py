'''
MODULARITÉ EN PYTHON: Utiliser les modules
------------------------------------------
Index des modules Python
https://docs.python.org/fr/3/py-modindex.html

random  Génère des nombres pseudo-aléatoires

math    Fonctions mathématiques

import random
from random import random, randrage
from random import *        -->permet d'importer la globalité du module random
import random as r

import os                   -->permet d'utiliser des commandes de mon système d'exploitation
'''

import random

print(random.randrange(100))    #nombre aléatoire entre 1 et 100

print("--------50 nombres aléatoire-----------")


#va afficher 50 nombres aléatoire entre 1 et 100
for i in range(50):

    print(random.randrange(100))



print("---------------------------------------")

#va afficher 10 nombres aléatoire entre 0 et 1
for i in range(10):

    print(random.random())


'''
import random as r

print(r.random())
print(r.randrange(1000))

'''

'''
from random import random, randrage

for i in range(50):

    print(randrange(100))

'''

'''
import os


os.system("clear")  #pour vider le terminal
'''