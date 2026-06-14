#--------------------------------
# Importation des bibliothèques et connexion à MySQL
#--------------------------------

import pymysql
import csv
import pandas as pd
import calendar
import matplotlib.pyplot as plt


db = pymysql.connect(host="146.59.198.88",
                     port=3300,
                     user="ferreira",
                     password="Aferreira26",
                     db="ferreira")

cursor = db.cursor()

#-----------------------------------------------
# Vide les tables de données SQL
#----------------------------------------------
cursor.execute("TRUNCATE TABLE Proprietaires")
cursor.execute("TRUNCATE TABLE Chiens")
cursor.execute("TRUNCATE TABLE Baladeurs")
cursor.execute("TRUNCATE TABLE Activites_Effectuees")
cursor.execute("TRUNCATE TABLE Activites_enregistrees")
cursor.execute("TRUNCATE TABLE Activites_reservees")
db.commit()


#--------------------------------
# Importation des données déjà créés
#--------------------------------

# Propriétaires

query = """CREATE TABLE IF NOT EXISTS Proprietaires (
                Id_Proprietaire INT AUTO_INCREMENT,
                nom VARCHAR(50),
                prenom VARCHAR(50),
                telephone VARCHAR(15),
                mail VARCHAR(100),
                mot_de_passe VARCHAR(50),
                PRIMARY KEY(Id_Proprietaire))"""

cursor.execute(query)
db.commit() 

proprietaires = pd.read_csv('proprietaires.csv',encoding="utf-8-sig",delimiter=",", header=0, names=["Id_Proprietaire","nom","prenom","telephone","mail","mot_de_passe"])

# Insertion ligne par ligne
for index, row in proprietaires.iterrows():
    query = "INSERT INTO Proprietaires (Id_Proprietaire,nom,prenom,telephone,mail,mot_de_passe) VALUES (%s, %s,%s, %s,%s, %s)"
    valeurs = (row["Id_Proprietaire"], row["nom"], row["prenom"],row["telephone"], row["mail"],row["mot_de_passe"])  
    cursor.execute(query, valeurs)
    
db.commit()

# Chiens

query = """CREATE TABLE IF NOT EXISTS Chiens (
                Id_Chien INT AUTO_INCREMENT,
                nom_chien VARCHAR(50),
                race_chien VARCHAR(50),
                temperament VARCHAR(50),
                Id_Proprietaire INT,
                PRIMARY KEY(Id_Chien))"""

cursor.execute(query)
db.commit() 

chiens = pd.read_csv('chiens.csv',encoding="utf-8-sig",delimiter=",", header=0, names=["Id_Chien","nom_chien","race_chien","temperament","Id_Proprietaire"])
print(proprietaires.columns)

for index, row in chiens.iterrows():
    query = "INSERT INTO Chiens (Id_Chien,nom_chien,race_chien,temperament,Id_Proprietaire) VALUES (%s,%s, %s,%s, %s)"
    valeurs = (row["Id_Chien"], row["nom_chien"], row["race_chien"],row["temperament"], row["Id_Proprietaire"])  
    cursor.execute(query, valeurs)
    
db.commit()

# Baladeurs

query = """CREATE TABLE IF NOT EXISTS Baladeurs (
                Id_Baladeur INT AUTO_INCREMENT,
                nom VARCHAR(50),
                prenom VARCHAR(50),
                telephone VARCHAR(15),
                mail VARCHAR(100),
                mot_de_passe VARCHAR(50),
                PRIMARY KEY(Id_Baladeur))"""

cursor.execute(query)
db.commit() 

baladeurs = pd.read_csv('baladeurs.csv',encoding="utf-8-sig",delimiter=",", header=0, names=["Id_Baladeur","nom","prenom","telephone","mail","mot_de_passe"])

