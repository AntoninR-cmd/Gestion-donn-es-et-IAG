def main():

    while True:
        print(f"Menu: \t")
        print("1. Nouveau Compte")
        print("2. Accès à mon compte")
        print("3. Quitter")

        choix_main = " "

        while choix_main not in ['1', '2', '3']:
            choix_main = input("Veuillez entrer votre choix (1, 2 ou 3) : ")

        if choix_main == '1':
            nouveau_compte()
        elif choix_main == '2':
            acces_compte()
        elif choix_main == '3':
            print("Au revoir")
            break

def nouveau_compte():
    print("Création d'un nouveau compte")
    print("Faites votre choix :")
    print("1. Je suis propriétaire et souhaite réserver une balade pour mon ou mes chiens")
    print("2. Je suis baladeur et souhaite proposer des balades à des proprétaires de chiens")
    print("3. Revenir en arrière")

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

    nom = resultat[1]
    prenom = resultat[2]

    choix_cp = ' '

    while choix_cp not in ['1', '2', '3']:
        print(f"Bonjour {prenom}")
        print("Que voulez-vous faire ?")
        print("1. Enregistrer un chien")
        print("2. Rechercher une balade pour mon ou mes chiens")
        print("3. Me déconnecter")

        choix_cp = input("")

    if choix_cp == '1':
        creation_chien()
    elif choix_cp == '2':
        # Fonction de recherche de balade
        print(" ")
    else:
        return


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

    nom = resultat_b[1]
    prenom = resultat_b[2]

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
        # Fonction création d'une balade
        print(' ')
    elif choix_cb == '2':
        # Fonction d'export des act
        print(" ")
    elif choix_cb == '3':
        # Fonction visulaisation évolution act
        print(' ')
    else:
        return

main()