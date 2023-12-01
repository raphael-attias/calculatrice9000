# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#programme en-tete programme python
#version python : 
#auteur : ATTAS Raphaël
#email : raphael.attias@laplateforme.io

from tkinter import *
from sympy import sympify, N

y = ""
historique = []

def bouton_clique(valeur):
    global y
    if reponse.get("1.0", "end-1c") == "Erreur: ":
        effacer()
    reponse.insert(END, str(valeur))
    y += str(valeur)

def gerer_erreur(exception):
    if isinstance(exception, (ValueError, SyntaxError)):
        return "Erreur: Expression mathématique invalide"
    elif isinstance(exception, ZeroDivisionError):
        return "Erreur: Division par zéro"
    else:
        return "Erreur inattendue: " + str(exception)

def bout_plus_minus():
    global y
    if not y:
        bouton_clique("-")
    elif y[-1] in "+-*/(":
        bouton_clique("-")
    else:
        effacer()
        reponse.insert(END, gerer_erreur(ValueError("Entrée invalide")))
        y = ""

def bout_point():
    global y
    if not y or y[-1] in "+-*/(":
        bouton_clique("0")
    elif "." not in y:
        bouton_clique(".")

def bout_operateur(operateur):
    global y
    if y and y[-1] not in "+-*/(":
        bouton_clique(operateur)
    elif operateur == "-" and (not y or y[-1] in "+*/("):
        bout_plus_minus()

def resultat():
    global y, historique
    if y:
        try:
            expression = sympify(y)
            result = round(float(N(expression)), 8)
            historique.append(y + " = " + str(result))
            reponse.delete("1.0", END)
            reponse.insert(END, str(result) + '\n')
        except Exception as e:
            effacer()
            reponse.insert(END, gerer_erreur(e))
        y = ""

def effacer():
    global y
    reponse.delete("1.0", END)
    y = ""

def afficher_historique():
    global historique
    for calcul in historique:
        reponse.insert(END, calcul + '\n')

fenetre = Tk()
fenetre.geometry("300x500")
fenetre.title("Calculatrice")

reponse = Text(fenetre)
reponse.grid(row=3, column=1, columnspan=6)
reponse.config(height=10, width=30, font=15)

# Création des boutons
bouton1 = Button(fenetre, text='1', width=5, font=15, command=lambda: bouton_clique(1))
bouton2 = Button(fenetre, text='2', width=5, font=15, command=lambda: bouton_clique(2))
bouton3 = Button(fenetre, text='3', width=5, font=15, command=lambda: bouton_clique(3))
bouton4 = Button(fenetre, text='4', width=5, font=15, command=lambda: bouton_clique(4))
bouton5 = Button(fenetre, text='5', width=5, font=15, command=lambda: bouton_clique(5))
bouton6 = Button(fenetre, text='6', width=5, font=15, command=lambda: bouton_clique(6))
bouton7 = Button(fenetre, text='7', width=5, font=15, command=lambda: bouton_clique(7))
bouton8 = Button(fenetre, text='8', width=5, font=15, command=lambda: bouton_clique(8))
bouton9 = Button(fenetre, text='9', width=5, font=15, command=lambda: bouton_clique(9))
bouton0 = Button(fenetre, text='0', width=5, font=15, command=lambda: bouton_clique(0))
boutonpoint = Button(fenetre, text=',', width=5, command=bout_point, bg="red")
boutonplus = Button(fenetre, text='+', width=4, command=lambda: bout_operateur("+"), bg="red")
boutonmoins = Button(fenetre, text='-', width=4, command=lambda: bout_operateur("-"), bg="red")
boutonfois = Button(fenetre, text='x', width=4, command=lambda: bout_operateur("*"), bg="red")
boutondiv = Button(fenetre, text='/', width=4, command=lambda: bout_operateur("/"), bg="red")
boutonpargauche = Button(fenetre, text='(', width=5, command=lambda: bouton_clique("("), bg="red")
boutonpardroite = Button(fenetre, text=')', width=5, command=lambda: bouton_clique(")"), bg="red")
boutonegale = Button(fenetre, text='=', width=6, command=resultat, bg="red")
boutoneffacer = Button(fenetre, text="supr", width=4, command=effacer, bg="red")

# Nouveaux boutons
boutonplus_minus = Button(fenetre, text="+/-", width=5, command=bout_plus_minus, bg="red")

# Placement des boutons avec grid
bouton1.grid(row=9, column=1)
bouton2.grid(row=9, column=2)
bouton3.grid(row=9, column=3)
bouton4.grid(row=7, column=1)
bouton5.grid(row=7, column=2)
bouton6.grid(row=7, column=3)
bouton7.grid(row=5, column=1)
bouton8.grid(row=5, column=2)
bouton9.grid(row=5, column=3)
bouton0.grid(row=11, column=2)
boutonpoint.grid(row=11, column=3)
boutonplus.grid(row=5, column=4)
boutonmoins.grid(row=7, column=4)
boutonfois.grid(row=9, column=4)
boutondiv.grid(row=11, column=4)
boutonpargauche.grid(row=13, column=1)
boutonpardroite.grid(row=13, column=2)
boutonegale.grid(row=12, column=4)
boutoneffacer.grid(row=13, column=3)


bouton_historique = Button(fenetre, text="Historique", width=8, command=afficher_historique, bg="red")
bouton_historique.grid(row=13, column=4)

fenetre.mainloop()
