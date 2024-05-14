from hero import Hero


class Archer(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Bow")