class Pokemon:
    def __init__(self, nom, prix, types, pv, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse, attaques):
        self.nom = nom
        self.prix = prix
        self.types = types
        self.pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = attaques

    def ajouter_attaque(self, attaque):
        self.attaques.append(attaque)

    def afficher_attaques(self):
        for i, attaque in enumerate(self.attaques):
            print(f"Attaque {i+1}:")
            attaque.afficher()

    def afficher(self):
        print("Nom:", self.nom)
        print("Prix:", self.prix)
        print("Types:", [type.get_nom() for type in self.types])
        print("Points de Vie:", self.pv)
        print("Niveau:", self.niveau)
        print("Attaque:", self.attaque)
        print("Attaque Spéciale:", self.attaque_speciale)
        print("Défense:", self.defense)
        print("Défense Spéciale:", self.defense_speciale)
        print("Vitesse:", self.vitesse)

    def get_points_de_vie(self):
        return self.points_de_vie

    def set_points_de_vie(self, new_pv):
        self.points_de_vie = new_pv
