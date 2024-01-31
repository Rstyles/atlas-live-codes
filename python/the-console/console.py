#!/usr/bin/python3
import cmd
from models.Pokemon import Pokemon
from repository.PokeApiRepository import PokeApiRepository

"""
A simple Pokedex command line interface
"""


class Pokedex(cmd.Cmd):
    """
    Pokedex command line interface.
    """

    intro = "Type help or ? to list commands."
    prompt = "(pokedex) "

    def do_search(self, name):
        """
        Retrieves a Pokemon by using the provided name.

        Args:
            name (str): The name of the Pokemon to retrieve.

        Returns:
            None
        """
        repo = PokeApiRepository()

        pokemon = repo.get_pokemon(name)

        print("Retrieving Pokemon...")
        
        # print the name
        print(pokemon.name)

        # print the types
        print("Types: " + ", ".join(pokemon.types))

        # print the abilities
        print("Abilities: " + ", ".join(pokemon.abilities))

        # print the stats as a table
        print("{:<20} {:<20}".format("Stat", "Value"))
        print("{:<20} {:<20}".format("-----", "-----"))
        for stat, value in pokemon.stats.items():
            print("{:<20} {:<20}".format(stat, value))

    def do_exit(self, arg):
        """
        Exits the Pokedex command line interface.

        Returns:
            None
        """
        print("Goodbye!")
        return True

    def do_quit(self, arg):
        """
        Quits the Pokedex command line interface.

        Returns:
            None
        """
        print("Goodbye!")
        return True


if __name__ == "__main__":
    Pokedex().cmdloop()
