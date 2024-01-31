import requests
from models.Pokemon import Pokemon


class PokeApiRepository:
    baseUrl = "https://pokeapi.co/api/v2/"

    def get_pokemon(self, name) -> Pokemon:
        """
        Retrieves a Pokemon object by making a GET request to the API using the provided name.
        
        Args:
            name (str): The name of the Pokemon to retrieve.
        
        Returns:
            Pokemon: A Pokemon object representing the retrieved Pokemon.
        """
        
        result = requests.get(self.baseUrl + "pokemon/" + name)
        json = result.json()
        self.pokemon = Pokemon(**json)
        return self.pokemon
