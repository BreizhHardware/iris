#!/usr/bin/env python

def readPoints(filename, indexes):
    """ Renvoie les informations du fichier filename sous la forme
        d'un dictionnaire dont
            * une clé est un point
            * la valeur associée est la classe d'appartenance du point.

        indexes : indices des attributs à récupérer.
    """
    
    p = '['
    fichier = open(filename, 'r')
    iris = {}

    fichier.readline()
    
    for line in fichier:
        line = line.split(',')
        line[4] = line[4][0]  #retire le \n
        
        for u in range(len(indexes)):
            j = [float(line[indexes[u]]) for u in range(len(indexes))]
        j = tuple(j)
        iris[j] = line[4] 

        
    fichier.close()

    return iris




def dist(P1, P2):
    """ Renvoie la distance entre les points P1 et P2.
        P1 et P2 sont deux points dans un espace de dimension quelconque.
    """

    P = 0
    x = []
    for i in range(len(P1)):
        x.append(float(P2[i]) - float(P1[i]))      #on mesure chacune des longueurs (vecteur)
    for i in (x):
        P = P + i**2            #formule de module
    P = P**0.5                  # puissance 0.5 = racine carré

    return P



def prediction(clsPoints, P, k):
    """ Renvoie la classe d'appartenance du point en utilisant le
        jeu de données clsPoints et en appliquant la méthode des
        k plus proches voisins.
    """
    D = clsPoints
    fleur0 =0
    fleur1 =0
    fleur2 =0
    l = []
    D2 = {}
    for i in D.keys():
        l.append(dist(i, P))
        D2[dist(i, P)] = i
    liste = sorted(l)
    
    
    for u in range(k):
        if D[D2[liste[u]]] == '0':    
            fleur0 += 1
        elif D[D2[liste[u]]] == '1':
            fleur1 += 1
        else:
            fleur2 += 1
   
    end = [fleur0, fleur1, fleur2]
    
    
    if max(end) == fleur0:
        return 0 
    elif max(end) == fleur1:
        return 1 
    else:
        return 2
