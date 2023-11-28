from tkinter import*
 
def b_action():
    print("Vous avez cliqué sur le bouton !")
    
maFenetre = Tk()
maFenetre.geometry("400x200")
 
#Création d'un bouton de commande
b = Button(maFenetre , text = "bouton avec action" , command = b_action)
 
# Placer le bouton sur la fenêtre
b.pack()
 
maFenetre.mainloop()
 
# affiche au click : Vous avez cliqué sur le bouton !