from joueur import Joueur

class Jeu:
    def __init__(self):
        self.joueurs = []

    def jouer(self, joueur1_nom, joueur2_nom):
        
        argent_joueur1 = 1000  
        joueur1 = Joueur(joueur1_nom)
        self.achat_pokemons(joueur1, argent_joueur1)

        
        argent_joueur2 = 1000  
        joueur2 = Joueur(joueur2_nom)
        self.achat_pokemons(joueur2, argent_joueur2)

        print("Début du combat!")

        
        for i in range(3):
            print(f"Round {i+1}:")
            self.round(joueur1, joueur2)

        
        if joueur1.manche_gagnee >= 2:
            print(f"{joueur1.nom} remporte la victoire!")
        elif joueur2.manche_gagnee >= 2:
            print(f"{joueur2.nom} remporte la victoire!")
        else:
            print("Aucun vainqueur n'a été déterminé.")

        
        rejouer = input("Voulez-vous rejouer? (Oui/Non): ").lower()
        if rejouer == "oui":
            joueur1_nom = input("Joueur 1, veuillez saisir votre nom: ")
            joueur2_nom = input("Joueur 2, veuillez saisir votre nom: ")
            self.jouer(joueur1_nom, joueur2_nom)
        else:
            print("Merci d'avoir joué!")

    def achat_pokemons(self, joueur, argent_disponible):
        print(f"{joueur.nom}, vous disposez de {argent_disponible} d'argent.")
        print("Voici la liste des Pokémons disponibles à l'achat:")
        
