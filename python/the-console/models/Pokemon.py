class Pokemon:
    def __init__(self, **response):
        """
        Initializes the class instance with the given response dictionary.

        Args:
            **response (dict): The response dictionary containing information.

        Returns:
            None
        """
        self.name: str = response.get("name")
        
        self.types = []
        for type in response.get("types"):
            self.types.append(type.get("type").get("name"))
            
        self.abilities = []
        for ability in response.get("abilities"):
            self.abilities.append(ability.get("ability").get("name"))
            
        self.stats = {}
        for stat in response.get("stats"):
            self.stats[stat.get("stat").get("name")] = stat.get("base_stat")
            

    def __str__(self) -> str:
        return self.name
