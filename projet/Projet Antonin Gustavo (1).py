#--------------------------------
# Importation des bibliothèques et connexion à MySQL
#--------------------------------

import pymysql
import pandas as pd
import calendar
import matplotlib.pyplot as plt
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import seaborn as sns


db = pymysql.connect(host="146.59.198.88",
                     port=3300,
                     user="ferreira",
                     password="Aferreira26",
                     db="ferreira")

cursor = db.cursor()

#-----------------------------------------------
# Vide les tables de données SQL
#----------------------------------------------
def vide_table():
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
def importation_donnees():

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

#---------------------------------------
# Fonction prélancement et préparation des données
#---------------------------------------
def prelancement():
    # Vider les tables existantes pour éviter tout conflit ?
    choix_vide = input("Voulez-vous vider les tables de données : Proprietaires, Chiens, Baladeurs, Activites_Effectuees, Activites_enregistrees et Activites_reservees ? (Y/N)").lower()

    while choix_vide not in ["y", "n"]:
        choix_vide = input("Voulez-vous vider les tables de données : Proprietaires, Chiens, Baladeurs, Activites_Effectuees, Activites_enregistrees et Activites_reservees ? (Y/N)").lower()

    if choix_vide == "y":
        vide_table()
        
        # Importer les données des fichiers csv si ce n'est pas déjà fait et si les tables sont vides
        choix_import = input("Voulez-vous importer les données depuis les fichiers csv ? (Y/N)").lower()

        while choix_import not in ["y", "n"]:
            choix_import = input("Voulez-vous importer les données depuis les fichiers csv ? (Y/N)").lower()

        if choix_import == "y":
            importation_donnees()
    main()

#--------------------------------
# Code du Menu et des enregistrements
#--------------------------------

def main():
    '''
    Fonction principale, elle permet de lancer le nettoyage des tables et leur remplissage et 
    elle affiche le menu et redirige vers les autres fonctions

    Paramètre : aucun

    Retourne : Rien
    '''

    # Boucle principale du programme : reste active jusqu'à ce que l'utilisateur choisisse de quitter (break).
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
    '''
    Interface permettant de créer un compte ou de revenir en arrière

    Aucun paramètre ni retour, cette fonction redirige vers d'autres fonctions
    '''
    print("Création d'un nouveau compte")
    print("Faites votre choix :")
    print("1. Je suis propriétaire et souhaite réserver une balade pour mon ou mes chiens")
    print("2. Je suis baladeur et souhaite proposer des balades à des proprétaires de chiens")
    print("3. Revenir en arrière")
    print("")

    choix_creation = ' '

    # Vérifie la validité de la réponse sans lever une erreur à chaque fois
    while choix_creation not in ['1', '2', '3']:
        choix_creation = input("Entrez votre choix (1, 2 ou 3) : ")

    if choix_creation == '1':
        creation_prop()
    elif choix_creation == '2':
        creation_baladeur()
    else:
        # retourne rien et permet ainsi de retourner à la fonction d'appel main()
        return


def acces_compte():
    '''
    Interface permettant d'acceder à un compte déjà existant

    Aucun paramètre ni retour, la fonction redirige vers d'autres fonctions
    '''
    print("1. Je suis propriétaire")
    print("2. Je suis baladeur")
    print("3. Revenir en arrière")
    print("")

    choix_acces = ' '

    # Vérifie la validité de la réponse sans lever une erreur à chaque fois
    while choix_acces not in ['1', '2', '3']:
        choix_acces = input("Entrez votre choix (1, 2 ou 3) : ")

    if choix_acces == '1':
        connexion_prop()
    elif choix_acces == '2':
        connexion_baladeur()
    else:
        # retourne rien et permet ainsi de retourner à la fonction d'appel main()
        return  


