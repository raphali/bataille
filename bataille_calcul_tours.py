import random


def init_cards():  # Crée un paquet de 52 cartes
    cartes = [
        "As",
        "Roi",
        "Dame",
        "Valet",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
    ]
    symboles = ["♣", "♠", "♦", "♥"]
    lst_cards = [f"{carte} {symbole}" for symbole in symboles for carte in cartes]
    random.shuffle(lst_cards)  # Mélange le paquet de cartes
    return lst_cards


def distribution(lst_cards): # Distribue les cartes à un joueur puis à l'autre 26 fois de maniére à distribuer tout le paquet
    main_ordi1 = []
    main_ordi2 = []
    for i in range(26):
        main_ordi1.append(lst_cards[0])
        lst_cards.pop(0)
        main_ordi2.append(lst_cards[0])
        lst_cards.pop(0)
    return main_ordi1, main_ordi2


def valeur_cartes(carte): # Définie une valeur pour chacune des cartes du paquet de manière à simplifier la fonction jeu qui suit
    valeurs = {
        "As": 14,
        "Roi": 13,
        "Dame": 12,
        "Valet": 11,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    nom = carte.split()[0] 
    return valeurs[nom]

def jeu(main_ordi1, main_ordi2): # Définie les régles de jeu
    compteur = 0
    while main_ordi1 and main_ordi2: # Tant qu'il reste des cartes dans main_ordi1 et main_ordi2
        compteur+=1
        carte1=main_ordi1.pop(0) # La premiére carte de main_ordi1 est retourné (et donc supprimée du paquet)
        carte2=main_ordi2.pop(0) # La premiére carte de main_ordi2 est retourné (et donc supprimée du paquet)
        if valeur_cartes(carte1) > valeur_cartes(carte2): # Si la carte de main_ordi1 est supérieur à celle de main_ordi2 ...
            main_ordi1.extend([carte1, carte2]) # ... main_ordi1 récupére les cartes mises en jeu
        elif valeur_cartes(carte1) < valeur_cartes(carte2): # Si la carte de main_ordi2 est supérieur à celle de main_ordi1 ...
             main_ordi2.extend([carte2, carte1]) # ... main_ordi2 récupére les cartes mises en jeu
        else:
            if len(main_ordi1) > 3 and len(main_ordi2) > 3: # Vérifie si les 2 joueurs ont encore au moins 3 cartes chacun (nécessité pour les batailles)
                bataille1 = [carte1] + main_ordi1[:3] # main_ordi1[:3] correspond au 3 cartes supplémentaires jouées dans la bataille et bataille1 correspond au 4 cartes jouées dans la bataille par l'ordi1
                bataille2 = [carte2] + main_ordi2[:3]
                main_ordi1 = main_ordi1[3:]
                main_ordi2 = main_ordi2[3:]
                if valeur_cartes(bataille1[-1]) > valeur_cartes(bataille2[-1]): # Compare les valeurs des dernières cartes posées
                    main_ordi1.extend(bataille1 + bataille2) # En cas de victoires, main_ordi1 récupére toute les cartes mises en jeu lors de la partie
                elif valeur_cartes(bataille1[-1]) < valeur_cartes(bataille2[-1]): # Compare les valeurs des dernières cartes posées
                    main_ordi2.extend(bataille2 + bataille1) # En cas de victoires, main_ordi2 récupére toute les cartes mises en jeu lors de la partie
            else:
                break
    if main_ordi1: # En cas de victoire de l'ordi1
        print(f"L'ordinateur 1 a gagné en {compteur} tours!")
    else: # En cas de victoire de l'ordi2
        print(f"L'ordinateur 2 a gagné en {compteur} tours!")

deck = init_cards()
main_ordi1, main_ordi2 = distribution(deck)
jeu(main_ordi1, main_ordi2)