for index, row in baladeurs.iterrows():
    query = "INSERT INTO Baladeurs (Id_Baladeur,nom,prenom,telephone,mail,mot_de_passe) VALUES (%s, %s,%s, %s,%s, %s)"
    valeurs = (row["Id_Baladeur"], row["nom"], row["prenom"],row["telephone"], row["mail"],row["mot_de_passe"])  
    cursor.execute(query, valeurs)
    
db.commit()

# Activités déjà éffectuées

query = """CREATE TABLE IF NOT EXISTS Activites_Effectuees (
                Id_Activite INT AUTO_INCREMENT,
                Id_Baladeur INT,
                activite VARCHAR(30),
                jour INT,
                mois INT,
                annee INT,
                moment VARCHAR(20),
                nb_chiens INT,
                tarif FLOAT,
                PRIMARY KEY(Id_Activite))"""

cursor.execute(query)
db.commit() 


activites = pd.read_csv('activites_effectuees.csv', encoding="utf-8-sig", delimiter=",", header=0, names=["Id_Baladeur", "activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"])

for index, row in activites.iterrows():
    query = """INSERT INTO Activites_Effectuees (Id_Baladeur, activite, jour, mois, annee, moment, nb_chiens, tarif) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    valeurs = (row["Id_Baladeur"], row["activite"], row["jour"], row["mois"], row["annee"], row["moment"], row["nb_chiens"], row["tarif"])  
    cursor.execute(query, valeurs)
    
db.commit()

# Enregistrement des activités disponibles

query = """CREATE TABLE IF NOT EXISTS Activites_enregistrees (
                Id_Enregistrement INT AUTO_INCREMENT,
                Id_Baladeur INT,
                activite VARCHAR(30),
                jour INT,
                mois INT,
                annee INT,
                moment VARCHAR(20),
                nb_chiens INT,
                tarif FLOAT,
                PRIMARY KEY(Id_Enregistrement))"""

cursor.execute(query)
db.commit() 

enregistrements = pd.read_csv('activites_enregistrees.csv', encoding="utf-8-sig", delimiter=",", header=0, names=["Id_Baladeur", "activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"])

for index, row in enregistrements.iterrows():
    query = """INSERT INTO Activites_enregistrees (Id_Baladeur, activite, jour, mois, annee, moment, nb_chiens, tarif) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    valeurs = (row["Id_Baladeur"], row["activite"], row["jour"], row["mois"], row["annee"], row["moment"], row["nb_chiens"], row["tarif"])
    cursor.execute(query, valeurs)
    
db.commit()

# Reservations

query = """CREATE TABLE IF NOT EXISTS Activites_reservees (
                Id_Reservation INT AUTO_INCREMENT,
                Id_Baladeur INT,
                activite VARCHAR(30),
                jour INT,
                mois INT,
                annee INT,
                moment VARCHAR(20),
                tarif FLOAT,
                Id_chien INT,
                PRIMARY KEY(Id_Reservation))"""

cursor.execute(query)
db.commit() 

reservations = pd.read_csv('activites_reservees.csv', encoding="utf-8-sig", delimiter=",", header=0, names=["Id_Baladeur", "activite", "jour", "mois", "annee", "moment", "tarif", "Id_chien"])