def connexion_prop():
    '''
    Permet de se connecter à un espace propriétaire existant

    Aucun paramètre ni retour

    Cette fonction est une étape de vérification et connexion,
    elle redirige vers l'espace propriétaire ou l'interface précédente
    '''

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

            # Permet de quitter en cas d'erreur de connexion
            rep_quit = input("Retour ? (Y/N)").lower()
            if rep_quit == "y":
                return
    
    id_proprietaire = resultat[0]
    prenom = resultat[2]
    print(" ")
    espace_prop(id_proprietaire, prenom)
    
def espace_prop(id_proprietaire, prenom):
    '''
    Cette fonction affiche l'espace propriétaire en un interface et
    permet d'accéder à toutes les fonctionnalités possibles
    pour les propriétaires de chiens : 
    - Enregistrer un chien
    - Rechercher un activité à partir de filtres ou d'une requête
    - Se déconnecter

    Paramètres : id_proprietaire : int
        id du propriétaire connecté
            prenom : str
        prenom du propriétaire pour l'affichage

    Retourne : Rien mais affiche l'interface et redirige vers les fonctions
    '''

    print("\n--- PROFIL PROPRIETAIRE ---")
    choix_cp = ' '

    while choix_cp not in ['1', '2', '3', '4']:
        print(f"Bonjour {prenom}")
        print("Que voulez-vous faire ?")
        print("1. Enregistrer un chien")
        print("2. Rechercher une activité pour mon ou mes chiens avec des filtres")
        print("3. Rechercher une activité pour mon ou mes chiens avec une requête")
        print("4. Me déconnecter")

        choix_cp = input("Entrez votre choix (1, 2, 3 ou 4) : ")
        while choix_cp not in ['1', '2', '3', '4']:
            choix_cp = input("Entrez votre choix (1, 2, 3 ou 4) : ")

    if choix_cp == '1':
        creation_chien(id_proprietaire, prenom)
    elif choix_cp == '2':
        print(" ")
        reservation(id_proprietaire, prenom)
    elif choix_cp == '3':
        recherche(id_proprietaire, prenom, k=3)
    else:
        return


def connexion_baladeur():
    '''
    Permet de se connecter à un espace baladeur existant

    Aucun paramètre ni retour

    Cette fonction est une étape de vérification et connexion,
    elle redirige vers l'espace baladeur ou l'interface précédente
    '''

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

            # Permet de quitter en cas d'erreur de connexion
            rep_quit = input("Retour ? (Y/N)").lower()
            if rep_quit == "y":
                return
            
    id_baladeur = resultat_b[0]
    prenom = resultat_b[2]
    print(" ")
    espace_baladeur(id_baladeur, prenom)


def espace_baladeur(id_baladeur, prenom):
    '''
    Cette fonction affiche l'espace baladeur en un interface et
    permet d'accéder à toutes les fonctionnalités possibles
    pour les baladeurs : 
    - Proposer une activité
    - Exporter les activités réalisées au format .csv
    - Visualiser graphiquement l'évolution de ses activités
    - Se déconnecter

    Paramètres : id_baladeur : int
        id du baladeur connecté
            prenom : str
        prenom du baladeur pour l'affichage

    Retourne : Rien mais affiche l'interface et redirige vers les fonctions
    '''

    print("\n--- PROFIL BALADEUR ---")
    choix_cb = ' '

    while choix_cb not in ['1', '2', '3', '4']:
        print(f"Bonjour {prenom}")
        print("Que voulez-vous faire ?")
        print("1. Proposer une balade")
        print("2. Exporter mes activités sous .csv")
        print("3. Visualiser l'évolution de mes activités")
        print("4. Me déconnecter")

        choix_cb = input("Entrez votre choix (1, 2, 3 ou 4) : ")
        while choix_cb not in ['1', '2', '3', '4']:
            choix_cb = input("Entrez votre choix (1, 2, 3 ou 4) : ")

    if choix_cb == '1':
        # Fonction d'enregistrement de nouvelles activités proposées
        enregistrement_nv_activite(id_baladeur,prenom)
    elif choix_cb == '2':
        # Fonction d'export des activités
        export_act(id_baladeur, prenom)
    elif choix_cb == '3':
        # Fonction visualisation évolution activités
        graphe_evol(id_baladeur, prenom)
    else:
        return

