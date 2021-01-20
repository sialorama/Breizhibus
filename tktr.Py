import tkinter as tk
from tkinter import ttk
from query import Query

class App:

    def clear_frame(self):
        for widget in self.frame_resultat.winfo_children():
            widget.destroy()

    def afficher_lignes(self):
        resultat = Query().get_all_lignes()
        self.clear_frame()
        for ligne in resultat:
            ligne_label = tk.Label(self.frame_resultat, text = ligne, font = ("helvetica", "10"))
            ligne_label.pack()
    
    def afficher_bus(self):
        couleur_ligne = self.var.get()
        resultat = Query().get_all_bus(couleur_ligne)
        self.clear_frame()
        for bus in resultat:
            ligne_label = tk.Label(self.frame_resultat, text = bus[0], font = ("helvetica", "10"))
            ligne_label.pack()
    
    def add_bus(self):
        resultat = Query().add_bus()
        for bus in resultat:
            ligne_label = tk.Label(self.racine, text = bus[0], font = ("helvetica", "10"))
            ligne_label.pack()
        
    def ajout_bus(self):
        num_bus = self.champ_num.get()
        immat = self.champ_immat.get()
        places = self.champ_places.get()
        id_ligne = self.valeur_champ_txt_id.get()
        Query().add_bus(num_bus, immat, places, id_ligne)

    def supprBus(self, listeId):
        print("index: ", self.listeSuppression.current())
        print("id à supprimer: ", listeId[self.listeSuppression.current()])
        Query().del_bus(listeId[self.listeSuppression.current()])

    def run(self):
        self.racine = tk.Tk()
        self.racine.title("Breizhibus")
        self.racine.geometry("1920x1080")
        self.racine.minsize(720, 480)
    #lOGO
        # self.image = Tk.PhotoImage(file='C:/Users/Sialorama/Google Drive/BRIEFS/BREISHIBUS')
        # self.texte = self.Label(self.racine, image=image)
        # self.text.pack()

        self.frame_menu = tk.Frame(self.racine,)
        self.frame_menu.pack()

        self.frame_boutons = tk.Frame(self.racine)
        self.frame_boutons.pack(pady=25)

        self.frame_BR = tk.Frame(self.racine)
        self.frame_BR.pack(pady=25)

        self.frame_ajout = tk.Frame(self.racine)
        self.frame_ajout.pack(pady=25)

        self.frame_resultat = tk.Frame(self.racine)
        self.frame_resultat.pack(pady=50)
        
        self.lignes_frame = tk.LabelFrame(self.frame_menu, text='Liste Bus')
        self.lignes_frame.pack()

        self.button_afficher = tk.Button(self.frame_boutons, text="Afficher toutes les lignes", command=self.afficher_lignes)
        self.button_afficher.grid(row=0, column=0, padx=5, ipadx=12)

        self.button_afficher1 = tk.Button(self.frame_boutons, text="Afficher tous les bus", command=self.afficher_bus)
        self.button_afficher1.grid(row=0, column=1, padx=5, ipadx=12)

        #Ajouter un bus
        self.valeur_champ_txt_num = tk.StringVar()
        self.label1 = tk.Label (self.frame_ajout, text="Entrez le numéro du bus :").pack()
        self.champ_num = tk.Entry(self.frame_ajout, textvariable=self.valeur_champ_txt_num)
        self.champ_num.pack()

        self.valeur_champ_txt_immat = tk.StringVar()
        self.label2 = tk.Label (self.frame_ajout, text="Entrez l'immatriculation :").pack()
        self.champ_immat = tk.Entry(self.frame_ajout, textvariable=self.valeur_champ_txt_immat)
        self.champ_immat.pack()

        self.valeur_champ_txt_place = tk.IntVar()
        self.label3 = tk.Label (self.frame_ajout, text="Entrez le nombre de place :").pack()
        self.champ_places = tk.Entry(self.frame_ajout, textvariable=self.valeur_champ_txt_place)
        self.champ_places.pack()

        self.valeur_champ_txt_id = tk.IntVar()
        self.label4 = tk.Label (self.frame_ajout, text="Choisissez une ligne :").pack()

        self.bt_ligne_vert = tk.Radiobutton(self.frame_ajout, text="Vert", variable=self.valeur_champ_txt_id, value=2)
        self.bt_ligne_vert.pack()

        self.bt_ligne_rouge = tk.Radiobutton(self.frame_ajout, text="Rouge", variable=self.valeur_champ_txt_id, value=1)
        self.bt_ligne_rouge.pack()

        self.bt_ligne_bleu = tk.Radiobutton(self.frame_ajout, text="Bleu", variable=self.valeur_champ_txt_id, value=3)
        self.bt_ligne_bleu.pack()

        self.bt_ligne_noir = tk.Radiobutton(self.frame_ajout, text="Noir", variable=self.valeur_champ_txt_id, value=4)
        self.bt_ligne_noir.pack()
        
        self.button_ajouter = tk.Button(self.frame_ajout, text="Ajouter un bus", command=self.ajout_bus)
        self.button_ajouter.pack()

        #Quitter tktr
        self.button_quit = tk.Button(self.frame_boutons, text="Quitter", command=self.racine.destroy)
        self.button_quit.grid(row=0, column=3, padx=5, ipadx=12)


        self.var = tk.StringVar(value="Rouge")
 
        self.R1 = tk.Radiobutton(self.frame_BR, text="Rouge", variable=self.var, value="Rouge")
        self.R1.pack()
        
        self.R2 = tk.Radiobutton(self.frame_BR, text="Vert", variable=self.var, value="Vert")
        self.R2.pack()
        #   self.R3 = tk.Radiobutton(self.frame_BR, text="Bleu", variable=self.var, value="Bleu", command=affiche_bus)
        self.R3 = tk.Radiobutton(self.frame_BR, text="Bleu", variable=self.var, value="Bleu")
        self.R3.pack()

        self.R4 = tk.Radiobutton(self.frame_BR, text="Noir", variable=self.var, value="Noir")
        self.R4.pack()

        # Mise en place de la combobox pour supprimer un bus
        data = Query().get_id_num()
        listeBus, listeId = [], []
        for row in data:
            listeId.append(row[0])
            listeBus.append(row[1])
        
        # Label de suppression, liste déroulante et Boutton de suppression
        self.labelSuppression = tk.Label(self.racine, text= "Veuillez choisir la ligne à supprimer: ")
        self.labelSuppression.pack()
        
        self.listeSuppression = ttk.Combobox(self.racine, values=listeBus, state="readonly")
        self.listeSuppression.pack()
        self.listeSuppression.current(0)

        self.buttonSuppression = tk.Button(self.racine, text = "Supprimer", command= lambda: self.supprBus(listeId))
        self.buttonSuppression.pack()
        #Modifier un bus
        # self.buttonModifier = tk.Button(self.racine, text = "Supprimer", command= lambda: self.ModifBus(listeId))
        # self.buttonModifier.pack()

        self.racine.mainloop() # Lancement de la boucle principale

app = App()
app.run()