for index, row in reservations.iterrows():
    query = """INSERT INTO Activites_reservees(Id_Baladeur, activite, jour, mois, annee, moment, tarif, Id_chien) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    valeurs = (row["Id_Baladeur"], row["activite"], row["jour"], row["mois"], row["annee"], row["moment"], row["tarif"], row["Id_chien"])
    cursor.execute(query, valeurs)
    
db.commit()


#--------------------------------
# Code du Menu et des enregistrements
#--------------------------------

def main():

    while True:
        print("Menu: \t")
        print("1. Nouveau Compte")
        print("2. Accès à mon compte")
        print("3. Quitter")
        print("")

        choix_main = " "

        while choix_main not in ['1', '2', '3']:
            choix_main = input("Veuillez entrer votre choix (1, 2 ou 3) : ")

        if choix_main == '1':
            print("")
            nouveau_compte()
        elif choix_main == '2':
            print("")
            acces_compte()
        elif choix_main == '3':
            print("Au revoir")
            print("")
            break

def nouveau_compte():
    print("Création d'un nouveau compte")
    print("Faites votre choix :")
    print("1. Je suis propriétaire et souhaite réserver une balade pour mon ou mes chiens")
    print("2. Je suis baladeur et souhaite proposer des balades à des proprétaires de chiens")
    print("3. Revenir en arrière")
    print("")

    choix_creation = ' '

    while choix_creation not in ['1', '2', '3']:
        choix_creation = input("Entrez votre choix (1, 2 ou 3) : ")

    if choix_creation == '1':
        creation_prop()
    elif choix_creation == '2':
        creation_baladeur()
    else:
        return


def acces_compte():
    print("1. Je suis propriétaire")
    print("2. Je suis baladeur")
    print("3. Revenir en arrière")
    print("")

    choix_acces = ' '

    while choix_acces not in ['1', '2', '3']:
        choix_acces = input("Entrez votre choix (1, 2 ou 3) : ")

    if choix_acces == '1':
        connexion_prop()
    elif choix_acces == '2':
        connexion_baladeur()
    else:
        return  


def connexion_prop():
    print("\n--- CONNEXION PROPRIÉTAIRE ---")
    test = True

    while test : 
        mail_cp = input("mail :")
        mdp_cp = input("Mot de passe :")

        query = """
        SELECT Id_Proprietaire, nom, prenom
        FROM Proprietaires
        WHERE mail = %s AND mot_de_passe = %s
        """

        cursor.execute(query, (mail_cp, mdp_cp))

        resultat = cursor.fetchone()

        if resultat:
            print("Connexion réussie")
            test = False
        else:
            print("Mail ou mot de passe incorrect")
    
    id_proprietaire = resultat[0]
    prenom = resultat[2]
    print(" ")
    espace_prop(id_proprietaire, prenom)
    
def espace_prop(id_proprietaire, prenom):
    print("\n--- PROFIL PROPRIETAIRE ---")
    choix_cp = ' '

    while choix_cp not in ['1', '2', '3']:
        print(f"Bonjour {prenom}")
        print("Que voulez-vous faire ?")
        print("1. Enregistrer un chien")
        print("2. Rechercher une balade pour mon ou mes chiens")
        print("3. Me déconnecter")

        choix_cp = input("")

    if choix_cp == '1':
        creation_chien(id_proprietaire, prenom)
    elif choix_cp == '2':
        print(" ")
        reservation(id_proprietaire, prenom)
    else:
        main()


def connexion_baladeur():
    test = True

    while test : 
        mail_cb = input("mail :")
        mdp_cb = input("Mot de passe :")

        query = """
        SELECT Id_Baladeur, nom, prenom
        FROM Baladeurs
        WHERE mail = %s AND mot_de_passe = %s
        """

        cursor.execute(query, (mail_cb, mdp_cb))

        resultat_b = cursor.fetchone()

        if resultat_b:
            print("Connexion réussie")
            test = False
        else:
            print("Mail ou mot de passe incorrect")
            
    id_baladeur = resultat_b[0]
    prenom = resultat_b[2]
    print(" ")
    espace_baladeur(id_baladeur, prenom)
    
def espace_baladeur(id_baladeur, prenom):
    print("\n--- PROFIL BALADEUR ---")
    choix_cb = ' '

    while choix_cb not in ['1', '2', '3', '4']:
        print(f"Bonjour {prenom}")
        print("Que voulez-vous faire ?")
        print("1. Proposer une balade")
        print("2. Exporter mes activités sous .csv")
        print("3. Visualiser l'évolution de mes activités")
        print("4. Me déconnecter")

        choix_cb = input("")

    if choix_cb == '1':
        enregistrement_nv_activite(id_baladeur,prenom)
    elif choix_cb == '2':
        # Fonction d'export des act
        export_act(id_baladeur, prenom)
    elif choix_cb == '3':
        # Fonction visulaisation évolution act
        graphe_evol(id_baladeur, prenom)
    else:
        return

#--------------------------------
# Enregistrement d'un nouveau propriétaire
#--------------------------------

def creation_prop():
    print("\n--- ENREGISTREMENT DE VOTRE COMPTE ---")
    nom = input("Quel est votre nom de famille ?")
    prenom = input("Quel est votre prénom ?")
    telephone = input("Quel est votre numero de téléphone ?")
    mail = input("Quel est votre mail ?")
    mdp = input("Quel mot de passe voulez-vous enregistrer ?")
    query = "INSERT INTO Proprietaires (nom, prenom, telephone, mail, mot_de_passe) VALUES (%s, %s, %s, %s, %s)"
    valeurs = (nom, prenom, telephone, mail, mdp)
    cursor.execute(query, valeurs)
    db.commit()
    id_nouveau_prop = cursor.lastrowid
    print(
        f"\nFélicitations {prenom}, votre compte propriétaire a bien été créé ! (Votre ID est le {id_nouveau_prop})")

    print("\nVoulez-vous enregistrer un chien ?")
    print("1 : Oui")
    print("2 : Non")
    choix = input("Votre choix (1 ou 2) : ")
    if choix == "1":
        print("")
        creation_chien(id_nouveau_prop)
    else:
        print("")
        print("Retour à l'espace client ... ")
        espace_prop(id_nouveau_prop, prenom)


# --------------------------------
# Enregistrement d'un nouveau chien
# --------------------------------

def creation_chien(id_proprietaire, prenom):
    print("\n--- ENREGISTREMENT DE VOTRE CHIEN ---")
    nom_chien = input("Quel est le nom du chien ? ")
    race_chien = input("Quel est la race du chien ? ")
    print("Quel est le tempérament du chien ? ")
    print("1: Sociable")
    print("2: Peureux")
    print("3: Calme")
    print("4: Joueur")
    print("5: Agressif")
    choix = input("Votre choix (1, 2, 3, 4 ou 5) : ")
    while choix not in ['1', '2', '3', '4', '5']:
        choix = input("Votre choix (1, 2, 3, 4 ou 5) : ")
    if choix == "1":
        temperament = "Sociable"
    elif choix == "2":
        temperament = "Peureux"
    elif choix == "3":
        temperament = "Calme"
    elif choix == "4":
        temperament = "Joueur"
    else :
        temperament = "Agressif"
    query = "INSERT INTO Chiens (nom_chien, race_chien, temperament, Id_Proprietaire) VALUES (%s, %s, %s, %s)"
    valeurs = (nom_chien, race_chien, temperament, id_proprietaire)
    cursor.execute(query, valeurs)
    db.commit()
    print(f"Le chien {nom_chien} a bien été associé à votre compte !")
    
    print("\nVoulez-vous enregistrer un autre chien ?")
    print("1 : Oui")
    print("2 : Non")
    choix = input("Votre choix (1 ou 2) : ")
    if choix == "1":
        creation_chien(id_proprietaire, prenom)
    else:
        print("Retour à l'espace client ... ")
        print("")
        espace_prop(id_proprietaire, prenom)


#--------------------------------
# Enregistrement d'un nouveau baladeur
#--------------------------------

def creation_baladeur():
    print("\n--- ENREGISTREMENT DE VOTRE COMPTE ---")
    nom = input("Quel est votre nom de famille ?")
    prenom = input("Quel est votre prénom ?")
    telephone = input("Quel est votre numero de téléphone ?")
    mail = input("Quel est votre mail ?")
    mdp = input("Quel mot de passe voulez-vous enregistrer ?")
    query = "INSERT INTO Baladeurs (nom, prenom, telephone, mail, mot_de_passe) VALUES (%s, %s, %s, %s, %s)"
    valeurs = (nom, prenom, telephone, mail, mdp)
    cursor.execute(query, valeurs)
    db.commit() 
    id_baladeur = cursor.lastrowid
    print(f"\nFélicitations {prenom}, votre compte propriétaire a bien été créé !")
    print("Retour à votre profil ")
    espace_baladeur(id_baladeur, prenom)


#--------------------------------
# Enregistrement d'une nouvelle activité
#--------------------------------

def enregistrement_nv_activite(id_baladeur, prenom):
    print("\n--- ENREGISTREMENT D'UNE NOUVELLE ACTIVITE ---")
    print("Quel est le type d'activité ? ")
    print("1: Balade")
    print("2: Garde")
    activite = input("Votre choix (1 ou 2) : ")
    while activite not in ['1', '2']:
        activite = input("Votre choix (1 ou 2) : ")
    if activite == "1" :
        activite = "Balade"
    else:
        activite = "Garde"
    annee = input("Année (ex: 2026) : ")
    while not annee.isdigit() or int(annee) < 2026:
        annee = input("Veuillez entrer une année valide (>= 2026) : ")
    annee = int(annee)
    mois = input("Quel mois (1 à 12) : ")
    while not mois.isdigit() or int(mois) not in range(1, 13):
        mois = input("Veuillez entrer un mois valide (1 à 12) : ")
    mois = int(mois)
    nb_jours_max = calendar.monthrange(annee, mois)[1]     # Le deuxième élément [1] est le nombre maximum de jours dans ce mois précis.
    print(f"Quel jour ? (Pour ce mois, le choix doit être entre 1 et {nb_jours_max})")
    jour = input("Jour choisi : ")
    while not jour.isdigit() or int(jour) not in range(1, nb_jours_max + 1):
        print(f"Erreur. Pour le mois {mois}/{annee}, le jour doit être entre 1 et {nb_jours_max}.")
        jour = input("Jour choisi : ")
    jour = int(jour)
    print("A quel moment de la journée voulez-vous enregistrer cette activité ?")
    print("1: Matin")
    print("2: Après-midi")
    moment = input("Votre choix (1 ou 2) : ")
    while moment not in ['1', '2']:
        moment = input("Votre choix (1 ou 2) : ")
    if moment == "1" :
        moment = "Matin"
    else:
        moment = "Après-Midi"
    nb_chiens = input("Combien de chiens pouvez-vous prendre en charge ? : ")
    tarif = input("Quel est le tarif pour un chien (€) ?")
    query = "INSERT INTO Activites_enregistrees (id_baladeur, activite, jour, mois, annee, moment, nb_chiens, tarif) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valeurs = (id_baladeur, activite, jour, mois, annee, moment, nb_chiens, tarif)
    cursor.execute(query, valeurs)
    db.commit()
    print(f"\nActivité enregistrée avec succès pour le {jour}/{mois}/{annee} !")
    print("")
    print("\nVoulez-vous enregistrer une nouvelle activité?")
    print("1 : Oui")
    print("2 : Non")
    choix = input("Votre choix (1 ou 2) : ")
    while choix not in ['1', '2']:
        choix = input("Votre choix (1 ou 2) : ")
    if choix == "1":
        print("")
        enregistrement_nv_activite(id_baladeur,prenom)
    else:
        print("")
        print("Retour à l'espace client ... ")
        espace_baladeur(id_baladeur, prenom)

#--------------------------------
# Recherche d'activité + réservation
#--------------------------------

def reservation(id_proprietaire, prenom):
    print("\n--- RECHERCHE ET RÉSERVATION D'UNE BALADE ---")
    query_chiens = """
    SELECT Id_Chien, nom_chien, race_chien, temperament 
    FROM Chiens 
    WHERE Id_Proprietaire = %s
    """
    cursor.execute(query_chiens, (id_proprietaire,))
    mes_chiens = cursor.fetchall()
    if not mes_chiens:
        print("")
        print("[Attention] Vous n'avez pas encore enregistré de chien sur votre compte.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        espace_prop(id_proprietaire, prenom)
        return
    colonnes_chiens = ["Id_Chien", "Nom du chien", "Race", "Tempérament"]
    df_chiens = pd.DataFrame(mes_chiens, columns=colonnes_chiens)
    print("\n--- POUR QUEL CHIEN SOUHAITEZ-VOUS RÉSERVER ? ---")
    print(df_chiens.to_string(index=False))
    print("")
    choix_chien = input("Entrez l'Id_Chien qui participera à la balade : ")
    while not choix_chien.isdigit() or int(choix_chien) not in df_chiens['Id_Chien'].values:
        choix_chien = input("Id invalide. Veuillez entrer un Id_Chien présent dans la liste ci-dessus : ")    
    id_chien_selectionne = int(choix_chien)
    print("")
    print("Quel type d'activité recherchez-vous ?")
    print("1: Balade")
    print("2: Garde")
    activite= input("Votre choix (1 ou 2) : ")
    while activite not in ['1', '2']:
        activite = input("Votre choix (1 ou 2) : ")
    if activite == "1":
        activite = "Balade"
    else:
        activite = "Garde"
    annee = input("Année (ex: 2026) : ")
    while not annee.isdigit() or int(annee) < 2026:
        annee = input("Année valide (>= 2026) : ")
    mois = input("Mois (1 à 12) : ")
    while not mois.isdigit() or int(mois) not in range(1, 13):
        mois = input("Mois valide (1 à 12) : ")
    nb_jours_max = calendar.monthrange(int(annee), int(mois))[1]
    jour = input(f"Jour (1 à {nb_jours_max}) : ")
    while not jour.isdigit() or int(jour) not in range(1, nb_jours_max + 1):
        jour = input(f"Jour valide (1 à {nb_jours_max}) : ")
    print("À quel moment ? ")
    print("1: Matin")
    print("2: Après-midi")
    moment = input("Votre choix (1 ou 2) : ")
    while moment not in ['1', '2']:
        moment = input("Votre choix (1 ou 2) : ")
    if moment == "1":
        moment = "Matin"
    else:
        "Après-Midi"

    query_recherche = """SELECT 
        ae.Id_Enregistrement, 
        b.nom, 
        b.prenom, 
        ae.activite, 
        ae.jour, 
        ae.mois, 
        ae.annee, 
        ae.moment, 
        ae.nb_chiens, 
        ae.tarif,
        ae.Id_Baladeur
    FROM Activites_enregistrees ae
    INNER JOIN Baladeurs b ON ae.Id_Baladeur = b.Id_Baladeur
    WHERE ae.activite = %s AND ae.jour = %s AND ae.mois = %s AND ae.annee = %s AND ae.moment = %s AND ae.nb_chiens > 0
    """
    cursor.execute(query_recherche, (activite, int(jour), int(mois), int(annee), moment))
    resultats = cursor.fetchall()
    colonnes = colonnes = ["Id_Offre", "Nom Baladeur", "Prénom Baladeur", "Activité", "Jour", "Mois", "Année", "Moment", "Places Restantes", "Tarif", "Id_Baladeur"]
    if not resultats:
        print("")
        print("Désolé, aucune activité ne correspond à vos critères à cette date.")
        input("Appuyez sur Entrée pour revenir au menu...")
        espace_prop(id_proprietaire, prenom)
        return
    disponibilites = pd.DataFrame(resultats, columns=colonnes)
    print("")
    print("--- ACTIVITÉS DISPONIBLES ---")
    print(disponibilites.to_string(index=False))
    print("")
    choix_id = input("Entrez l'Id_Offre que vous souhaitez réserver (ou 'q' pour annuler) : ")
    if choix_id.lower() == 'q':
        espace_prop(id_proprietaire, prenom)
        return
    while not choix_id.isdigit() or int(choix_id) not in disponibilites['Id_Offre'].values:
        choix_id = input("Id invalide. Veuillez choisir un Id_Offre présent dans le tableau : ")
    id_offre_choisie = int(choix_id)
    ligne_choisie = disponibilites[disponibilites['Id_Offre'] == id_offre_choisie].iloc[0]
    query_reservation = """
    INSERT INTO Activites_reservees (Id_Baladeur, activite, jour, mois, annee, moment, tarif, Id_chien) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    reservation = (int(ligne_choisie['Id_Baladeur']), ligne_choisie['Activité'], int(ligne_choisie['Jour']), 
                   int(ligne_choisie['Mois']), int(ligne_choisie['Année']), ligne_choisie['Moment'], float(ligne_choisie['Tarif']), id_chien_selectionne)
    cursor.execute(query_reservation, reservation)
    places_dispo = int(ligne_choisie['Places Restantes']) - 1
    if places_dispo == 0:
        # Plus de places ? On supprime la ligne de la table des offres disponibles
        query_update = "DELETE FROM Activites_enregistrees WHERE Id_Enregistrement = %s"
        cursor.execute(query_update, (id_offre_choisie,))
        print("")
        print("Places épuisées pour cette offre, elle a été retirée des disponibilités.")
    else:
        query_update = "UPDATE Activites_enregistrees SET nb_chiens = %s WHERE Id_Enregistrement = %s"
        cursor.execute(query_update, (places_dispo, id_offre_choisie))
        print("")
        print(f"Réservation enregistrée ! Il reste {places_dispo} place(s) pour cette activité.")
    db.commit()
    print("")
    input("Appuyez sur Entrée pour revenir à votre espace...")
    espace_prop(id_proprietaire, prenom)
    





