from tkinter import *
from sympy import sympify, N

y = ""

def bouton_clique(valeur):
    global y
    reponse.insert(END, str(valeur))
    y += str(valeur)

def bout1():
    bouton_clique(1)

def bout2():
    bouton_clique(2)

def bout3():
    bouton_clique(3)

def bout4():
    bouton_clique(4)

def bout5():
    bouton_clique(5)

def bout6():
    bouton_clique(6)

def bout7():
    bouton_clique(7)

def bout8():
    bouton_clique(8)

def bout9():
    bouton_clique(9)

def bout0():
    bouton_clique(0)

def boutplus():
    bouton_clique("+")

def boutmoins():
    bouton_clique("-")

def boutfois():
    bouton_clique("*")

def boutdiv():
    bouton_clique("/")

def boutpoint():
    bouton_clique(".")

def pargauche():
    bouton_clique("(")

def pardroite():
    bouton_clique(")")

def resultat():
    global y
    if y:
        try:
            expression = sympify(y)
            result = round(float(N(expression)), 8)
            reponse.insert(END, " = " + str(result) + '\n')
        except (ValueError, SyntaxError, ZeroDivisionError) as e:
            reponse.delete("1.0", END)
            reponse.insert(END, "Erreur: " + str(e) + '\n')
        y = ""

def gerer_erreur(exception):
    if isinstance(exception, (ValueError, SyntaxError)):
        return "Erreur: Expression mathématique invalide"
    elif isinstance(exception, ZeroDivisionError):
        return "Erreur: Division par zéro"
    else:
        return "Erreur inattendue: " + str(exception)

def effacer():
    global y
    reponse.delete("1.0", END)
    y = ""

fenetre = Tk()
fenetre.geometry("300x500")
fenetre.title("Calculatrice")

reponse = Text(fenetre)
reponse.grid(row=3, column=1, columnspan=6)
reponse.config(height=10, width=30, font=15)

# Création des boutons
bouton1 = Button(fenetre, text='1', width=5, font=15, command=bout1)
bouton2 = Button(fenetre, text='2', width=5, font=15, command=bout2)
bouton3 = Button(fenetre, text='3', width=5, font=15, command=bout3)
bouton4 = Button(fenetre, text='4', width=5, font=15, command=bout4)
bouton5 = Button(fenetre, text='5', width=5, font=15, command=bout5)
bouton6 = Button(fenetre, text='6', width=5, font=15, command=bout6)
bouton7 = Button(fenetre, text='7', width=5, font=15, command=bout7)
bouton8 = Button(fenetre, text='8', width=5, font=15, command=bout8)
bouton9 = Button(fenetre, text='9', width=5, font=15, command=bout9)
bouton0 = Button(fenetre, text='0', width=5, font=15, command=bout0)
boutonpoint = Button(fenetre, text=',', width=5, command=boutpoint, bg="red")
boutonplus = Button(fenetre, text='+', width=4, command=boutplus, bg="red")
boutonmoins = Button(fenetre, text='-', width=4, command=boutmoins, bg="red")
boutonfois = Button(fenetre, text='x', width=4, command=boutfois, bg="red")
boutondiv = Button(fenetre, text='/', width=4, command=boutdiv, bg="red")
boutonpargauche = Button(fenetre, text='(', width=5, command=pargauche, bg="red")
boutonpardroite = Button(fenetre, text=')', width=5, command=pardroite, bg="red")
boutonegale = Button(fenetre, text='=', width=6, command=resultat, bg="red")
boutoneffacer = Button(fenetre, text="supr", width=4, command=effacer, bg="red")

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

fenetre.mainloop()
