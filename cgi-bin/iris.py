#!/usr/bin/env python
from knn import *
import cgi
import cgitb

L = []
S = []
K = []
U = []
cgitb.enable()

irisFile = ("assets/iris.csv")


form = cgi.FieldStorage() # Renvoie les données du formulaire sous
                          # la forme d'un dictionnaire.
if 'sepal-length' in form:
    sepalLength = float(form['sepal-length'].value)
    L.append(sepalLength)
    S.append("longueur des sépales")
    K.append(0)
    U.append(float(form['sepal-length'].value))
if 'sepal-width' in form:
    sepalWidth = float(form['sepal-width'].value)
    L.append(sepalWidth)
    S.append("largeure des sépales")
    K.append(1)
    U.append(float(form['sepal-width'].value))
if 'petal-length' in form:
    petalLength = float(form['petal-length'].value)
    L.append(petalLength)
    S.append("longueur des pépales")
    K.append(2)
    U.append(float(form['petal-length'].value))
if 'petal-width' in form:
    petalWidth = float(form['petal-width'].value)
    L.append(petalWidth)
    S.append("largeur des pépales")
    K.append(3)
    U.append(float(form['petal-width'].value))

if len(K) == 2:
    nmb = (K[0], K[1])
elif len(K) == 3:
    nmb = (K[0], K[1], K[2])
else:
    nmb = (K[0], K[1], K[2], K[3])

if len(U) == 2:
    meze = (U[0], U[1])
elif len(U) == 3:
    meze = (U[0], U[1], U[2])
else:
    meze = (U[0], U[1], U[2], U[3])

a = readPoints(irisFile, (nmb)) 
prout = prediction(a, (meze), 5)
    
if prout == 0:
    espir = 'Setosa'
elif prout == 1:
    espir = 'Versicolor'
else:
    espir = 'Virginica'
a = len(L)
i= 0
txt=""

while i < a:
        txt = txt + "<ul>  <li> <p> " + "La valeur est de " + str(L[i]) + " pour la " + S[i] + " </p>  </li> </ul> \n"
        i = i + 1



print (f'''
    <!DOCTYPE html>
    <html>
       <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="../assets/css/style_iris.css" />
            <title>Résultat</title>
        </head>
        <body>
            <h1 class="titre">Reconnaissance d'une iris</h1>
            {txt}
            <p>Il s'agit probablement de l'espèce <strong>{espir}</strong></p>
            <div style = "position:relative; left:850px; bottom:250px";
            <center><img src = ../assets/pic/{espir}.jpeg></center>
        </body>
        ''')