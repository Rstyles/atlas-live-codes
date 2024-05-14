class Hero:
    def __init__(self, name: str, weapon: str) -> None:
        self.name = name
        self.weapon = weapon

    def attack(self) -> None:
        print(f"{self.name} is attacking with a {self.weapon}")

    def __str__(self) -> str:
        return f"{self.name} is a(n) {self.__class__.__name__} and is equiped with a {self.weapon}"