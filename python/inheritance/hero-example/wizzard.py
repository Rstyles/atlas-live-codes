from hero import Hero


class Wizzard(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Staff")
        
    def cast_spell(self, spell: str) -> None:
        print(f"{self.name} is casting {spell}")
        
    def attack(self) -> None:
        self.cast_spell("Fireball")