#--------------------------------
# Enregistrement d'un nouveau propriétaire
#--------------------------------

def creation_prop():
    '''
    Cette fonction permet de créer un compte propriétaire. 
    Les données sont ensuite envoyées vers la base de données SQL associée
    Il est alors possible d'être à la fois propriétaire et baladeur sous deux comptes différents.

    Aucun paramètre ni retour.
    Cette fonction affiche de question, enrichit la base de données avec les réponses
    et redirige vers l'espace propriétaire ou la page menu principal.
    '''

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

    while choix not in ["1", "2"]:
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
    '''
    Cette fonction permet d'afficher l'interface d'ajout d'un chien et d'enrichir ses données
    Elle affiche les questions et enrichit la base de données Chiens des données de chaque animal ajouté
    elle redirige ensuite vers l'espace propriétaire

    Paramètres : id_proprietaire : int
        permet d'associer le ou les chiens à leur propriétaire
            prenom : str
        utilisé pourb l'affichage

    Retourne : Rien, affiche les questions, enrichit la base de données et redirige vers la fonction espace_prop() associée
    '''

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
    '''
    Cette fonction permet de créer un compte baladeur. 
    Les données sont ensuite envoyées vers la base de données SQL associée
    Il est alors possible d'être à la fois propriétaire et baladeur sous deux comptes différents.

    Aucun paramètre ni retour.
    Cette fonction affiche des questions, enrichit la base de données avec les réponses
    et redirige vers l'espace baladeur.
    '''

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
    '''
    Cette fonction permet de proposer une nouvelle activité.
    Elle affiche les questions et enrichit la base  de données associées Activites_enregistrees.
    Elle l'enrichit des informations suivantes : 
        - Type d'activité :activite
        - la date (jour, mois, annee)
        - le moment dans la journée (moment)
        - le nombre de chiens pouvant être pris en charge (nb_chiens)
        - le tarif pour chaque chien (tarif)
    Elle redirige ensuite vers l'espace baladeur ou pour enregistrer une autre activité

    Paramètres : id_baladeur : int
        Permet de lier les bases de données Baladeurs et Activites_enregistrees avec cette clé
            prenom : str
        Utilisé pour l'affichage
    
    Retourne : rien mais affiche les questions, enrichit la base de données et redirige vers d'autres fonctions
    '''
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
    # Le deuxième élément [1] est le nombre maximum de jours dans ce mois précis.
    nb_jours_max = calendar.monthrange(annee, mois)[1]     
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
    '''
    Cette fonction permet de rechercher avec une recherche SQL précise et réserver une activité pour 1 ou plusieurs chiens.
    Elle vérifie que le propriétaire possède bien un ou des chiens
    Elle fait choisir le chien pour lequel on souhaite réserver
    Elle demande à l'utilisateur : 
        - le type d'activité désiré (activite)
        - la date (jour, mois, annee)
        - le moment de la journée (moment)
    Elle vérifie si une activité est disponible selon ces conditions
    Si oui execute la fonction reserver() qui permet de réserver une offre précise
    Elle redirige ensuite vers l'espace propriétaire.

    Paramètres : id_propriétaire : int
        Lie les tables Proprietaires, Chiens et Activites_reservees
            prenom : str
        Utilisé pour l'affichage

    Retourne : Rien
    '''
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
        moment = "Après-Midi"

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
    colonnes = colonnes = [
        "Id_Offre", "Nom Baladeur", "Prénom Baladeur", "Activité", "Jour",
        "Mois", "Année", "Moment", "Places Restantes", "Tarif", "Id_Baladeur"
        ]
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

    reserver(ligne_choisie, id_chien_selectionne, id_offre_choisie)

    print("")
    input("Appuyez sur Entrée pour revenir à votre espace...")
    espace_prop(id_proprietaire, prenom)


