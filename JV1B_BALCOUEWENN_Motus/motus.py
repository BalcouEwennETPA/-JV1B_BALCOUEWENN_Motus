#rouge = bonne lettre
#bleu = mauvaise lettre
#magenta = bonne lettre mais mal placé


import random
from colorama import init
init()
from colorama import Fore, Back, Style


#prendre au hasard un mot sur 10 possibilités differentes

listeMots =["girafe","accuse","dragon","belier","buteur","canard","cuivre","script","splash","rideau"]
motaleatoire = listeMots [random.randrange (0,len(listeMots))]

#def lettreindex ():
    #listeMots =["girafe","accuse","dragon","belier","buteur","canard","cuivre","script","splash","rideau"]
    #motaleatoire = listeMots [random.randrange (0,len(listeMots))]
    #for i in range (len(motaleatoire)):
        #if motaleatoire[i]=="a":
            #return i

#fonction de la victoire et couleur sur un mot

def motcouleur ():
    
    listeMots =["girafe","accuse","dragon","belier","buteur","canard","cuivre","script","splash","rideau"]
    
    motaleatoire = listeMots [random.randrange (0,len(listeMots))]
    
    print(motaleatoire)
    
    motdemande = input("quelle mot voulez vous tester ?")
    if (motaleatoire) == (motdemande) :
        print (Fore.RED + (motaleatoire))
        print (Style.RESET_ALL + "Vous avez gagné bien joué")
    if (motaleatoire) != (motdemande) :
        print (Fore.BLUE +(motdemande))

#fonction de la couleur sur des lettres

def lettrecouleur ():
    
    listeMots =["droite","accuse","gauche","belier","buteur","canard","cuivre","script","splash","rideau"]
    
    motaleatoire = listeMots [random.randrange (0,len(listeMots))]
    
    print(motaleatoire)
    
    motdemande = input("quelle mot (six lettre) voulez vous tester ?")

    for i in range (len(motaleatoire)) :
        if motaleatoire[i] == motdemande[i] :
            print (Fore.RED + motaleatoire[i]);
        if motaleatoire[i] != motdemande[i] :
            print (Fore.BLUE + motdemande[i]);
        #if (motaleatoire) == (motdemande) :
            #print (Style.RESET_ALL + "Vous avez gagné bien joué")

motcouleur ()
lettrecouleur () 