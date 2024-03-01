class Attaque:
    def __init__(self, nom, type_attaque, categorie, precision, puissance, pp):
        self.nom = nom
        self.type_attaque = type_attaque
        self.categorie = categorie
        self.precision = precision
        self.puissance = puissance
        self.pp = pp

    def afficher(self):
        print("Nom:", self.nom)
        print("Type:", self.type_attaque)
        print("Catégorie:", self.categorie)
        print("Précision:", self.precision)
        print("Puissance:", self.puissance)
        print("PP:", self.pp)
