from models.Pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.party_pokemon = []
        self.boxed_pokemon = []

    def encounter_pokemon(self, pokemon: Pokemon):
        print(f"A wild {pokemon.name} appeared!")
        catch_decision = input("Would you like to catch it? (Y/N)")
        if catch_decision.lower() == "y":
            self.catch_pokemon(pokemon)
            print(f"You caught {pokemon.name}!")
        else:
            print(f"{pokemon.name} ran away!")

    def catch_pokemon(self, pokemon: Pokemon) -> None:
        nickname_decision = input(f"Would you like to give {pokemon.name} a nickname? (Y/N)")
        if nickname_decision.lower() == "y":
            nickname = input("Enter a nickname: ")
            pokemon.nickname = nickname
            print(f"{pokemon.name} was nicknamed {nickname}!")

        if self.party_full():
            self.boxed_pokemon.append(pokemon)
            print(f"{pokemon.name} was added to your box!")
        else:
            self.party_pokemon.append(pokemon)
            pokemon.is_caught = True
            print(f"{pokemon.name} was added to your party!")


    def party_full(self) -> bool:
        return len(self.party_pokemon) >= 6

    def print_party(self):
        print("----------------------------------------")
        print(f"{self.name}'s Party:")
        for pokemon in self.party_pokemon:
            print(pokemon)
        print("----------------------------------------")

    def print_boxed(self):
        for pokemon in self.boxed_pokemon:
            print(pokemon)
