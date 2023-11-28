from tkinter import *

def bout1():
    reponse.insert(END, "1")
    global y
    y = y + '1'

def bout2():
    reponse.insert(END, "2")
    global y
    y = y + '2'

def bout3():
    reponse.insert(END, "3")
    global y
    y = y + '3'

def bout4():
    reponse.insert(END, "4")
    global y
    y = y + '4'

def bout5():
    reponse.insert(END, "5")
    global y
    y = y + '5'

def bout6():
    reponse.insert(END, "6")
    global y
    y = y + '6'

def bout7():
    reponse.insert(END, "7")
    global y
    y = y + '7'

def bout8():
    reponse.insert(END, "8")
    global y
    y = y + '8'

def bout9():
    reponse.insert(END, "9")
    global y
    y = y + '9'

def bout0():
    reponse.insert(END, "0")
    global y
    y = y + '0'

def boutplus():
    reponse.insert(END, "+")
    global y
    y = y + "+"

def boutmoins():
    reponse.insert(END, "-")
    global y
    y = y + "-"

def boutfois():
    reponse.insert(END, "*")
    global y
    y = y + "*"

def boutdiv():
    reponse.insert(END, "/")
    global y
    y = y + "/"

def boutpoint():
    reponse.insert(END, ".")
    global y
    y = y + "."

def pargauche():
    reponse.insert(END, "(")
    global y
    y = y + '('

def pardroite():
    reponse.insert(END, ")")
    global y
    y = y + ')'

def resultat():
    reponse.insert(END, " = ")
    global y
    x = round(eval(y), 8)
    reponse.insert(END, str(x) + '\n')
    y = str()

def effacer():
    global y
    reponse.delete("1.0", END)

fenetre = Tk()
fenetre.geometry("600x600")
fenetre.title("Calculatrice programmeur")

reponse = Text(fenetre)  # Utilisez Text à la place de text
reponse.grid(row=3, column=1, columnspan=6)
reponse.config(height=10, width=30, font=15)

bout1 = Button(fenetre, text='1', width=5, font=15, command=bout1).grid(row=9, column=1)
bout2 = Button(fenetre, text='2', width=5, font=15, command=bout2).grid(row=9, column=2)
bout3 = Button(fenetre, text='3', width=5, font=15, command=bout3).grid(row=9, column=3)
bout4 = Button(fenetre, text='4', width=5, font=15, command=bout4).grid(row=7, column=1)
bout5 = Button(fenetre, text='5', width=5, font=15, command=bout5).grid(row=7, column=2)
bout6 = Button(fenetre, text='6', width=5, font=15, command=bout6).grid(row=7, column=3)
bout7 = Button(fenetre, text='7', width=5, font=15, command=bout7).grid(row=5, column=1)
bout8 = Button(fenetre, text='8', width=5, font=15, command=bout8).grid(row=5, column=2)
bout9 = Button(fenetre, text='9', width=5, font=15, command=bout9).grid(row=5, column=3)
bout0 = Button(fenetre, text='0', width=5, font=15, command=bout0).grid(row=11, column=1)
boutpoint = Button(fenetre, text=',', width=5, command=boutpoint).grid(row=11, column=3)
boutplus = Button(fenetre, text='+', width=4, command=boutplus).grid(row=5, column=4)
boutmoins = Button(fenetre, text='-', width=4, command=boutmoins).grid(row=7, column=4)
boutfois = Button(fenetre, text='x', width=4, command=boutfois).grid(row=9, column=4)
boutdiv = Button(fenetre, text='/', width=4, command=boutdiv).grid(row=11, column=4)
pargauche = Button(fenetre, text='(', width=5, command=pargauche).grid(row=13, column=1)
pardroite = Button(fenetre, text=')', width=5, command=pardroite).grid(row=13, column=2)
boutegale = Button(fenetre, text='=', width=4).grid(row=12, column=4)

fenetre.mainloop()