class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.manche_gagnee = 0
        self.argent = 0
        self.pokemons = []

    def choisir_pokemon(self):
        
        pass

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon):
        
        pass

    def recuperer_pokemon(self, numero):
        return self.pokemons[numero - 1]

    def afficher_pokemons(self):
        for i, pokemon in enumerate(self.pokemons):
            print(f"Pokemon {i+1}:")
            pokemon.afficher()

    def afficher(self):
        print("Nom:", self.nom)
        print("Manche gagnée:", self.manche_gagnee)
        print("Argent:", self.argent)
