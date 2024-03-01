from attaque import Attaque
from pokemon import Pokemon

attaques_pokemon = {
    "Bulbizarre": [
        Attaque("Fouet Lianes", "Plante", 45, "Physique", 100, 25),
        Attaque("Tranch'Herbe", "Plante", 55, "Physique", 95, 20),
        Attaque("Bomb-Graine", "Plante", 80, "Physique", 100, 15),
        Attaque("Lance-Soleil", "Plante", 120, "Spéciale", 100, 10)
    ],
    "Salameche": [
        Attaque("Lance-Flamme", "Feu", 90, "Spéciale", 100, 15),
        Attaque("Tranche", "Normal", 70, "Physique", 100, 20),
        Attaque("Flammèche", "Feu", 40, "Spéciale", 100, 25),
        Attaque("Griffe", "Normal", 40, "Physique", 100, 35)
    ],
}

donnees_pokemon = {
    "Bulbizarre": {
        "types": ["Plante"],
        "pv": 45,
        "niveau": 5,
        "prix": 100,
        "attaque": 10,
        "attaque_speciale": 15,
        "defense": 12,
        "defense_speciale": 13,
        "vitesse": 8
    },
    "Salameche": {
        "types": ["Feu"],
        "pv": 39,
        "niveau": 5,
        "prix": 100,
        "attaque": 12,
        "attaque_speciale": 10,
        "defense": 9,
        "defense_speciale": 11,
        "vitesse": 10
    }
}

pokemons = []

for nom_pokemon, attaques in attaques_pokemon.items():
    donnees_base = donnees_pokemon.get(nom_pokemon, {})
    pokemon = Pokemon(
        nom=nom_pokemon,
        prix=donnees_base.get("prix"),
        types=donnees_base.get("types", []),
        pv=donnees_base.get("pv"),
        niveau=donnees_base.get("niveau"),
        attaque=donnees_base.get("attaque"),
        attaque_speciale=donnees_base.get("attaque_speciale"),
        defense=donnees_base.get("defense"),
        defense_speciale=donnees_base.get("defense_speciale"),
        vitesse=donnees_base.get("vitesse"),
        attaques=attaques
    )
    pokemons.append(pokemon)