#--------------------------------
# Exporter les activités déjà faites + quantité argent gagnée
#--------------------------------
def export_act(id_baladeur, prenom):
    print("\n--- EXPORTATION DES ACTIVITES ---")
    query_exp = """
    SELECT * 
    FROM Activites_Effectuees 
    WHERE Id_Baladeur = %s
    """
    cursor.execute(query_exp, (id_baladeur, ))
    mes_act = cursor.fetchall()

    if not mes_act:
        print("")
        print("[Attention] Vous n'avez pas encore réalisé d'activité.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        espace_baladeur(id_baladeur, prenom)
        return
    colonnes_act = ["Id_Activite", "Id_Baladeur", "activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"]
    df_act = pd.DataFrame(mes_act, columns=colonnes_act)
    df_act = df_act[["activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"]]

    print(df_act)
    gain = (df_act["tarif"] * df_act["nb_chiens"]).sum()
    print(f"Vous avez gagné {gain} €")
    reponse = input("Voulez-vous exporter ce tableau au format .csv ? (Y/N)")
    reponse = reponse.upper()
    while reponse not in ["Y", "N"]:
        reponse = input("Voulez-vous exporter ce tableau ? (Y/N)")
    if reponse == "Y":
        df_act.to_csv("Mes_activités.csv", index=False, encoding="utf-8-sig")
        print(f"Le fichier 'Mes activités.csv' a été créé avec succès dans le dossier.")
    else:
        print("Retour à votre profil")
        espace_baladeur(id_baladeur, prenom)
        return



#--------------------------------
# Visualisation graphique de l'évolution des activités
#--------------------------------
def graphe_evol(id_baladeur, prenom):
    print("\n--- VISUALISATION GRAPHIQUE DE L'EVOLUTION DES ACTIVITES ---")
    query_evol = """
    SELECT * 
    FROM Activites_Effectuees 
    WHERE Id_Baladeur = %s
    """
    cursor.execute(query_evol, (id_baladeur, ))
    evol_act = cursor.fetchall()

    if not evol_act:
        print("")
        print("[Attention] Vous n'avez pas encore réalisé d'activité.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        espace_baladeur(id_baladeur, prenom)
        return
    colonnes_act = ["Id_Activite", "Id_Baladeur", "activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"]
    df_evol_act = pd.DataFrame(evol_act, columns=colonnes_act)
    df_evol_act = df_evol_act[["activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"]]

    df_evol_act["gain_act"] = df_evol_act["tarif"]*df_evol_act["nb_chiens"]

    df_evol_act["temps"] = df_evol_act['mois'].astype(str) + "_" + df_evol_act['annee'].astype(str)
    
    annees_dispo = sorted(df_evol_act["annee"].unique())

    print("\nQue voulez vous visualiser ?")
    print("1. Le nombre d'activité")
    print("2. Le nombre de chien pris en charge")
    print("3. Les gains perçus")
    print("4. les activités réalisées")
    print("5. Rien, je veux retourner sur mon profil")
    choix1 = input("Que choisissez-vous ? (1, 2, 3, 4 ou 5)")

    while choix1 not in ["1", "2", "3", "4", "5"]:
        choix1 = input("Que choisissez-vous ? (1, 2, 3, 4 ou 5)")

    if not choix1 == "5":
        print("\n Années disponibles")
        print(annees_dispo)
        choix2 = input("Quelle année voulez-vous observer parmi celle(s) disponible(s) ? ")

        while not choix2.isdigit() or int(choix2) not in annees_dispo:
            choix2 = input("Quelle année voulez-vous observer parmi celle(s) disponible(s) ? ")
    
        choix2 = int(choix2)

    if choix1 == "1":
        tab_temp = (
            df_evol_act.groupby("mois")
            .size()
            .reindex(range(1, 13), fill_value=0)
            .reset_index(name="nb_activites")
        )

        plt.bar(tab_temp["mois"], tab_temp["nb_activites"])
        plt.xlabel("Mois")
        plt.ylabel("Nombre d'activités réalisées")
        plt.title(f"Évolution du nombre d'activités réalisées en {choix2}")
        plt.xticks(range(1, 13), range(1, 13), rotation=45)
        plt.show()

        graphe_evol(id_baladeur, prenom)
        return
    elif choix1 == "2":
        tab_temp = (
            df_evol_act.groupby("mois")["nb_chiens"]
            .sum()
            .reindex(range(1, 13), fill_value=0)
            .reset_index()
        )

        plt.bar(tab_temp["mois"], tab_temp["nb_chiens"])
        plt.xlabel("Mois")
        plt.ylabel("Nombre de chiens pris en charge")
        plt.title(f"Évolution du nombre de chiens pris en charge en {choix2}")
        plt.xticks(range(1, 13), range(1, 13), rotation=45)
        plt.show()

        graphe_evol(id_baladeur, prenom)
        return
    elif choix1 == "3":
        tab_temp = (
            df_evol_act.groupby("mois")["gain_act"]
            .sum()
            .reindex(range(1, 13), fill_value=0)
            .reset_index()
        )

        plt.bar(tab_temp["mois"], tab_temp["gain_act"])
        plt.xlabel("Mois")
        plt.ylabel("Gain perçu (€)")
        plt.title(f"Évolution du gain perçu mensuel en {choix2}")
        plt.xticks(range(1, 13), range(1, 13), rotation=45)
        plt.show()

        graphe_evol(id_baladeur, prenom)
        return
    elif choix1 == "4":
        tab_temp = (
            df_evol_act.groupby(["mois", "activite"])
            .size()
            .unstack(fill_value=0)
            .reindex(range(1, 13), fill_value=0)
        )

        tab_temp.index = range(1, 13)

        tab_temp.plot(kind="bar", stacked=True)
        plt.xlabel("Mois")
        plt.ylabel("Nombre d'activités réalisées")
        plt.title(f"Répartition des activités réalisées en {choix2}")
        plt.xticks(rotation=45)
        plt.legend(title="Activité")
        plt.tight_layout()
        plt.show()

        graphe_evol(id_baladeur, prenom)
        return
    else:
        print("Retour sur le profil ...")
        espace_baladeur(id_baladeur, prenom)
        return


main()
