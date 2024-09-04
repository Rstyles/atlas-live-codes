from models.Pokemon import Pokemon
from models.Trainer import Trainer


bob = Trainer("Bob")
bob.print_party()
bob.print_boxed()

pikachu = Pokemon("Pikachu", ["Electric"])
bulbasaur = Pokemon("Bulbasaur", ["Grass", "Poison"])
charmander = Pokemon("Charmander", ["Fire"])
squirtle = Pokemon("Squirtle", ["Water"])

bob.encounter_pokemon(pikachu)
bob.encounter_pokemon(pikachu)

bob.print_party()
