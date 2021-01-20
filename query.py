import mysql.connector
 
class Query:
    def __init__(self):
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='root', port = 3306, db='breizhibus')
        self.curseur = self.mydb.cursor()

    def get_all_lignes(self):
        self.curseur.execute("SELECT nom FROM lignes")
        return self.curseur.fetchall()

    def get_arrets_for_ligne(self, couleur_ligne):
        self.curseur.execute("SELECT nom FROM arrets INNER JOIN arrets_lignes ON arrets.id_arrets = arrets_lignes.id_arrets  WHERE id_lignes IN (SELECT id_lignes FROM lignes WHERE nom=%s)"%(couleur_ligne))
        return self.curseur.fetchall()

    def get_bus_for_ligne(self, couleur_ligne):
        self.curseur.execute("SELECT id_lignes FROM lignes WHERE nom= %s" %(couleur_ligne))
        return self.curseur.fetchone()

    def add_ligne():
        self.curseur.execute("INSERT INTO bus(numero, id_lignes) VALUES (%s, %s)" %(id_ligne))
        self.mydb.commit()
             
    def get_all_bus(self, couleur_ligne):
        requete = "SELECT numero FROM bus b JOIN lignes li ON b.id_lignes=li.id_lignes WHERE nom = %s"
        param = (couleur_ligne, )
        self.curseur.execute(requete, param)
        reponse = self.curseur.fetchall()
        return reponse

    def add_bus(self, num_bus, immat, places, id_ligne):
        requete = "INSERT INTO bus(numero, immatriculation, nombre_place, id_lignes) VALUES (%s, %s, %s, %s)"
        param = ( num_bus, immat, places, id_ligne, )
        self.curseur.execute(requete, param)
        self.mydb.commit()
        

    def del_bus(self, id_bus):
        requete = "DELETE FROM `bus` WHERE `id_bus`=%s"
        param = (id_bus, )
        self.curseur.execute(requete, param)
        self.mydb.commit()
       

    def get_id_num(self):
        requete = "SELECT id_bus, numero FROM bus"
        self.curseur.execute(requete, )
        reponse = self.curseur.fetchall()
        return reponse
    
# Query().del_bus("BB09")