def reserver(ligne_choisie, id_chien_selectionne, id_offre_choisie):
    '''
    Cette fonction permet de réserver une offre d'activité.
    A partir d'une offre de la base de données Activites_enregistrees, 
    elle enrichit la base Activites_reservees selon les paramètres.
    Cette fonction actualise également l'offre de la base de données Activites_enregistrees
    en diminuant le nombre de place ou en supprimant l'offre si elle est complète.

    Paramètres : ligne_choisie : pandas.Series
        Ligne du DataFrame contenant toutes les informations
        de l'activité sélectionnée (baladeur, date, activité,
        tarif, nombre de places restantes, etc.).

    id_chien_selectionne : int
        Identifiant du chien pour lequel la réservation est effectuée.

    id_offre_choisie : int
        Identifiant de l'offre (Id_Enregistrement) dans la table
        Activites_enregistrees. Sert à mettre à jour ou supprimer
        l'offre après la réservation.

    Retourne : Rien, Modifie les bases de données SQL
    '''
    # 1. On récupère le Id_Enregistrement de MySQL qui était stocké dans la ligne
    if 'Id_Offre' in ligne_choisie: # Correction pour certaines différences de code pour nous eviter
    # de nous perdre avec les corrections
    # Avec ça, on s'assure une correction universelle
        vrai_id_enregistrement = int(ligne_choisie['Id_Offre'])
    elif 'Id_Enregistrement' in ligne_choisie:
        vrai_id_enregistrement = int(ligne_choisie['Id_Enregistrement'])
    else:
        print("Erreur : Impossible de trouver l'identifiant de l'activité.")
        return
    # 2. On va chercher le nombre de places ACTUEL en Base de Données
    query_places = "SELECT nb_chiens FROM Activites_enregistrees WHERE Id_Enregistrement = %s"
    cursor.execute(query_places, (vrai_id_enregistrement,))
    resultat_places = cursor.fetchone()
    
    if not resultat_places:
        print("Erreur : Cette activité n'existe plus.")
        return
        
    places_actuelles = int(resultat_places[0])
    
    # Sécurité : S'il n'y a plus du tout de place au moment du clic
    if places_actuelles <= 0:
        print("Désolé, il n'y a plus de places disponibles pour cette activité.")
        return
    
    query_reservation = """
    INSERT INTO Activites_reservees (Id_Baladeur, activite, jour, mois, annee, moment, tarif, Id_chien) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    reservation = (int(ligne_choisie['Id_Baladeur']), ligne_choisie['Activité'],
                   int(ligne_choisie['Jour']), int(ligne_choisie['Mois']),
                   int(ligne_choisie['Année']), ligne_choisie['Moment'],
                   float(ligne_choisie['Tarif']), id_chien_selectionne
                   )
    cursor.execute(query_reservation, reservation)
    places_dispo = places_actuelles - 1
    if places_dispo == 0:
        # Plus de places = on supprime la ligne de la table des offres disponibles
        query_update = "DELETE FROM Activites_enregistrees WHERE Id_Enregistrement = %s"
        cursor.execute(query_update, (vrai_id_enregistrement,))
        print("")
        print("Places épuisées pour cette offre, elle a été retirée des disponibilités.")
    else:
        query_update = "UPDATE Activites_enregistrees SET nb_chiens = %s WHERE Id_Enregistrement = %s"
        cursor.execute(query_update, (places_dispo, vrai_id_enregistrement))
        print("")
        print(f"Réservation enregistrée ! Il reste {places_dispo} place(s) pour cette activité.")
    db.commit()
    return
#--------------------------------
# Exporter les activités déjà faites + quantité argent gagnée
#--------------------------------
def export_act(id_baladeur, prenom):
    '''
    Cette fonction permet d'exporter les activités réalisées d'un baladeur au format .csv
    et affiche le gain total perçu.

    Paramètres : id_baladeur : int
        Identifiant du baladeur concerné, permet de sélectionnées seulement les activités souhaitée
            prenom : str
        Utilisé uniquement pour l'affichage et l'interface.

    Retourne : Rien mais permet de sauvegarder dans le dossier du script un fichier .csv
    contenant les activités réalisées
    et d'afficher le gain total. 
    '''
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
    colonnes_act = [
        "Id_Activite", "Id_Baladeur", "activite", "jour",
        "mois", "annee", "moment", "nb_chiens", "tarif"
        ]
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
        espace_baladeur(id_baladeur, prenom)
    else:
        print("Retour à votre profil")
        espace_baladeur(id_baladeur, prenom)
        return



#--------------------------------
# Visualisation graphique de l'évolution des activités
#--------------------------------
def graphe_evol(id_baladeur, prenom):
    '''
    Cette fonction permet d'afficher un graphe de l'évolution des activités
    Elle permet d'afficher le nombre, d'activités réalisées, le nombre de chiens pris en charge,
    les gains perçus et le type d'activité en fonction des mois d'une année.

    Paramètres : id_baladeur : int
        Permet de sélectionner les activités liées au baladeur
            prenom : str
        Utilisé pour l'affichage.

    Retourne : Rien mais affiche le graphe et redirige vers d'autres fonctions et interfaces
    '''
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
    colonnes_act = [
        "Id_Activite", "Id_Baladeur", "activite", "jour",
        "mois", "annee", "moment", "nb_chiens", "tarif"
        ]
    df_evol_act = pd.DataFrame(evol_act, columns=colonnes_act)
    df_evol_act = df_evol_act[["activite", "jour", "mois", "annee", "moment", "nb_chiens", "tarif"]]
    
    # On calcule le gain perçu pour chaque activité (tarif x nb_chiens)
    df_evol_act["gain_act"] = df_evol_act["tarif"]*df_evol_act["nb_chiens"]

    # Liste les années disponibles parmi les activités déjà réalisées
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
        # Somme le nombre de chiens pris en compte en groupant selon les mois
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
        # Somme les gains reçus en groupant selon les mois
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
        # On compte le nombre de ligne en regroupant selon les mois et le type d'activité
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

#--------------------------------
# Partie LLM
#--------------------------------

def export_baladeur():
    '''
    Cette fonction permet d'importer les données combinées des baladeurs (Baladeurs)
    et des activités proposées par les baladeurs (Activites_enregistrees). 
    Elle permet aussi de générer les textes génériques résumant les informations de chaque activité proposée.
    Ces textes pourront être alors utilisé en embedding ensuite.

    Paramètres : aucun

    Retourne : df_exp_act : pandas.Dataframe
        Ce dataframe contient toutes les données des activités proposées liées avec le baladeur associé.
            df_res : pandas.Dataframe
        Ce dataframe contient les textes résumant les offres. 
        Ces textes sont associés aux identifiants de l'activitée et du baladeur et au nom du baladeur
    '''
    query_expbal = '''SELECT * FROM Baladeurs b JOIN Activites_enregistrees ae ON b.Id_Baladeur = ae.Id_Baladeur;'''

    cursor.execute(query_expbal)
    act = cursor.fetchall()

    if not act:
        print("")
        print("[Attention] Aucune activité enregistrée.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        return
    
    colonnes_exp_act = [
        "Id_Baladeur", "nom", "prenom", "telephone", "mail", "mot_de_passe",
        "Id_Enregistrement", "Id_Baladeur_2", "activite", "jour", "mois",
        "annee", "moment", "nb_chiens", "tarif"
        ]
    df_exp_act = pd.DataFrame(act, columns= colonnes_exp_act)
    
    resultats = []

    for idx, row in df_exp_act.iterrows():
        texte = (
            f"{row['prenom']} {row['nom']} propose une {row['activite']} le {row['jour']}/{row['mois']}/{row['annee']} au moment : {row['moment']}. {row['nb_chiens']} place(s) est/sont disponible(s) à {row['tarif']} € chacune."
        )
        
        ligne = {
            "Id_Enregistrement": row["Id_Enregistrement"], "Id_Baladeur": row["Id_Baladeur"],
            "nom": row["nom"], "texte": texte
            }
        resultats.append(ligne)

    df_res = pd.DataFrame(resultats)

    return df_exp_act, df_res


def embed(text):
    '''
    Cette fonction génère l'embedding d'un texte à l'aide du modèle
    'nomic-embed-text' d'Ollama.

    Paramètres
    text : str
        Texte à convertir en vecteur numérique.

    Retourne :
    list[float]
        Vecteur d'embedding représentant le sens du texte
        dans un espace de 768 dimensions. Ce vecteur pourra ensuite
        être comparé à d'autres embeddings grâce à la
        similarité cosinus.
    '''
    reponse = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text)
    vecteur = reponse["embedding"]

    return vecteur


def embeddings_data(df):
    '''
    Cette fonction calcule et réunie toutes les coordonnées
    des vecteurs des textes du dataframe entré en paramètre

    Paramètre : df : pandas.Dataframe
        dataframe contenant une colonne "texte" dont on veut les coordonnées en embedding
    
    Retourne : embeddings : Array numpy
        Cet array contient les coordonnées de chaque vecteur de texte
    '''
    embeddings = []
    for i, row in df.iterrows():
        txt = row["texte"]
        vec = embed(txt)
        embeddings.append(vec)

    embeddings = np.array(embeddings)

    return(embeddings)


def recherche_baladeur(requete, embeddings, df, top_k=3):
    '''
    Cette fonction calcule la similarité de cosinus entre
    les coordonnées des vecteurs des textes et celles de la requête.
    Elle retourne ensuite les indices et les noms des top_k textes
    les plus proches de la requête en embedding

    Paramètres : requete : str
        texte de la requête donc on veut étudier la similarité
            embeddings : array numpy
        Array contenant les coordonnées des vecteurs des textes des activités proposées
            df : pandas.Dataframe
        Dataframe contenant la liste des activités proposées
            top_k : int
        Nombre de textes les  plus proches de la requête à renvoyer

    Retourne : idx_sorted : liste 
        Liste des indices des textes les plus proches
            res : Dictionnaire
        Dictionnaire contenant les noms des baladeurs pour les textes les plus proches
    '''
    q_emb = embed(requete)
    scores = cosine_similarity([q_emb], embeddings)[0]
    idx_sorted = np.argsort(scores)[::-1][:top_k]
    print("="*60)

    res = {}

    for rank, idx in enumerate(idx_sorted):
        print(f"{rank+1}. [{df.iloc[idx]['nom']}] score={scores[idx]:.3f}")
        res[f"{rank+1}"] = df.iloc[idx]['nom']
        print(df.iloc[idx]["texte"])
    return idx_sorted, res


def recherche(id_proprietaire, prenom, k = 3):
    '''
    Cette fonction demande une requête au propriétaire et recherche l'activité la plus proche.
    Cette fonction importe les données des activités proposées,
    calcule les embeddings des textes générés à partir des informations des activités,
    calcule la similarité cosinus de ces textes avec la requête en embedding
    et affiche les k activités les plus proche de la requête.
    Elle demande ensuite pour quels chiens réserver et réserver avec la fonction reserver().

    Paramètres : id_proprietaire : int
        permet de d'effectuer la réservation à ce nom et recherche le(s) chien(s) possédé(s)
            prenom : str
        utilisé pour l'affichage
            k : int
        défini le nombre d'activité à afficher en réponse à la requête, par défaut k = 3

    Retourne : Rien mais modifie les bases de données des activités proposées et réservées : 
    Activites_enregistrees et Activites_reservees. La fonction redirige aussi vers d'autres
    fonctions et interfaces. 
    '''
    print(60*"=")
    print("RECHERCHE PAR REQUETE")
    requete = input("Que recherchez vous ? ")

    df, df_res = export_baladeur()

    idx_sorted, res = recherche_baladeur(requete, embeddings_data(df_res), df_res, top_k=k)
    
    # Appel de la fonction RAG
    top_3_profils = df_res.iloc[idx_sorted]
    rag(requete, top_3_profils)

    print(f"{k+1}. Voir plus de résultats ou avec une autre requête")
    print(f"{k+2}. Retour à mon espace")
    choix_final = input("Que choisissez-vous (1, 2, 3, 4, ...) ?")

    while choix_final not in [str(i) for i in range(1, k+3)]:
        choix_final = input("Que choisissez-vous (1, 2, 3, 4, ...) ?")
    
    if choix_final == str(k+1):
        new_k = input("Combien de résultats voulez-vous voir ? ")

        while not new_k.isdigit() or int(new_k) <= 0:
            new_k = input("Veuillez entrer un nombre entier positif : ")

        new_k = int(new_k)

        recherche(id_proprietaire, prenom, k = new_k)
        return
    elif choix_final == str(k+2):
        print("Retour à votre espace ...")
        espace_prop(id_proprietaire, prenom)
        return
    else :
        id_offre_choisie = idx_sorted[int(choix_final)-1]
        
        ligne_choisie = df.iloc[id_offre_choisie]
        ligne_choisie = ligne_choisie[[
            "Id_Enregistrement", "Id_Baladeur", "activite", "jour", "mois",
            "annee", "moment", "nb_chiens", "tarif"
            ]]
        ligne_choisie = ligne_choisie.rename({
            "activite": "Activité",
            "jour": "Jour",
            "mois": "Mois",
            "annee": "Année",
            "moment": "Moment",
            "tarif": "Tarif",
            "nb_chiens": "Places Restantes"
        })

        print("Vos chiens : ")
        query_chiens = '''SELECT * FROM Chiens WHERE Id_Proprietaire = %s;'''
        cursor.execute(query_chiens, (id_proprietaire,))
        chiens_dispo = pd.DataFrame(
            cursor.fetchall(), columns=[
                "Id_chien", "nom_chien", "race_chien", "temperament", "Id_Proprietaire"
                ]
                                    )

        for idc, row in chiens_dispo.iterrows():
            rep = input(f"Voulez vous réserver pour {row['nom_chien']} (y/n)").lower()
            while rep not in ["y", "n"]:
                rep = input(f"Voulez vous réserver pour {row['nom_chien']} (y/n)").lower()

            if rep == "y":
                reserver(ligne_choisie, row["Id_chien"], id_offre_choisie)

        
        print("Retour à l'espace personnel ...")
        espace_prop(id_proprietaire, prenom)
        return  


def rag(requete, profils_selectionnes):
    '''
    Cette fonction utilise un LLM via Ollama pour générer 
    une recommandation personnalisée de baladeur basée sur la requête du propriétaire 
    et une sélection de profils d'activités.

    Paramètres :
        requete : str
            La demande et les critères saisis par le propriétaire.
        profils_selectionnes : pandas.DataFrame
            Un DataFrame contenant les profils des k activités les plus pertinentes 
            trouvées lors de la recherche par similarité.

    Retourne :
        Rien. La fonction affiche directement la recommandation textuelle de l'IA 
        dans la console.
    '''
    context = profils_selectionnes.to_string(index=False)
    prompt = f"""
Tu es un assistant pour le site balade-mon-chien.com. 
À partir des profils ci-dessous, recommande le baladeur le plus adapté à la demande du propriétaire.

CONTEXTE (Profils disponibles) :
{context}

DEMANDE DU PROPRIÉTAIRE :
{requete}

RÉPONSE (Sois concis, amical et explique brièvement pourquoi ce choix) :
"""
    print("\nL'IA analyse les profils pour vous...")

    response = ollama.generate(
        model="llama3.2:3b",
        prompt=prompt
    )
    
    print("\n" + "=" * 60)
    print("LA RECOMMANDATION DE NOTRE IA")
    print("=" * 60)
    print(response["response"])
    print("=" * 60 + "\n")

prelancement()