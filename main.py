from joueur import Joueur
from donnees import pokemons
from pokemon import Pokemon

print("******** BATTLE POKEMON *********")


nom_joueur1 = input("Quel est ton nom Player 1? : ")
confirmation_nom_joueur1 = input(f"Ton nom est {nom_joueur1}? (Oui/Non): ").lower()

while confirmation_nom_joueur1 == "non":
    nom_joueur1 = input("Veuillez saisir à nouveau votre nom Player 1 : ")
    confirmation_nom_joueur1 = input(f"Ton nom est {nom_joueur1}? (Oui/Non): ").lower()

joueur1 = Joueur(nom_joueur1)


nom_joueur2 = input("Quel est ton nom Player 2 ? : ")
confirmation_nom_joueur2 = input(f"Ton nom est {nom_joueur2}? (Oui/Non): ").lower()

while confirmation_nom_joueur2 == "non":
    nom_joueur2 = input("Veuillez saisir à nouveau votre nom Player 2 : ")
    confirmation_nom_joueur2 = input(f"Ton nom est {nom_joueur2}? (Oui/Non): ").lower()

joueur2 = Joueur(nom_joueur2)

print(f"Bienvenue {nom_joueur1} et {nom_joueur2} ! ")

print("\nPokémons disponibles pour", nom_joueur1)
for i, pokemon in enumerate(pokemons, start=1):
    print(f"{i}. {pokemon.nom}")


pokemon_joueur1 = pokemons[int(input(f"\n{joueur1.nom}, choisissez un Pokémon (saisissez le numéro) : ")) - 1]
joueur1.ajouter_pokemon(pokemon_joueur1)
print(f"{nom_joueur1} a choisi {pokemon_joueur1.nom}.\n")


print("\nPokémons disponibles pour", nom_joueur2)
for i, pokemon in enumerate(pokemons, start=1):
    print(f"{i}. {pokemon.nom}")

pokemon_joueur2 = pokemons[int(input(f"\n{joueur2.nom}, choisissez un Pokémon (saisissez le numéro) : ")) - 1]
joueur2.ajouter_pokemon(pokemon_joueur2)
print(f"{nom_joueur2} a choisi {pokemon_joueur2.nom}.\n")