from hero import Hero


class Knight(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Sword")

    def defend(self) -> None:
        print(f"{self.name} is defending with a Shield")